#!/bin/bash

# Check if python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found. Please install Python 3."
    exit 1
fi

# Check if pip is installed, if not, install it
if ! command -v pip3 &> /dev/null
then
    echo "pip3 could not be found. Installing pip..."
    python3 -m ensurepip --upgrade
fi

# Install pipenv if not already installed
if ! command -v pipenv &> /dev/null
then
    echo "pipenv could not be found. Installing pipenv..."
    python3 -m pip install --user pipenv
    export PATH="$HOME/.local/bin:$PATH"  # Add local bin to PATH
fi

# Install dependencies with pipenv
pipenv install

# Copy .env.example to .env
cp example.env .env

echo "Setup complete. Please edit the .env file with your MongoDB credentials."
