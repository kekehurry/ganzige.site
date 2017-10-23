#!/bin/bash -l
date
cd /usr/www
python manage.py makemigrations
python manage.py migrate
ps -ef|grep uwsgi|grep -v grep|cut -c 9-15|xargs kill -s 9
nohup uwsgi --ini /usr/www/uwsgi.ini > /dev/null 2>&1 &
python mail.py
