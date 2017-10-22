#!/bin/bash -l
cd /usr/www
git fetch --all
git reset --hard origin/master
git pull
