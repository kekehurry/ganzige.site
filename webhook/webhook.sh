#!/bin/bash -l
sudo cd /usr/www
sudo git fetch --all
sudo gti reset origin/master
sudo git pull
