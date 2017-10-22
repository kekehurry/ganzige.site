#!/bin/bash -l
cd /usr/www
git fetch --all
git reset origin/master
git pull
