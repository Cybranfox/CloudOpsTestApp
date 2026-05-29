#!/usr/bin/env bash

# Set project and offline folder paths
PROJECT_DIR="$(pwd)"
OFFLINE_DIR="${PROJECT_DIR}/CloudQuest_Offline"

# Step 1: Verify the offline package exists
if [ ! -d "$OFFLINE_DIR" ]; then
    echo "Error: Offline package folder 'CloudQuest_Offline' not found in current directory."
    exit 1
fi

# Step 2: Check if Python is installed
if ! command -v python &> /dev/null; then
    echo "Error: Python not found. Please install Python for Windows or via WSL."
    exit 1
fi

# Step 3: Verify or install pip
if ! command -v pip &> /dev/null; then
    echo "Error: pip not found. Please install pip and ensure it's in your PATH."
    exit 1
fi

# Step 4: Confirm Flask is installed in Python environment
if ! python -c "import flask" 2>/dev/null; then
    echo "Installing Flask in your Python environment..."
    pip install --quiet flask
fi

# Step 5: Launch the app in the offline folder
echo "Starting the offline CloudQuest RPG..."
cd "$OFFLINE_DIR"

# Optional: Run the app in background or in current terminal
python run_cloudquest.py
