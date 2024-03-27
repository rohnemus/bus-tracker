#!/bin/bash

echo $(date -u) "Starting bus tracker" >> ~/bus-tracker/bus-tracker/log.txt

cd ~/bus-tracker/bus-tracker/matrix/bindings/python/samples
sudo python display.py --led-gpio-mapping=adafruit-hat --led-cols=64 --led-rows=32 >/dev/null
echo $(date -u) "Stopping bus tracker" >> ~/bus-tracker/bus-tracker/log.txt