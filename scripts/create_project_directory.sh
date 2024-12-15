#!/bin/bash

# Script to create a standard directory structure for a Python project

# Check if a project name is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <project_name>"
    exit 1
fi

PROJECT_NAME=$1

# Create the base directory for the project
mkdir -p "$PROJECT_NAME"

# Navigate to the project directory
cd "$PROJECT_NAME" || exit

# Create the standard directory structure
mkdir -p \
    "$PROJECT_NAME" \
    tests \
    docs \
    scripts \
    data \
    config \
    logs

# Create placeholder files
touch \
    "$PROJECT_NAME"/__init__.py \
    README.md \
    .gitignore \
    requirements.txt \
    setup.py

# Add example content to the README.md
cat <<EOF > README.md
# $PROJECT_NAME

## Description
A Python project.

## Installation
\`\`\`
pip install -r requirements.txt
\`\`\`

## Usage
\`\`\`
python -m $PROJECT_NAME
\`\`\`

## Testing
\`\`\`
pytest
\`\`\`
EOF

# Add example content to .gitignore
cat <<EOF > .gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Virtual environment
venv/
.env/

# Logs
logs/

# Local configurations
*.env
*.local

# Jupyter Notebook checkpoints
.ipynb_checkpoints/

# Pytest cache
.pytest_cache/
EOF

# Add example content to setup.py
cat <<EOF > setup.py
from setuptools import setup, find_packages

setup(
    name="$PROJECT_NAME",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "$PROJECT_NAME=$PROJECT_NAME.__main__:main",
        ]
    },
)
EOF

# Add example __main__.py in the package
cat <<EOF > "$PROJECT_NAME"/__main__.py
def main():
    print("Welcome to $PROJECT_NAME!")

if __name__ == "__main__":
    main()
EOF

echo "Python project directory structure created for '$PROJECT_NAME'."

