#!/bin/bash -l
cd /usr/www
git fetch --all
gti reset origin/master
git pull
