"""
System file to manage the Gunicorn configuration
"""
from deployment import main

# Official docs:
# https://docs.gunicorn.org/en/stable/settings.html
# https://github.com/benoitc/gunicorn/blob/master/examples/example_config.py

# Tech reference:
# https://www.agiliq.com/blog/2017/11/how-performant-your-python-web-application/
# https://medium.com/building-the-system/gunicorn-3-means-of-concurrency-efbb547674b7


# Logging info

loglevel = "info"

# Worker processes

threads = 2
workers = main.worker_count
worker_class = "gthread"

# Server socket

bind = "0.0.0.0:8080"
graceful_timeout = 60
timeout = 60

max_requests = 80
max_requests_jitter = 120

# Server hooks


def pre_fork(server, worker):
    """
    Method to be called just before a worker is forked
    """
    server.log.info(f"Prepare worker with pid: {worker.pid}")


def worker_exit(server, worker):
    """
    Method to be called just after a worker has been exited, in the worker process
    """
    server.log.info(f"Worker stopped (pid: {worker.pid})")


def when_ready(server):
    """
    Method to be called just after the server is started
    """
    server.log.info(f"Main server is ready. Spawning {server.num_workers} workers")
