#!/bin/bash

# Install Homebrew (if not already installed)
if ! command -v brew &> /dev/null; then
    echo "Homebrew not found. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Install Python (if not already installed)
if ! command -v python3 &> /dev/null; then
    echo "Python3 not found. Installing Python3..."
    brew install python
fi

# Create a virtual environment
echo "Creating virtual environment..."
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run the guru_test.py script
echo "Running guru_test.py..."
python -m unittest guru_test.py

# Deactivate the virtual environment
deactivate

echo "Testing completed."
