#!/bin/bash

# UPDATE APT
sudo apt update

# PYTHON
if ! command -v python3 &> /dev/null/; then
  echo "Installing python..."
  sudo apt install python3.10
  sudo apt install python3-venv
fi

# PIP
if ! command -v pip3 &> /dev/null; then
    echo "Installing pip..."
    sudo apt install python3-pip
fi

# VENV
echo "Creating virtual environment..."
python3 -m venv ./petpal/venv
source ./petpal/venv/bin/activate

# INSTALL REQ PACKAGES
echo "Installing required packages..."
pip install django djangorestframework Pillow djangorestframework-simplejwt

# MIGRATE
echo "Running Django management commands..."
python3 ./petpal/manage.py makemigrations
python3 ./petpal/manage.py migrate

echo "Completed."
