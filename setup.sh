#!/bin/bash

# Create Config File
echo ""
echo "Creating config file"
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

# Set script to run on startup
echo ""
echo "Creating service to run bus-tracker.sh on startup"
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

# Initialize git submodule
echo ""
echo "Initializing git submodule"
cd ~/bus-tracker/bus-tracker
git submodule init
git submodule update --init --recursive

# Install Python Bindings
echo ""
echo "Building Python Bindings"
cd ~/bus-tracker/bus-tracker/matrix
sudo apt-get update && sudo apt-get install python3-dev python3-pillow -y
make build-python PYTHON=$(command -v python3)
sudo make install-python PYTHON=$(command -v python3)

# Move python scripts to run directory
echo ""
echo "Moving scripts to matrix/bindings/python/samples"
cd ~/bus-tracker/bus-tracker
cp bustracker.py display.py matrix/bindings/python/samples
cp bus-tracker.sh /usr/local/bin

# Enable systemd service and start it
echo ""
echo "Enabling systemd"
sudo systemctl daemon-reload
sudo systemctl enable bus_tracker.service 
sudo systemctl start bus_tracker.service 
sudo systemctl status bus_tracker.service
