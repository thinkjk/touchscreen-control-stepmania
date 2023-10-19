import pygame
import sys
import subprocess
import pyautogui

# Initialize pygame
pygame.init()

# Constants for screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 480

# Define button images
BUTTON_IMAGES = {
    "up": {
        "normal": pygame.image.load("images/Up_Arrow_Default_Scaled.png"),
        "pressed": pygame.image.load("images/Up_Arrow_Pressed_Scaled.png"),
    },
    "down": {
        "normal": pygame.image.load("images/Down_Arrow_Default_Scaled.png"),
        "pressed": pygame.image.load("images/Down_Arrow_Pressed_Scaled.png"),
    },
    "left": {
        "normal": pygame.image.load("images/Left_Arrow_Default_Scaled.png"),
        "pressed": pygame.image.load("images/Left_Arrow_Pressed_Scaled.png"),
    },
    "right": {
        "normal": pygame.image.load("images/Right_Arrow_Default_Scaled.png"),
        "pressed": pygame.image.load("images/Right_Arrow_Pressed_Scaled.png"),
    },
    "button1": {
        "normal": pygame.image.load("images/Start_Button_Default_Scaled.png"),
        "pressed": pygame.image.load("images/Start_Button_Pressed_Scaled.png"),
    },
    "button2": {
        "normal": pygame.image.load("images/Escape_Button_Default_Scaled.png"),
        "pressed": pygame.image.load("images/Escape_Button_Pressed_Scaled.png"),
    },
    # Add more buttons and images as needed
}


# Define button positions (X, Y coordinates) for 800x480 resolution
BUTTON_POSITIONS = {
    "up": (320, 50),
    "down": (320, 288),
    "left": (100, 160), 
    "right": (560, 160),  
    "button1": (20, 372),
    "button2": (620, 372),
}

# Create a dictionary to keep track of button states (pressed or not)
button_states = {button: False for button in BUTTON_IMAGES}

# Define the mapping between touchscreen buttons and keyboard keys
BUTTON_KEY_MAPPING = {
    "up": "up",
    "down": "down",
    "left": "left",
    "right": "right",
    "button1": "space",  # Map button1 to the spacebar
    "button2": "enter",  # Map button2 to the Enter key
    # Add more mappings as needed
}

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_width(), screen.get_height()
pygame.display.set_caption("Touchscreen Control Box")

# Define the background color (white in this case)
BACKGROUND_COLOR = (40, 40, 40)

def draw_buttons():
    screen.fill(BACKGROUND_COLOR)

    for button, images in BUTTON_IMAGES.items():
        button_x, button_y = BUTTON_POSITIONS[button]
        if button_states[button]:
            screen.blit(images["pressed"], (button_x, button_y))
        else:
            screen.blit(images["normal"], (button_x, button_y))

# Function to send key presses and releases
def send_key(key, is_pressed):
    if is_pressed:
        pyautogui.keyDown(key)
    else:
        pyautogui.keyUp(key)

# Function to bring the main application window into focus
def focus_main_app():
    try:
        subprocess.Popen(["wmctrl", "-a", "Simply Love"])
    except Exception as e:
        print(f"Failed to focus main app: {e}")

def send_key(key, is_pressed):
    focus_main_app()
    if is_pressed:
        print(f"Pressing key: {key}")
        pyautogui.keyDown(key)
    else:
        print(f"Releasing key: {key}")
        pyautogui.keyUp(key)

pyautogui.PAUSE = 0.05  # Set to a small value, 0.05 seconds

def main():
    # Create a dictionary to keep track of touch states for each button
    touch_states = {button: False for button in BUTTON_IMAGES}

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.FINGERDOWN:
                touch_x, touch_y = event.x * SCREEN_WIDTH, event.y * SCREEN_HEIGHT
                for button, (button_x, button_y) in BUTTON_POSITIONS.items():
                    images = BUTTON_IMAGES[button]
                    button_rect = pygame.Rect(button_x, button_y, images["normal"].get_width(), images["normal"].get_height())
                    if button_rect.collidepoint(touch_x, touch_y):
                        # Set touch state for the button
                        touch_states[button] = True
                        # Translate button press to key press and send it
                        key = BUTTON_KEY_MAPPING.get(button)
                        if key is not None:
                            send_key(key, True)
                        # Bring the main application window into focus
                        focus_main_app()
            elif event.type == pygame.FINGERUP:
                # Handle button release events here, not immediately after a press event
                for button in BUTTON_IMAGES:
                    if touch_states[button]:
                        # Translate button release to key release and send it
                        key = BUTTON_KEY_MAPPING.get(button)
                        if key is not None:
                            send_key(key, False)
                        touch_states[button] = False

        # Update button states based on touch states
        for button in BUTTON_IMAGES:
            button_states[button] = touch_states[button]

        draw_buttons()
        pygame.display.update()

if __name__ == "__main__":
    main()
