# bus-tracker

Use this to pull from the muni api and display with a pixel display

Users will need to make an account and request an api key here: TODO

# Hardware
## List of OTS hardware used:
 - rpi 3b
 - [Waveshare 64x32 pixel display](https://www.waveshare.com/product/rgb-matrix-p2.5-64x32.htm)
 - [Adafruit pixel display hat](https://www.adafruit.com/product/2345)
 - usb wifi dongle
 - 5v 4A 2.1mm power supply
 - 12in HUB75 ribbon cable
 
 ## Custom enclosure:
 STL files can be found here in /print files
 Links to onshape documents can be found here
 
 
# Installation

## Virtual Env
https://raspberrypi-guide.github.io/programming/create-python-virtual-environment

`pip3 install virtualenv virtualenvwrapper`
`nano ~/.bashrc`

Append:
```
#Virtualenvwrapper settings:
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_VIRTUALENV=~/.local/bin/virtualenv
source ~/.local/bin/virtualenvwrapper.sh
export VIRTUALENVWRAPPER_ENV_BIN_DIR=bin
```

`source ~/.bashrc1

## Requirements
### LED Matrix Library
https://github.comlhzeller/rpi-rgb-led-matrix

