#!/bin/bash


# Set script to run on startup
echo "Adding bus-tracker.sh to run on startup"
echo "" >> ~/.bashrc
echo "# Run bus tracker display script on boot:" >> ~/.bashrc
echo "~/bus-tracker/bus-tracker/bus-tracker.sh &" >> ~/.bashrc
source ~/.bashrc

# Initialize git submodule
echo "Initializing git submodule"
cd ~/bus-tracker/bus-tracker
git submodule init
git submodule update --init --recursive

# Install Python Bindings
echo "Building Python Bindings"
cd ~/bus-tracker/bus-tracker/matrix
sudo apt-get update && sudo apt-get install python3-dev python3-pillow -y
make build-python PYTHON=$(command -v python3)
sudo make install-python PYTHON=$(command -v python3)

# Move python scripts to run directory
echo "Moving scripts to matrix/bindings/python/samples"
cd ~/bus-tracker/bus-tracker
cp bustracker.py display.py matrix/bindings/python/samples

