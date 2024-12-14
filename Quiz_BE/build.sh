#!/usr/bin/env bash
# Exit on error
set -o errexit

# Install dependencies
pip install -r Quiz_BE/requirements.txt

# Apply database migrations
python Quiz_BE/manage.py migrate

cd Quiz_BE