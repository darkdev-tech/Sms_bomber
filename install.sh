#!/bin/bash

echo "Installing dependencies..."
pkg update && pkg upgrade -y
pkg install python -y
pip install -r requirements.txt

echo "Setup complete! You can now run 'python smsbomber.py'."
