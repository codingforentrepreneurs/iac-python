#!/bin/bash

APP_PORT=${PORT:-8000}

/opt/venv/bin/gunicorn -k uvicorn.workers.UvicornWorker src.main:app --bind "0.0.0.0:${APP_PORT}"