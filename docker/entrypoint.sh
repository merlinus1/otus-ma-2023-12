#!/bin/bash

source /app/.venv/bin/activate
uvicorn --host 0.0.0.0 --port 8000 app.main:app