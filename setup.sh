#!/bin/bash


# Set script to run on startup
echo ""
echo "Creating service to run bus-tracker.sh on startup"
sudo cat > ~/etc/systemd/system/bus_tracker.service << EOF
[Unit]
Description=Display bus times
After=network.target

[Service]
ExecStart=~/bus-tracker/bus-tracker/bus-tracker.sh
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF

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

# Enable systemd service and start it
echo ""
echo "Enabling systemd"
sudo systemctl daemon-reload
sudo systemctl enable shellscript.service 
sudo systemctl start shellscript.service 

