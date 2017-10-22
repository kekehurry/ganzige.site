#!/bin/bash -l
cd /usr/www
git fetch --all
git reset --hard origin/master
git pull
$ps -ef|grep uwsgi|grep -v grep|cut -c 9-15|xargs kill -s 9
nohup uwsgi --ini /usr/www/uwsgi.ini
