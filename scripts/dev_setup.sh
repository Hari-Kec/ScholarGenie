#!/bin/bash

echo "Setting up ScholarGenie environment..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "Setup complete."
