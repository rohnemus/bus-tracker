#!/bin/bash

echo "Starting bus tracker"

cd ~/bus-tracker/bus-tracker/matrix/bindings/python/samples
sudo python display.py --led-gpio-mapping=adafruit-hat --led-cols=64 --led-rows=32 
