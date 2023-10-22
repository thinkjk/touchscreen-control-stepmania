
Touchscreen Control for StepMania
=================================

This application provides a touchscreen interface to control the StepMania game. It enables users to play the game using touchscreen devices as inputs.

![Touchscreen Control for StepMania Demo](some_image.png)

Features
--------

-   Dynamically determines touchscreen device paths based on physical IDs.
-   Displays graphical buttons for game controls.
-   Supports dual monitor setups.
-   Simulates key presses in response to touchscreen events.


Notes
-------------
Currently running with two of these monitors: https://www.amazon.com/ELECROW-Raspberry-Touchscreen-Monitor-HDMI-Compatible/dp/B07FDYXPT7/

On an Intel NUC running Ubuntu 22.04 LTS

Prerequisites
-------------

-   Python 3
-   pip
-   `pygame` library
-   `pyautogui` library
-   `evdev` library

Installation
------------

1.  Clone this repository:

```bash
git clone https://github.com/thinkjk/touchscreen-control-stepmania.git
``````
2. Install pip
```bash
sudo apt install python3-pip
```
3.   Navigate to the cloned directory and install the required Python libraries:
```bash
pip3 install pygame pyautogui evdev
```
4. For the application to access input devices, you need to grant the necessary permissions. This can be achieved by adding the current user to the `input` group. Note: After executing the command, you may need to log out and log back in for the changes to take effect.

Execute the following command:

```bash
sudo usermod -a -G input $USER
```

Usage
-----

#### Finding the Physical ID of the Touchscreen Monitor

To determine the physical ID of your touchscreen monitor, you'll need to use the `evdev_monitor_list` script provided in this repository.

Run the script:

```bash
python3 evdev_monitor_list.py
```
The script will list all connected input devices, along with their paths, names, and physical IDs. Look for your touchscreen device in the list and note down its physical ID. This ID will be used to dynamically determine the device paths for touchscreens in the main application.

Note: Ensure you have the necessary permissions to access the input devices. If you encounter permission issues, refer to the "Granting Permissions for Input Devices" section in this README.
### Startup Script

1.  Before starting the game, you can use the provided startup script. This script ensures the proper order of operations and logs debug information to `/tmp/startup_log.txt`.

    To use the startup script:

```bash
chmod +x path_to_startup_script.sh
``````
### Touchscreen Control Panel

To run the touchscreen control panel for a specific monitor, execute:

```bash
python3 control_panel.py <monitor_number>
``````
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

Distributed under the MIT License. See `LICENSE.txt` for more information.


<!-- CONTACT -->
## Contact

Jason Kramer - [Website](thinkjk.com) - jkramer@thinkjk.com

Project Link: [https://github.com/thinkjk/touchscreen-control-stepmaniae](https://github.com/thinkjk/touchscreen-control-stepmania)



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* All images made by [ESB Studio](https://www.instagram.com/esbstudios/)
* Model modified by Wei Chen Lin
