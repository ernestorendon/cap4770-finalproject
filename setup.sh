# setup.sh
#!/bin/bash

# Install pipenv if not already installed
if ! command -v pipenv &> /dev/null
then
    echo "pipenv could not be found. Installing pipenv..."
    pip install pipenv
fi

# Install dependencies with pipenv
pipenv install

# Copy .env.example to .env
cp example.env .env

echo "Setup complete. Please edit the .env file with your MongoDB credentials."
