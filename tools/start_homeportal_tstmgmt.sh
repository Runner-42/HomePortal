#!/bin/bash

exec > >(tee -a "/var/log/homeportal/HomePortal.log") 2>&1
date

echo "Starting Home Portal Management processes"

source /home/homeportal/venv/bin/activate

echo "Starting gunicorn process"
cd /home/homeportal
gunicorn --workers 1 --bind 127.0.0.1:8000 manage &

deactivate