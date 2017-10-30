#!/bin/bash -l
date
cd /usr/www
python manage.py makemigrations
python manage.py migrate
ps -ef|grep uwsgi|grep -v grep|cut -c 9-15|xargs kill -s 9
nohup uwsgi --ini /usr/www/uwsgi.ini > /dev/null 2>&1 &
lsof -i :8001
python manage.py collectstatic
yes
nginx -s stop
nginx
python mail.py
