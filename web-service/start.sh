#!/bin/bash
export FLASK_APP="$(pwd)/core.py"
flask run --host="0.0.0.0" --port="80"