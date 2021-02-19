#!/bin/bash

gunicorn -c deployment/gconfig.py deployment.main:flask_app
