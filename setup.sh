#!/usr/bin/env bash

echo "Creating virtual environment..."
python3 -m venv venv

echo "Activate virtual environment..."
source venv/bin/activate

echo "Install dependencies from requirements.txt..."
pip install -r requirements.txt
