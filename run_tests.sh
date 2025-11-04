#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

echo "Activating Python virtual environment..."
source ./.Deep_Blue_Analytics/bin/activate

echo "Running unit tests..."
python -m unittest discover tests

echo "Tests completed successfully."