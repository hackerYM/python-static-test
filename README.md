## Python Static Test Template

### About

The simple template to prepare static tests on a Python project.

### Project setup

1. [Install a macOS packages management - brew](https://brew.sh/)

1. [Install a Python version management - pyenv](https://github.com/pyenv/pyenv)

1. [Install a dependency management - poetry]((https://python-poetry.org/docs/))

1. Create a virtual environment

   ```bash
   poetry env use python3.7
   poetry env list
   poetry env info
   ```

1. Inspect Python requirements

   ```bash
   poetry show
   poetry show --tree
   poetry show <package> --tree
   ```

1. Install Python packages

   ```bash
   poetry install
   poetry install -E unit-test
   poetry install -E static-test

   poetry shell
   pre-commit install
   pre-commit run --all-files  # git hook scripts
   ```

### Utility Commands

1. Run the server

    ```shell
    python manage.py run
    ```

1. Get all routes

    ```shell
    python manage.py routes
    ```
