#!/usr/bin/env bash
# Exit on error
set -o errexit

cd Quiz_BE

# Install dependencies
pip install -r requirements.txt

# Apply database migrations
python manage.py migrate

