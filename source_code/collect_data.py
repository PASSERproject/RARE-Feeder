#!/usr/bin/python
# John Filipowicz
# Radford University
 
# This file is to collect the current reading from the DHT11 temp/humidity
# sensor to the designated .csv file

import sys
sys.path.insert(0, '~/Documents/feederSoftware/sensor_libraries/DHT_Python_Library/Adafruit_Python_DHT')
import Adafruit_DHT
import datetime


def collect():

	# GPIO pin connected to data pin verify correctness.
	pin = 17

	# Reading the sensor. If using the DHT22, change the 11 to 22
	humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin)

	# Un-comment the below line to use F instead of C
	# temperature = temperature * 9/5.0 + 32

	# Change the name of the file by changing the string literal "x.csv"
	# Don't do this. The filename is hard coded right now
	filename = "/media/pi/Feeder_Data/DHT_data.csv"
	datum = open(filename, "a")

	# Writing the sensor data to file
	datum.write("\n" + str(temperature) + ",")
	datum.write(str(humidity) + ",")
	datum.write(str(datetime.datetime.now()))
	datum.close()
