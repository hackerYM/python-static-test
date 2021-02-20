# Python Static Test

### About

![GitHub](https://img.shields.io/github/license/hackerYM/python-static-test?color=blue)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/hackerYM/python-static-test?color=blue)
![Code Style](https://img.shields.io/badge/code%20style-flake8-000000.svg)

The simple template to prepare static tests on any Python projects, and we use [Flask](https://github.com/pallets/flask)
to build a simple API services as our example.


### Project setup

1. [Install a macOS packages management - brew](https://brew.sh/)

1. [Install a Python version management - pyenv](https://github.com/pyenv/pyenv)

1. [Install a dependency management - poetry](https://python-poetry.org/docs/)

1. Create a virtual environment

   ```bash
   poetry env use python3.7
   poetry env list
   poetry env info
   ```

   ![Sample Image](images/sample-01.png)

1. Inspect Python packages

   ```bash
   poetry show
   poetry show --tree
   poetry show <package> --tree
   ```

   ![Sample Image](images/sample-02.png)

1. Install Python packages

   ```bash
   poetry install
   poetry install -E unit-test -E static-test

   poetry shell  # Spawn a shell within the virtual environment
   ```


### Git hook scripts

1. Enable [pre-commit](https://pre-commit.com/) package manager

   ```bash
   pre-commit install
   ```

1. Config in [pre-commit-config.yaml](.pre-commit-config.yaml)

1. Run against all the files

   ```bash
   pre-commit run --all-files
   ```

   ![Sample Image](images/sample-03.png)

### Code Linter

We use [Flake8](https://flake8.pycqa.org/en/latest/) and [FlakeHell](https://flakehell.readthedocs.io/index.html) to
perform static analysis of source code checking for symantec discrepancies to follow the coding standards.

- [Flake8 Extensions](https://github.com/DmytroLitvinov/awesome-flake8-extensions)

- [Flake8 Rules](https://lintlyci.github.io/Flake8Rules/)

- [Bandit Rules](https://bandit.readthedocs.io/en/latest/plugins/index.html#complete-test-plugin-listing)

1. Config in [pyproject.toml](pyproject.toml)

   ```toml
   [tool.flakehell]
   plugins-rule = "..."

   [tool.flakehell.plugins]
   package-name = ["+*", "..."]
   ```

1. Inspect Flake8 plugins

   ```shell
   flakehell plugins
   flakehell codes <package-name>
   ```

   ![Sample Image](images/sample-04.png)
   ![Sample Image](images/sample-05.png)

1. Run patched flake8 against the code

   ```shell
   flakehell lint
   ```

   ![Sample Image](images/sample-06.png)


### Security Check

We use [Safety](https://github.com/pyupio/safety) to check installed Python dependencies for known security
vulnerabilities.

```shell
safety check
poetry export -E unit-test -E static-test | safety check --stdin
```

![Sample Image](images/sample-07.png)


### CI / CD

It also can generate [Code Quality](https://docs.gitlab.com/ee/user/project/merge_requests/code_quality.html) artifact
compatible with [Gitlab CI](.gitlab-ci.yml).

```json
[
    {
        "description": "C812 missing trailing comma",
        "fingerprint": "adfe44c4361050aa765c9e2e4ee93c3d",
        "location": {
            "path": "./app/controllers/index.py",
            "lines": {
                "begin": 17
            }
        }
    }
]
```

![Test Report](https://docs.gitlab.com/ee/user/project/merge_requests/img/code_quality.png)
