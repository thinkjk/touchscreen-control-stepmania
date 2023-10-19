import pygame
import sys
import pyautogui

# Initialize the pygame library
pygame.init()

# Constants
# Screen dimensions for the game
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 480
# Background color for the game window
BACKGROUND_COLOR = (40, 40, 40)

# Dictionary to hold button images
# Each button has two states: default and pressed
BUTTON_IMAGES = {
    name: {
        state: pygame.image.load(f"images/{name.capitalize()}_Arrow_{state.capitalize()}_Scaled.png")
        for state in ["default", "pressed"]
    }
    for name in ["up", "down", "left", "right", "start", "escape"]
}

# Dictionary to define positions for each button on the screen
BUTTON_POSITIONS = {
    "up": (320, 50),
    "down": (320, 288),
    "left": (100, 160),
    "right": (560, 160),
    "start": (20, 372),
    "escape": (620, 372),
}

# Mapping touchscreen buttons to their respective keyboard keys
BUTTON_KEY_MAPPING = {
    "up": "up",
    "down": "down",
    "left": "left",
    "right": "right",
    "start": "enter",
    "escape": "escape",
}

# Setting up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Touchscreen Control Box")


#Draws the buttons on the screen
def draw_buttons(button_states):
    screen.fill(BACKGROUND_COLOR)
    for button, images in BUTTON_IMAGES.items():
        button_x, button_y = BUTTON_POSITIONS[button]
        image = images["pressed"] if button_states[button] else images["default"]
        screen.blit(image, (button_x, button_y))

#Simulate a key press or release.
def send_key(key, is_pressed):
    action = pyautogui.keyDown if is_pressed else pyautogui.keyUp
    action(key)
    
#Handle touch events (press and release)
def handle_touch_event(event, touch_states):
    touch_x, touch_y = event.x * SCREEN_WIDTH, event.y * SCREEN_HEIGHT

    for button, (button_x, button_y) in BUTTON_POSITIONS.items():
        images = BUTTON_IMAGES[button]
        button_rect = pygame.Rect(button_x, button_y, images["default"].get_width(), images["default"].get_height())

        if button_rect.collidepoint(touch_x, touch_y):
            touch_states[button] = event.type == pygame.FINGERDOWN

            key = BUTTON_KEY_MAPPING.get(button)
            if key:
                send_key(key, touch_states[button])

def main():
    touch_states = {button: False for button in BUTTON_IMAGES}
    pyautogui.PAUSE = 0.05

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type in [pygame.FINGERDOWN, pygame.FINGERUP]:
                handle_touch_event(event, touch_states)

        draw_buttons(touch_states)
        pygame.display.update()

if __name__ == "__main__":
    main()