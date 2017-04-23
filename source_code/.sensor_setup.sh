#!/bin/bash

# John Filipowicz
# Radford University

# Purpose: Run setup for proximity and dht sensors.
# Note: This must be run before the software's first use on a Pi.

mkdir -p ~/Feeder/sensor_libraries/DHT
mkdir -p ~/Feeder/sensor_libraries/Proximity

git clone http://github.com/adafruit/Adafruit_Python_DHT ~/Feeder/sensor_libraries/DHT/
git clone http://github.com/adafruit/Adafruit_Python_VCNL40xx ~/Feeder/sensor_libraries/DHT/

sudo python ~/Feeder/sensor_libraries/DHT/setup.py install
sudo python ~/Feeder/sensor_libraries/Proximity/setup.py install
