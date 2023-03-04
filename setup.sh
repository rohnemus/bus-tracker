#!/bin/bash


# add to run on startup
sudo echo "bus-tracker.sh" >> /home/pi/.bashrc

# move python script to sample directory
cp bustracker.py display.py matrix/bindings/python/samples

