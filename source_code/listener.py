#!/usr/bin/python

# John Filipowicz
# Radford University

# The purpose of this file is to 'listen' for either a sizable pressure reading
#    or for a proximity sensor hit that is close enough. Once one is found, the
#    appropriate code is executed and the program shall loop.

import time
import RPi.GPIO as GPIO
import sys
from subprocess import call

sys.path.insert(0, '~/Documents/feederSoftware/sensor_libraries/Proximity_Python_Library/Adafruit_Python_VCNL40xx')
import Adafruit_VCNL40xx


# Pin to read. Verify correctness
pin = 21

# Threshold for Proximity sensor
threshold = 2700

# Time to sleep between hits in seconds
sleep_hit = 5

# Time to sleep between misses in seconds
sleep_miss = 5


# BCM means we are using GPIO numbering instead of pin numbering.
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

# Creating Proximity sensor instance
vcnl = Adafruit_VCNL40xx.VCNL410()


while True:
	print('Pressure={0}  ,  Proximity={1}'.format(GPIO.input(pin), vcnl.read_proximity()))
	if (GPIO.input(pin) or (vcnl.read_proximity() > threshold)):
		#print('Triggered by sensor')
		self.capture()
		time.sleep(sleep_hit);
	else:
		#print('below threshold')
		time.sleep(sleep_miss);

def capture():
	# Output location
	path = "/media/pi/Feeder_Data/"

	# File Name
	output = time.strftime("%m%d%Y-%H%M%S") + ".avi"

	# Frames Per Second
	fps = 25

	# Video Duration
	time = "0:0:10"

	call(["streamer", "-q", "-r", fps, "-f", "rgb24", "-t", time, "-o", path + output])


















