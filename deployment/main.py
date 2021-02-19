"""
System file to run the main application
"""
import multiprocessing
from app.app import create_app


def _create_flask_app():
    """
    Method to create one Flask application
    """
    return create_app()


def _ideal_worker_count():
    """
    Method to recommend (2 x $num_cores) + 1 as the number of workers
    """
    return multiprocessing.cpu_count() * 2 + 1


flask_app = _create_flask_app()
worker_count = _ideal_worker_count()
