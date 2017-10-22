#!/bin/bash -l
cd /usr/www
git fetch --all
git reset --hard origin/master
git pull
pid=`lsof -i:8001| awk 'NR==2{print $2}'`　
kill -9 `eval $pid`　
nohup uwsgi --ini /usr/www/uwsgi.ini
