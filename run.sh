#/bin/bash

source ./petpal/venv/bin/activate
python3 ./petpal/manage.py makemigrations
python3 ./petpal/manage.py migrate
python3 ./petpal/manage.py runserver
