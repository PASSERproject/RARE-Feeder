#!/bin/bash

# John Filipowicz
# Radford University

# Purpose: This script is meant to download/install all packages needed for the feeder to operate

# Packages will be installed by sections



# Update System
apt-get update

# Sensors
apt-get install build-essential python-dev

# Webcam
apt-get install imagemagick libav libav-tools libav-doc

# Genetic Algorithm
apt-get install libapache2-mod-php5 php5 php-pear apache2 apache2-utils
php5-xcache php5-mysql php5-curl php5-gd

