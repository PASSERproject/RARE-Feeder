#!/usr/bin/bash

# John Filipowicz
# Radford University

# Purpose: Prep for and launch all necessary processes.

CSV=/media/pi/Feeder_Data/DHT_data.csv

if [! -f "$CSV"] then
	echo "Temperature,Humidity,TimeStamp" >> "$CSV"
fi

./periodic.py &
./listener.py &
#Dr. Ray's Program too















