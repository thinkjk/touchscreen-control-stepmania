
Touchscreen Control for StepMania
=================================

This application provides a touchscreen interface to control the StepMania game. It enables users to play the game using touchscreen devices as inputs.

![Touchscreen Control for StepMania Demo](https://chat.openai.com/c/demo-image-placeholder.png)

Features
--------

-   Dynamically determines touchscreen device paths based on physical IDs.
-   Displays graphical buttons for game controls.
-   Supports dual monitor setups.
-   Simulates key presses in response to touchscreen events.

Prerequisites
-------------

-   Python 3
-   `pygame` library
-   `pyautogui` library
-   `evdev` library

Installation
------------

1.  Clone this repository:

    bash

-   `git clone <repository_url>`

    -   Navigate to the cloned directory and install the required Python libraries:

1.  `pip install pygame pyautogui evdev`

Usage
-----

### Startup Script

1.  Before starting the game, you can use the provided startup script. This script ensures the proper order of operations and logs debug information to `/tmp/startup_log.txt`.

    To use the startup script:

    bash

1.  `chmod +x path_to_startup_script.sh
    ./path_to_startup_script.sh`

### Touchscreen Control Panel

To run the touchscreen control panel for a specific monitor, execute:

bash

`python3 multi_control_panel.py <monitor_number>`

Replace `<monitor_number>` with either `1` or `2` depending on the monitor you want to use.

How It Works
------------

-   The program uses the `evdev` library to determine the device paths of the touchscreens based on their physical IDs.
-   `pygame` is used to display the game controls (buttons) on the touchscreen.
-   When a button is pressed on the touchscreen, the corresponding key press is simulated using `pyautogui`.

File Structure
--------------

-   **Monitor Physical ID Finder**:
    -   Retrieves and displays information about connected input devices.
-   **Startup Script**:
    -   Launches the StepMania game and initializes the touchscreen control panels for both monitors.
-   **Game Code**:
    -   Provides the main functionality of displaying the touchscreen interface and handling touch events.

Contributing
------------

Contributions are welcome! Please open an issue or submit a pull request if you have improvements or fixes.

License
-------

This project is open source, licensed under the [MIT License](https://chat.openai.com/c/LICENSE).



<!-- CONTACT -->
## Contact

Jason Kramer - [Website](thinkjk.com) - jkramer@thinkjk.com

Project Link: [https://github.com/github_username/repo_name](https://github.com/github_username/repo_name)



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* All images made by [ESB Studio](https://www.instagram.com/esbstudios/)
* Models made/modified by [Wei Chen](???)



<!-- #!/bin/bash

# Log file for debugging
LOG_FILE="/tmp/startup_log.txt"

# Update the package list and install necessary dependencies
sudo apt-get update
sudo apt-get install -y python3-pip libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev python3-numpy subversion libportmidi-dev ffmpeg libswscale-dev libavformat-dev libavcodec-dev x11-xserver-utils evtest

# Install Python packages
pip3 install pygame pyautogui evdev

# Add the current user to the input group to grant permissions to access input devices
sudo usermod -a -G input $USER

# Notify user to log out and log back in for group changes to take effect
echo "Please log out and log back in to apply group changes."

#disable xhost access control
xhost +

# Start itgmania
/opt/itgmania/itgmania &

# Wait for 5 seconds for correct order of operations
sleep 5

# Start the first monitor Python script 
python3 /home/jason/touchscreen-control-stepmania/multi_control_panel.py 1 >> $LOG_FILE 2>&1 &

# Start the second monitor Python script
python3 /home/jason/touchscreen-control-stepmania/multi_control_panel.py 2 >> $LOG_FILE 2>&1 & -->
