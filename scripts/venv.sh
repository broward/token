#!/bin/bash
# remove existing environment
rm -r -f sdt_venv

# Script to create a Python virtual environment
sudo apt install python3.9-venv

# Set the virtual environment name
VENV_NAME="sdt_venv"

# Check if the virtual environment already exists
if [ -d "$VENV_NAME" ]; then
  echo "Virtual environment '$VENV_NAME' already exists."
  exit 1
fi

# Create the virtual environment
python3.9 -m venv "$VENV_NAME"

# Check if the creation was successful
if [ $? -eq 0 ]; then
  echo "Virtual environment '$VENV_NAME' created successfully."
  eval source $VENV_NAME/bin/activate
else
  echo "Failed to create virtual environment '$VENV_NAME'."
  exit 1
fi

# Provide instructions on how to activate the virtual environment
echo "To activate the virtual environment, run:"
echo "source $VENV_NAME/bin/activate"
