#!/bin/bash -l
git pull origin master　
pid=`lsof -i:8000| awk 'NR==2{print $2}'`　
echo "pid:$pid"　
kill -9 $pid　
lsof -i:8001
nohup uwsgi --ini /usr/www/uwsgi.ini
