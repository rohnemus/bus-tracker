# bus-tracker

Use this to pull from the muni api and display with a pixel display!

Users will need to make an account and request an api key [here.](https://511.org/open-data/token)
  
# Setup
## Hardware
### List of OTS hardware used:
 - rpi 3b running standard rasbian os
 - [Waveshare P4 64x32 pixel display](https://www.waveshare.com/RGB-Matrix-P4-64x32.htm)
 - [Adafruit pixel display hat](https://www.adafruit.com/product/2345)
 - usb wifi dongle
 - 5v 4A 2.1mm power supply
 - 12in HUB75 ribbon cable
 
 ### Custom enclosure:
 STL files can be found here in /print files
 Links to onshape documents can be found here
 
 ### Assembly
Much of this project is based off of hzeller's [rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix) library consult documentation here for more help with wiring

## Software
### Clone repository
```
cd ~
mkdir bus-tracker
cd bus-tracker
git clone https://github.com/rohnemus/bus-tracker.git
```

Once this project is cloned the rest can be done automatically using [setup.sh](https://github.com/rohnemus/bus-tracker/blob/main/setup.sh) or manually:
### Automatic
```
cd bus-tracker
chmod u+x setup.sh
./setup.sh
```

### Manual
#### Create config file
```
cd bus-tracker
cat > config.ini << EOF
[credentials]
api=PASTE_API_KEY_HERE

[bus selection]
stops=14159,14158
direction=IB

[display]
show_direction=False
screen_width=11
EOF
```
#### Create sytemd service
```
cat > bus_tracker.service << EOF
[Unit]
Description=Display bus times
After=network.target

[Service]
ExecStart=/bin/bash ${HOME}/bus-tracker/bus-tracker/bus-tracker.sh
Restart=on-failure
RestartSec=10s
Type=forking
User=${USER}
WorkingDirectory=${HOME}/bus-tracker/bus-tracker

[Install]
WantedBy=multi-user.target
EOF
sudo mv bus_tracker.service /etc/systemd/system
```

#### LED Matrix Library
The [rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix) library is included as submodule. Use the following commands to initialize:

```
git submodule init
git submodule update --init --recursive
```

Run the following commands in the /matrix directory to build the python bindings:

```
sudo apt-get update && sudo apt-get install python3-dev python3-pillow -y
make build-python PYTHON=$(command -v python3)
sudo make install-python PYTHON=$(command -v python3)
```

#### Move python script to sample directory
```
cp bustracker.py display.py matrix/bindings/python/samples
```

#### Test everything is working

```
cd /bindings/python/samples
sudo ./runtext.py --led-gpio-mapping=adafruit-hat --led-cols=64 --led-rows=32
```

#### Enable systemd service and start it
```
sudo systemctl daemon-reload
sudo systemctl enable bus_tracker.service 
sudo systemctl start bus_tracker.service 
sudo systemctl status bus_tracker.service
```

### Done
Reboot and the bus tracker should display on boot!
