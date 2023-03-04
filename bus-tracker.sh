#!/bin/bash

echo "Starting bus tracker"

cd matrix/bindings/python/samples
sudo ./runtext.py --led-gpio-mapping=adafruit-hat --led-cols=64 --led-rows=32 &

echo "Script Done"