#!/bin/bash

# Log file for debugging
LOG_FILE="/tmp/startup_log.txt"

# Disable xhost access control
xhost +

# Start itgmania
/opt/itgmania/itgmania &

# Wait for 10 seconds for correct order of operations
sleep 10

# Start the first monitor Python script 
python3 $HOME/touchscreen-control-stepmania/control_panel.py 1 >> $LOG_FILE 2>&1 &

# Start the second monitor Python script
python3 $HOME/touchscreen-control-stepmania/control_panel.py 2 >> $LOG_FILE 2>&1 &
