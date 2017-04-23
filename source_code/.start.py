#!/usr/bin/python

# John Filipowicz
# Radford University

# Purpose: Prep for and launch all necessary processes.

import os
from subprocess import call

csv_path = "/media/pi/Feeder_Data/DHT_data.csv"

# Verifying or creating the csv file
if not os.path.isfile(csv_path):
	call(["touch", csv_path])
	datum = open(csv_path, "a")
	datum.write("Temperature,Humidity,TimeStamp")
	datum.close()

# Launching the processes
#call(["python", "periodic.py", "&", "python", "listener.py"]) # Add Dr Ray's program
