#!/bin/bash

# John Filipowicz
# Radford University

# Purpose: Capture images from webcam and make them into a video

# Loop control variable, do not change
i=0

location=/media/pi/FEEDER_DATA
mkdir -p $location/images
rm $location/images/*.jpeg

while [ $i -lt 10 ]
do
	streamer -f jpeg -r 640x480 -o $location/images/image$i.jpeg
	let i=i+1
done

mogrify -resize 800x800 $location/images/*.jpeg
convert $location/*.jpeg -delete 10 -morph 10 $location/images/%05d.jpg
avconv -r 25 -i $location/images.%05d.jpeg -qscale 2 $location/test.mp4
