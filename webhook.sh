#!/bin/bash -l
date
cd /usr/www
rm uwsgi.log
git fetch --all
git reset --hard origin/master
git pull
python manage.py makemigrations
python manage.py migrate
ps -ef|grep uwsgi|grep -v grep|cut -c 9-15|xargs kill -s 9
nohup uwsgi --ini /usr/www/uwsgi.ini > uwsgi.log 2>&1 &
lsof -i :8001
