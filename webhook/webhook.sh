#!/bin/bash -l
cd /usr/www
git pull origin master　
python /usr/www/manage.py migrate
