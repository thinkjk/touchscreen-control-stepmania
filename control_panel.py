import pygame
import sys
import pyautogui
import os
from evdev import InputDevice, ecodes, list_devices
from select import select

# Get the directory where the script is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define images for each button state.
BUTTON_IMAGES = {
    name: {
        state: pygame.image.load(os.path.join(BASE_DIR, f"images/{name.capitalize()}_Arrow_{state.capitalize()}_Scaled.png"))
        for state in ["default", "pressed"]
    }
    for name in ["up", "down", "left", "right", "start", "escape"]
}



# Define positions for buttons on the screen.
BUTTON_POSITIONS = {
    "up": (320, 50),
    "down": (320, 288),
    "left": (100, 160),
    "right": (560, 160),
    "start": (20, 372),
    "escape": (620, 372),
}

# Key mappings for each monitor.
BUTTON_KEY_MAPPING_1 = {
    "up": "up",
    "down": "down",
    "left": "left",
    "right": "right",
    "start": "enter",
    "escape": "escape",
}
BUTTON_KEY_MAPPING_2 = {
    "up": "w",
    "down": "s",
    "left": "a",
    "right": "d",
    "start": "f",
    "escape": "g",
}

def get_device_path_by_phys(phys_address):
    """Return the device path for the given physical address, or None if not found."""
    devices = [InputDevice(path) for path in list_devices()]
    for device in devices:
        if device.phys == phys_address:
            return device.path
    return None

# Dynamically get the device paths using the physical addresses
DEVICE_MAPPING = {
    '1': get_device_path_by_phys("usb-0000:00:14.0-2/input0"),  # First touchscreen
    '2': get_device_path_by_phys("usb-0000:00:14.0-4/input0"),  # Second touchscreen
}

POSITION_MAPPING = {
    '1': "0,0",
    '2': "800,0",
}

pygame.display.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 480

def draw_buttons(screen, touch_states):
    """Draw the button images based on their current state."""
    screen.fill((40, 40, 40))
    for button, position in BUTTON_POSITIONS.items():
        state = "pressed" if touch_states.get(button) else "default"
        screen.blit(BUTTON_IMAGES[button][state], position)
    pygame.display.flip()

def send_key(key, is_pressed):
    """Simulate a key press or release."""
    (pyautogui.keyDown if is_pressed else pyautogui.keyUp)(key)

def handle_touch_event(event, touch_states, button_key_mapping):
    """Handle touch events and update button states."""
    global last_touch_x, last_touch_y

    if event.type == ecodes.EV_ABS:
        if event.code == ecodes.ABS_MT_POSITION_X:
            last_touch_x = event.value
        elif event.code == ecodes.ABS_MT_POSITION_Y:
            last_touch_y = event.value
    elif event.type == ecodes.EV_KEY and event.code == ecodes.BTN_TOUCH and last_touch_x and last_touch_y:
        for button, position in BUTTON_POSITIONS.items():
            image = BUTTON_IMAGES[button]["default"]
            if pygame.Rect(position[0], position[1], image.get_width(), image.get_height()).collidepoint(last_touch_x, last_touch_y):
                touch_states[button] = event.value == 1
                send_key(button_key_mapping.get(button), touch_states[button])

def run_for_device(device_path, monitor_number, button_key_mapping):
    """Main function to handle input and display for each monitor."""
    os.environ['SDL_VIDEO_WINDOW_POS'] = POSITION_MAPPING[monitor_number]
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN | pygame.NOFRAME)
    touch_states = {button: False for button in BUTTON_IMAGES.keys()}
    
    # Draw the buttons immediately after setting up the screen
    draw_buttons(screen, touch_states)
    
    pyautogui.PAUSE = 0.05

    device = InputDevice(device_path)
    
    while True:
        # Poll and clear the Pygame event queue
        for _ in pygame.event.get():
            pass

        # Add a timeout to the select function (e.g., 0.1 seconds)
        r, _, _ = select([device], [], [], 0.1)
        if r:
            for event in r[0].read():
                if event.type in (ecodes.EV_ABS, ecodes.EV_KEY):
                    handle_touch_event(event, touch_states, button_key_mapping)
            draw_buttons(screen, touch_states)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Please provide a monitor number as an argument (1 or 2).")
    monitor_arg = sys.argv[1]
    if monitor_arg not in ["1", "2"]:
        sys.exit("Invalid monitor number. Choose 1 or 2.")
        
    key_mapping = BUTTON_KEY_MAPPING_1 if monitor_arg == "1" else BUTTON_KEY_MAPPING_2
    run_for_device(DEVICE_MAPPING[monitor_arg], monitor_arg, key_mapping)
