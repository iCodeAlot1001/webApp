#!/bin/bash
echo "BUILD START"

python3.12 -m ensurepip --upgrade
python3.12 -m pip install --upgrade pip setuptools wheel

python3.12 -m pip install -r requirements.txt
python3.12 manage.py collectstatic --noinput --clear
echo "BUILD END"