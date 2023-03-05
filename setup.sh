#!/bin/bash


# Set script to run on startup
echo "" >> ~/.bashrc
echo "# Run bus tracker display script on boot:" >> ~/.bashrc
echo "~/bus-tracker/bus-tracker/bus-tracker.sh &" >> ~/.bashrc
source ~/.bashrc

# Initialize git submodule
cd ~/bus-tracker/bus-tracker
git submodule init
git submodule update --init --recursive

# Install Python Bindings
cd matrix
sudo apt-get update && sudo apt-get install python3-dev python3-pillow -y
make build-python PYTHON=$(command -v python3)
sudo make install-python PYTHON=$(command -v python3)

# Move python script to sample directory
cp bustracker.py display.py matrix/bindings/python/samples

