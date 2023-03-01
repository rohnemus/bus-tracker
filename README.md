# bus-tracker

Use this to pull from the muni api and display with a pixel display

Users will need to make an account and request an api key here: TODO

# Hardware
List of hardware used:
 - rpi 3b
 - waveshare 64x32 pixel display
 - adafruit pixel display hat
 
 mounting cad
 
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

