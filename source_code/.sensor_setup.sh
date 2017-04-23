#!/bin/bash

# John Filipowicz
# Radford University

# Purpose: Run setup for proximity and dht sensors.
# Note: This must be run before the software's first use on a Pi.

sudo python ~/Feeder/sensorlibraries/DHT/setup.py install
sudo python ~/Feeder/sensorlibraries/Proximity/setup.py install
