#!/bin/bash -l
cd /usr/www
git fetch --all
git reset --hard origin/master
git pull
pid=`lsof -i:8000| awk 'NR==2{print $2}'`　
