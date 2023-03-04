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
This library is included as submodule. Use the following commands to initialize:

```
git submodule init
git submodule update --init --recursive
```

Once the submodule is initialized update the hardware config in the makefile:

`nano matrix/lib/Makefile`

    Line 37: `HARDWARE_DESC?=adafruit-hat` 


Run the following commands in the /matrix directory to build the python bindings:

```
sudo apt-get update && sudo apt-get install python3-dev python3-pillow -y
make build-python PYTHON=$(command -v python3)
sudo make install-python PYTHON=$(command -v python3)
```

Test everything is working:

```
cd /bindings/python/samples
sudo ./runtext.py --led-cols=64 --led-rows=32
```
