import pygame
import sys
import random


current_turn = None
ship_animation_done = False
patent_animation_done = False
fade_animation_done = False  
COVID_animation_done = False
reflect_animation_done = False
show_reflect1_done = False
show_reflect2_done= False
show_reflect3_done = False
show_instructions_done = False

dice_roll_counter = 0  # dice roll counter
dice_roll = None

# Initialize Pygame
pygame.init()

# Screen setup
screen_width, screen_height = 600, 700
screen = pygame.display.set_mode((screen_width, screen_height))
# screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (0, 155, 255)
RED = (150, 0, 0)
GREEN = (0, 80, 0)
BLUE = (0, 70, 255)
YELLOW = (200, 120, 0)

TURN_GREEN = (0, 155, 0)
TURN_BLUE = (0, 100, 255)
TURN_YELLOW = (255, 155, 0)
TURN_RED = (200, 0, 0)

# Set up colors
BOX_RED = (255, 204, 204)
BOX_GREEN = (200, 255, 200)
BOX_BLUE = (173, 216, 230)
BOX_YELLOW = (255, 255, 224)


# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)
turn_font = pygame.font.SysFont('gillsans', 30)

# Button dimensions
button_width, button_height = 200, 60
button_x = screen_width // 2 - button_width // 2
button_y = screen_height // 2

# Start button rectangle
start_button_rect = pygame.Rect(button_x, button_y+100, button_width, button_height)

# Load scroll image for instructions
scroll_image = pygame.image.load('images/scroll_image.jpeg')
old_paper = pygame.image.load('images/old_paper.jpeg')
old_paper = pygame.transform.scale(old_paper, (screen_width, screen_height))
scroll_image = pygame.transform.scale(scroll_image, (screen_width, screen_height))

# Load welcome image for instructions
welcome_image = pygame.image.load('images/welcome.png')
welcome_image = pygame.transform.scale(welcome_image, (screen_width, screen_height))

#instructions text
instructions1 = pygame.image.load('images/instructions111.png')
instructions2 = pygame.image.load('images/instructions22.png')
instructions3 = pygame.image.load('images/instructions33.png')

#colonization text
colony1 = pygame.image.load('images/colony1.png')
colony2 = pygame.image.load('images/colony2-2.png')
#patent text
patent1 = pygame.image.load('images/patent11.png')
patent2 = pygame.image.load('images/patent22.png')
#COVID text
covid1 = pygame.image.load('images/covid1.png')
covid2 = pygame.image.load('images/covid2.png')
#reflections text
time1 = pygame.image.load('images/time1.png')
time2 = pygame.image.load('images/time2.png')
time3 = pygame.image.load('images/time3.png')


# Show COVID
def show_COVID():
# Fade in and out scroll image
# def animate_fade_in_out_scroll():
    global COVID_animation_done
    if COVID_animation_done:
        return
    # Fade in
    for alpha in range(0, 255, 5):
        covid1.set_alpha(alpha)
        screen.fill(WHITE)
        screen.blit(covid1, (0, 0))
        pygame.display.flip()
        pygame.time.delay(20)

    # Wait for the player to press a key
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

    # Show second page of covid
    screen.fill(WHITE)
    screen.blit(covid2, (0, 0))  # Display second page image
    pygame.display.flip()

    # Wait for the player to press a key to exit instructions
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

    # Fade out
    for alpha in range(255, 0, -5):
        covid2.set_alpha(alpha)
        screen.fill(WHITE)
        screen.blit(covid2, (0, 0))
        pygame.display.flip()
        pygame.time.delay(20)

    # Clear the screen after instructions
    screen.fill(WHITE)
    pygame.display.flip()
    COVID_animation_done = True

# Show reflection
def show_reflect1():
# Fade in and out scroll image
# def animate_fade_in_out_scroll():
    global show_reflect1_done
    if show_reflect1_done:
        return
    # Fade in
    for alpha in range(0, 255, 5):
        time1.set_alpha(alpha)
        screen.fill(WHITE)
        screen.blit(time1, (0, 0))
        pygame.display.flip()
        pygame.time.delay(20)

    # Wait for the player to press a key
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

    # Fade out
    for alpha in range(255, 0, -5):
        time1.set_alpha(alpha)
        screen.fill(WHITE)
        screen.blit(time1, (0, 0))
        pygame.display.flip()
        pygame.time.delay(20)
   
    # Clear the screen after instructions
    screen.fill(WHITE)
    pygame.display.flip()
    show_reflect1_done = True


# Show reflection
def show_reflect2():
# Fade in and out scroll image
# def animate_fade_in_out_scroll():
    global show_reflect2_done
    if show_reflect2_done:
        return
    # Fade in
    for alpha in range(0, 255, 5):
        time2.set_alpha(alpha)
        screen.fill(WHITE)
        screen.blit(time2, (0, 0))
        pygame.display.flip()
        pygame.time.delay(20)

    # Wait for the player to press a key
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False
    
    # Fade out
    for alpha in range(255, 0, -5):
        time2.set_alpha(alpha)
        screen.fill(WHITE)
        screen.blit(time2, (0, 0))
        pygame.display.flip()
        pygame.time.delay(20) 
   
      
    # Clear the screen after instructions
    screen.fill(WHITE)
    pygame.display.flip()
    show_reflect2_done = True


# Show reflection
def show_reflect3():
# Fade in and out scroll image
# def animate_fade_in_out_scroll():
    global show_reflect3_done
    if show_reflect3_done:
        return
    # Fade in
    for alpha in range(0, 255, 5):
        time3.set_alpha(alpha)
        screen.fill(WHITE)
        screen.blit(time3, (0, 0))
        pygame.display.flip()
        pygame.time.delay(20)

    # Wait for the player to press a key
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

    # Fade out
    for alpha in range(255, 0, -5):
        time3.set_alpha(alpha)
        screen.fill(WHITE)
        screen.blit(time3, (0, 0))
        pygame.display.flip()
        pygame.time.delay(20)
    # Clear the screen after instructions
    screen.fill(WHITE)
    pygame.display.flip()
    show_reflect3_done = True


def show_instructions():
    # Show first page of instructions
    # screen.fill(WHITE)
    # screen.blit(instructions1, (0, 0))
    # pygame.display.flip()
    global show_instructions_done
    if show_instructions_done:
        return

    # Fade in
    for alpha in range(0, 255, 5):
        instructions1.set_alpha(alpha)
        screen.fill(WHITE)
        screen.blit(instructions1, (0, 0))
        pygame.display.flip()
        pygame.time.delay(20)

    # Wait for the player to press a key to move to the second page
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

    # Show second page of instructions
    screen.fill(WHITE)
    screen.blit(instructions2, (0, 0))  # Display second page image
    pygame.display.flip()

    # Wait for the player to press a key to exit instructions
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

# Show third page of instructions
    screen.fill(WHITE)
    screen.blit(instructions3, (0, 0))
    pygame.display.flip()

    # Wait for the player to press a key to move to the second page
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False
    # Fade out
    for alpha in range(255, 0, -5):
        instructions3.set_alpha(alpha)
        screen.fill(WHITE)
        screen.blit(instructions3, (0, 0))
        pygame.display.flip()
        pygame.time.delay(20)

    # Clear the screen after instructions
    screen.fill(WHITE)
    pygame.display.flip()

# Welcome screen
def welcome_screen():
    running = True

    while running:
        screen.fill(WHITE)  # Clear the screen with white background
        screen.blit(welcome_image, (0, 0))

        
        mouse_pos = pygame.mouse.get_pos()

        # Change button color when hovered
        button_color = LIGHT_BLUE if start_button_rect.collidepoint(mouse_pos) else BLUE

        pygame.draw.rect(screen, button_color, start_button_rect)
        start_text = small_font.render("Start", True, WHITE)
        screen.blit(start_text, (button_x + button_width // 2 - start_text.get_width() // 2,
                                button_y + 100 + button_height // 2 - start_text.get_height() // 2))

        pygame.display.flip()  # Update the screen

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    # Start button clicked, proceed to instructions
                    running = False
                    show_instructions()

# Call the welcome screen function
welcome_screen()

# After the instructions, your main game loop starts here
running = True

# BACKGROUND, AND ALL GAMEPLAY DETAILS
try:
    map_image = pygame.image.load('images/pachisi1.jpeg') if dice_roll_counter <  25 else pygame.image.load('images/antique_ludo.jpeg') if 25 <= dice_roll_counter < 35 else pygame.image.load('images/modern_ludo11.jpeg')
    map_image = pygame.transform.scale(map_image, (screen_width, screen_height - 100))
except pygame.error:
    print("Unable to load image. Please ensure 'antique_ludo.jpeg' is in the same directory.")
    sys.exit()



# GRID AND TOKENS
grid_size = 40
token_radius = grid_size // 3

# Load images of tokens 1
yellow_one_image = pygame.image.load('images/yellow_pawn.png')
blue_one_image = pygame.image.load('images/blue_pawn.png')
red_one_image = pygame.image.load('images/red_pawn.png')
green_one_image = pygame.image.load('images/green_pawn.png')
pawn_one_image = pygame.image.load('images/pawn.png')

yellow_one = pygame.transform.scale(yellow_one_image, (grid_size, grid_size))
blue_one= pygame.transform.scale(blue_one_image, (grid_size, grid_size))
red_one = pygame.transform.scale(red_one_image, (grid_size, grid_size))
green_one= pygame.transform.scale(green_one_image, (grid_size, grid_size))
pawn_one= pygame.transform.scale(pawn_one_image, (grid_size, grid_size))

# Load images of tokens 2
yellow_token_image = pygame.image.load('images/yellow_sepoy.png')
blue_token_image = pygame.image.load('images/blue_sepoy.png')
red_token_image = pygame.image.load('images/red_sepoy.png')
green_token_image = pygame.image.load('images/green_sepoy.png')

yellow_two = pygame.transform.scale(yellow_token_image, (grid_size, grid_size))
blue_two = pygame.transform.scale(blue_token_image, (grid_size, grid_size))
red_two = pygame.transform.scale(red_token_image, (grid_size, grid_size))
green_two = pygame.transform.scale(green_token_image, (grid_size, grid_size))

# Load image of the ship
ship_image = pygame.image.load('images/ship.png')
ship_image = pygame.transform.scale(ship_image, (300, 250))  # Scale the ship image

# Load vintage map background for ship animation
vintage_map_image = pygame.image.load('images/vintage_map.jpeg')
vintage_map_image = pygame.transform.scale(vintage_map_image, (screen_width, screen_height))

# Load patent image for animation
patent_image = pygame.image.load('images/patent.jpeg')
patent_image = pygame.transform.scale(patent_image, (screen_width, screen_height))

# TOKEN PATHS AND STARTS AND END POSITIONS
yellow_start_positions = [(10.5, 1.75), (10.5, 3.25), (12.2, 1.75), (12.2, 3.25)]
yellow_path = [
    (8,1), #Starting, yellow
    (8, 2), (8,3),(8, 4), (8, 5),  #Rest of # Right side, yellow
    (9,6), (10,6), (11,6), (12,6),(13,6),(14,6),   #Top, y
    (14,7), (14,8),   #Top to bottom, blue
    (13,8), (12,8), (11,8), (10,8), (9,8),   #Bottom, blue
    (8,9), (8,10), (8,11), (8,12), (8,13), (8,14),  #Right, red
    (7,14), (6,14), #Right to left, red
    (6,13), (6,12), (6,11), (6,10), (6,9),  #Left, red
    (5,8), (4,8), (3,8), (2,8), (1,8), (0,8), #Bottom, green
    (0,7), (0,6),   #Bottom to top, green
    (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), #Top, green
    (6,5), (6,4), (6,3), (6,2), (6,1), (6,0),  #Left, yellow
    (7,0),  #Before home run, yellow
    (7,1), (7,2), (7,3), (7,4), (7,5), 
    (7,6)   #Home run, yellow
]

yellow_end_position = (7, 6)

blue_start_positions = [(10.5, 10.5), (10.5, 12.2), (12.2, 10.5), (12.2, 12.2)]
blue_path = [ 
    (13,8), #Starting, blue
    (12,8), (11,8), (10,8), (9,8),   #Rest of #Bottom, blue
    (8,9), (8,10), (8,11), (8,12), (8,13), (8,14),  #Right, red
    (7,14), (6,14), #Right to left, red
    (6,13), (6,12), (6,11), (6,10), (6,9), #Left, red
    (5,8), (4,8), (3,8), (2,8), (1,8), (0,8), #Bottom, green
    (0,7), (0,6),   #Bottom to top, green
    (1,6), (2,6), (3,6), (4,6), (5,6),  #Top, green
    (6,5), (6,4), (6,3), (6,2), (6,1), (6,0),  #Left, yellow
    (7,0),  #Before home run, yellow
    (8,0),  #Connecting yellow right and left
    (8,1), #Starting, yellow
    (8, 2), (8,3),(8, 4), (8, 5),  #Rest of # Right side, yellow
    (9,6), (10,6), (11,6), (12,6),(13,6),(14,6),   #Top, blue
    (14,7),   #Before home run, blue
    (13,7), (12,7), (11,7), (10,7), (9,7), (8,7),   #Home run, blue
]

blue_end_position = (8, 7)

red_start_positions = [(2, 10.5), (2, 12.2), (3.25, 10.5), (3.25, 12.2)]
red_path = [ 
    (6,13), #Starting position, red
    (6,12), (6,11), (6,10), (6,9),  #Rest of #Left, red
    (5,8), (4,8), (3,8), (2,8), (1,8), (0,8), #Bottom, green
    (0,7), (0,6),   #Bottom to top, green
    (1,6), (2,6), (3,6), (4,6), (5,6), #Top, green
    (6,5), (6,4), (6,3), (6,2), (6,1), (6,0),  #Left, yellow
    (7,0),  #Before home run, yellow
    (8,0),  #Connecting yellow right and left
    (8,1), #Starting, yellow
    (8, 2), (8,3),(8, 4), (8, 5),  #Rest of # Right side, yellow
    (9,6), (10,6), (11,6), (12,6),(13,6),(14,6),   #Top, blue
    (14,7), (14,8),   #Top to bottom, blue
    (13,8), (12,8), (11,8), (10,8), (9,8),   #Bottom, blue
    (8,9), (8,10), (8,11), (8,12), (8,13), (8,14),  #Right, red
    (7,14),  #Before home base, red
    (7,13), (7,12), (7,11), (7,10), (7,9), (7,8) #Home run! Red
]
red_end_position = (7, 8)

green_start_positions = [(2, 1.75), (2, 3.25), (3.5, 1.75), (3.5, 3.25)]
green_path = [
    (1,6), (2,6), (3,6), (4,6), (5,6), #Top, green
    (6,5), (6,4), (6,3), (6,2), (6,1), (6,0),  #Left, yellow
    (7,0),  #Before home run, yellow
    (8,0),  #Connecting yellow right and left
    (8,1), #Starting, yellow
    (8, 2), (8,3),(8, 4), (8, 5) , #Rest of # Right side, yellow
    (9,6), (10,6), (11,6), (12,6),(13,6),(14,6),   #Top, blue
    (14,7), (14,8),   #Top to bottom, blue
    (13,8), (12,8), (11,8), (10,8), (9,8),   #Bottom, blue
    (8,9), (8,10), (8,11), (8,12), (8,13), (8,14),  #Right, red
    (7,14), (6,14), #Right to left, red
    (6,13), (6,12), (6,11), (6,10), (6,9),  #Left, red
    (5,8), (4,8), (3,8), (2,8), (1,8), (0,8), #Bottom, green
    (1,7), (2,7), (3,7), (4,7), (5,7), (6,7) #Home run!! Green
]


green_end_position = (6,7)

# Initialize tokens
yellow_tokens = yellow_start_positions.copy()
blue_tokens = blue_start_positions.copy()
red_tokens = red_start_positions.copy()
green_tokens = green_start_positions.copy()

# Scores for each color
scores = {'yellow': 0, 'blue': 0, 'red': 0, 'green': 0}


# Button dimensions and placement
button_width, button_height = 150, 35
button_color = BLUE
button_hover_color = LIGHT_BLUE
button_text = "Roll Dice"
button_rect = pygame.Rect((screen_width // 2 - button_width // 2, screen_height - button_height - 50), (button_width, button_height))


# Button dimensions
wbutton_width, button_height = 200, 60
wbutton_x = screen_width // 2 - button_width // 2

# Turns
turn_order = ['yellow', 'blue', 'red', 'green']
current_turn_index = 0

# Roll dice
def roll_dice():
    return random.randint(1, 6)

# def roll_dice(): #FOR DEMOS, IF YOU WANT THE DICE TO ROLL FAST!
#     # Choose only from the even numbers: 2, 4, 6
#     return random.choice([2, 4, 6])


# BASIC TEMPLATE FOR FADING IN AND OUT, NOT USED DIRECTLY BUT EXISTS FOR OTHER FUNCTIONS
def animate_fade_in_out_scroll():
    global fade_animation_done
    if fade_animation_done:
        return
    # Fade in
    for alpha in range(0, 255, 5):
        scroll_image.set_alpha(alpha)
        screen.fill(WHITE)
        screen.blit(scroll_image, (0, 0))
        pygame.display.flip()
        pygame.time.delay(20)

    # Wait for the player to press a key
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

    # Fade out
    for alpha in range(255, 0, -5):
        scroll_image.set_alpha(alpha)
        screen.fill(WHITE)
        screen.blit(scroll_image, (0, 0))
        pygame.display.flip()
        pygame.time.delay(20)
    # Clear the screen after instructions
    screen.fill(WHITE)
    pygame.display.flip()
    fade_animation_done = True

# Animate patent image
def animate_patent():
    global patent_animation_done
    if patent_animation_done:
        return
    print("Animating patent image across the screen...")  # Print statement to indicate patent animation start

    # Zoom in animation
    for scale in range(1, 6):
        scaled_image = pygame.transform.scale(patent_image, (screen_width * scale, screen_height * scale))
        rect = scaled_image.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.fill(WHITE)  # Clear the screen

        screen.blit(scaled_image, rect)
        pygame.display.flip()
        pygame.time.delay(150)  # Control the speed of the zoom-in

    # Directly display the scroll image and "PATENT" text after fading out the patent image
    for alpha in range(0, 255, 5):
        patent1.set_alpha(alpha)
        screen.fill(WHITE)
        screen.blit(patent1, (0, 0))
        pygame.display.flip()
        pygame.time.delay(20)

    # Wait for the player to press a key to move to the second page
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

    # Show second page of instructions
    screen.fill(WHITE)
    screen.blit(patent2, (0, 0))  # Display second page image
    pygame.display.flip()

    # Wait for the player to press a key to exit instructions
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False
    # Fade out
    for alpha in range(0, 255, -5):
        patent2.set_alpha(alpha)
        screen.fill(WHITE)
        screen.blit((patent2), (0, 0))
        pygame.display.flip()
        pygame.time.delay(20)

    # Transition to the 'royal_ludo' background
    screen.fill(WHITE)  # Clear the screen after the player continues
    pygame.display.flip()

    # Change the background to 'antique_ludo.jpeg' after the animation and text
    global map_image
    map_image = pygame.image.load('images/antique_ludo.jpeg')
    map_image = pygame.transform.scale(map_image, (screen_width, screen_height - 100))

    patent_animation_done = True


# Animate ship movement
def animate_ship():
    global ship_animation_done
    if ship_animation_done:
        return
    print("Animating ship across the screen...")  # Print statement to indicate ship animation start
    ship_x = -100  # Start off-screen on the left
    ship_y = screen_height - 300  # Position at the bottom of the screen

    # Remove existing visuals before starting the animation
    screen.blit(vintage_map_image, (0, 0))
    pygame.display.flip()

    # Animate the ship moving across the screen
    while ship_x < screen_width:
        screen.blit(vintage_map_image, (0, 0))  # Ensure the screen is cleared for the ship animation
        screen.blit(ship_image, (ship_x-50, ship_y-150))  # Draw the ship
        pygame.display.flip()  # Update the screen

        ship_x += 10  # Move the ship to the right twice as fast
        pygame.time.delay(25)  # Control the speed of the ship

    # Fade in
    for alpha in range(0, 255, 5):
        colony1.set_alpha(alpha)
        screen.fill(WHITE)
        screen.blit(colony1, (0, 0))
        pygame.display.flip()
        pygame.time.delay(20)

    # Wait for the player to press a key to continue
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False
    
    # Show second page of colony
    screen.fill(WHITE)
    screen.blit(colony2, (0, 0))  # Display second page image
    pygame.display.flip()

    # Wait for the player to press a key to continue
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False
    
    # Fade out
    for alpha in range(0, 255, -5):
        colony2.set_alpha(alpha)
        screen.fill(WHITE)
        screen.blit((colony2), (0, 0))
        pygame.display.flip()
        pygame.time.delay(20)
    
    # Remove the scroll image
    screen.fill(WHITE)
    pygame.display.flip()

    # Change the background to 'Ludo.jpeg' after the ship animation and colonialism text
    global map_image
    map_image = pygame.image.load('images/Ludo.jpeg')
    map_image = pygame.transform.scale(map_image, (screen_width, screen_height - 100))
    ship_animation_done = True

# Draw highlighted token
def draw_highlighted_token(token_position, token_color):
    pygame.draw.circle(screen, WHITE, (token_position[0] * grid_size + grid_size // 2, token_position[1] * grid_size + grid_size // 2), token_radius + 5, 3)
    pygame.draw.circle(screen, token_color, (token_position[0] * grid_size + grid_size // 2, token_position[1] * grid_size + grid_size // 2), token_radius)


# Function to display total scores
def display_scores():
    screen.blit(scroll_image, (0, 0))
    # Find the winning color
    winning_color = max(scores, key=scores.get)
    winning_text = f"{winning_color.capitalize()} WINS!"
    win_text_surface = font.render(winning_text, True, BLACK)
    screen.blit(win_text_surface, (screen_width // 2 - win_text_surface.get_width() // 2, 50))

    # Display scores for each color
    y_offset = 150
    for color, score in scores.items():
        score_text = f"{color.capitalize()}: {score}"
        score_surface = small_font.render(score_text, True, BLACK)
        screen.blit(score_surface, (screen_width // 2 - score_surface.get_width() // 2, y_offset))
        y_offset += 50

    #  GitHub
    github_text = "Check out alvs210's GitHub!"
    github_surface = small_font.render(github_text, True, BLACK)
    screen.blit(github_surface, (screen_width // 2 - github_surface.get_width() // 2, y_offset + 50))

    #  Thanks for Playing
    thanks_text = "Thanks for playing!"
    thanks_surface = small_font.render(thanks_text, True, BLACK)
    screen.blit(thanks_surface, (screen_width // 2 - thanks_surface.get_width() // 2, y_offset + 100))


    pygame.display.flip()



# Draw board with tokens
def draw_board_with_tokens(dice_roll=None, win=False):
    # Board background
    map_image = pygame.image.load('images/pachisi1.jpeg') if dice_roll_counter < 25 else pygame.image.load('images/antique_ludo.jpeg') if 25 <= dice_roll_counter < 35 else pygame.image.load('images/modern_ludo11.jpeg')
    map_image = pygame.transform.scale(map_image, (screen_width, screen_height - 100))
    screen.blit(map_image, (0, 0))
    
    # Draw tokens on top of the board
    for i, (x, y) in enumerate(yellow_tokens):
        if dice_roll_counter < 25:
            screen.blit(yellow_one, (x * grid_size, y * grid_size))
        elif 25 <= dice_roll_counter < 35:
            screen.blit(yellow_two, (x * grid_size, y * grid_size))
        else:
            pygame.draw.circle(screen, YELLOW, (x * grid_size + grid_size // 2, y * grid_size + grid_size // 2), token_radius)
    
    for i, (x, y) in enumerate(blue_tokens):
        if dice_roll_counter < 25:
            screen.blit(blue_one, (x * grid_size, y * grid_size))
        elif 25 <= dice_roll_counter < 35:
            screen.blit(blue_two, (x * grid_size, y * grid_size))
        else:
            pygame.draw.circle(screen, BLUE, (x * grid_size + grid_size // 2, y * grid_size + grid_size // 2), token_radius)
    
    for i, (x, y) in enumerate(red_tokens):
        if dice_roll_counter < 25:
            screen.blit(red_one, (x * grid_size, y * grid_size))
        elif 25 <= dice_roll_counter < 35:
            screen.blit(red_two, (x * grid_size, y * grid_size))
        else:
            pygame.draw.circle(screen, RED, (x * grid_size + grid_size // 2, y * grid_size + grid_size // 2), token_radius)
    
    for i, (x, y) in enumerate(green_tokens):
        if dice_roll_counter < 25:
            screen.blit(green_one, (x * grid_size, y * grid_size))
        elif 25 <= dice_roll_counter < 35:
            screen.blit(green_two, (x * grid_size, y * grid_size))
        else:
            pygame.draw.circle(screen, GREEN, (x * grid_size + grid_size // 2, y * grid_size + grid_size // 2), token_radius)
    
    # Dice dimensions and drawing

    if dice_roll is not None and not win:
        # Draw a simple white dice
        dice_size = 60
        dice_x = screen_width // 2 - dice_size // 2
        dice_y = screen_height // 2 - dice_size // 2 - 45
        pygame.draw.rect(screen, WHITE, (dice_x, dice_y, dice_size, dice_size))  # Draw the dice background
        pygame.draw.rect(screen, BLACK, (dice_x, dice_y, dice_size, dice_size), 2)  # Draw the dice border

        # Draw the number on the dice
        dice_text = small_font.render(str(dice_roll), True, BLACK)
        screen.blit(dice_text, (dice_x + dice_size // 2 - dice_text.get_width() // 2, dice_y + dice_size // 2 - dice_text.get_height() // 2))

    if current_turn is not None:
            if current_turn == 'yellow':
                text = turn_font.render("Yellow's Turn", True, TURN_YELLOW)
                text_rect = text.get_rect(topleft=(415, 10))
                pygame.draw.rect(screen, BOX_YELLOW, text_rect.inflate(10, 10))
                screen.blit(text, text_rect)
            elif current_turn == 'blue':
                text = turn_font.render("Blue's Turn", True, TURN_BLUE)
                text_rect = text.get_rect(topleft=(425, 560))
                pygame.draw.rect(screen, BOX_BLUE, text_rect.inflate(10, 10))
                screen.blit(text, text_rect)
            elif current_turn == 'red':
                text = turn_font.render("Red's Turn", True, RED)
                text_rect = text.get_rect(topleft=(55, 560))
                pygame.draw.rect(screen, BOX_RED, text_rect.inflate(10, 10))
                screen.blit(text, text_rect)
            elif current_turn == 'green':
                text = turn_font.render("Green's Turn", True, GREEN)
                text_rect = text.get_rect(topleft=(55, 10))
                pygame.draw.rect(screen, BOX_GREEN, text_rect.inflate(10, 10))
                screen.blit(text, text_rect)

    # Draw scores
    # Clear previous scores
    score_rect = pygame.Rect(10, screen_height - 40, screen_width - 20, 40)
    screen.fill(WHITE, score_rect)
    
    # Draw updated scores
    score_text = f"Scores: Yellow: {scores['yellow']} | Blue: {scores['blue']} | Red: {scores['red']} | Green: {scores['green']}"
    score_surface = small_font.render(score_text, True, BLACK)
    screen.blit(score_surface, (10, screen_height - 30))

    # Button
    if not win:
        pygame.draw.rect(screen, button_color, button_rect)
        text_surf = small_font.render(button_text, True, WHITE)
        screen.blit(text_surf, (button_rect.centerx - text_surf.get_width() // 2, button_rect.centery - text_surf.get_height() // 2))
    else:
        display_scores()

    pygame.display.flip()


# Animate token movement using the appropriate image based on logic
def animate_token_movement(start_pos, end_pos, token_color, dice_roll_counter):
    # Load the appropriate image based on the RGB value passed in
    if token_color == YELLOW:
        if dice_roll_counter < 25:
            token_image = yellow_one
        elif 25 <= dice_roll_counter <= 35:
            token_image = yellow_two
        else:
            token_image = None
            token_draw_color = YELLOW
    elif token_color == BLUE:
        if dice_roll_counter < 25:
            token_image = blue_one
        elif 25 <= dice_roll_counter <= 35:
            token_image = blue_two
        else:
            token_image = None
            token_draw_color = BLUE
    elif token_color == RED:
        if dice_roll_counter < 25:
            token_image = red_one
        elif 25 <= dice_roll_counter <= 35:
            token_image = red_two
        else:
            token_image = None
            token_draw_color = RED
    elif token_color == GREEN:
        if dice_roll_counter < 25:
            token_image = green_one
        elif 25 <= dice_roll_counter <= 35:
            token_image = green_two
        else:
            token_image = None
            token_draw_color = GREEN
    start_pixel_pos = (start_pos[0] * grid_size + grid_size // 2, start_pos[1] * grid_size + grid_size // 2)
    end_pixel_pos = (end_pos[0] * grid_size + grid_size // 2, end_pos[1] * grid_size + grid_size // 2)
    # Duration and frames for smooth animation
    duration = 0.2  # Duration in seconds
    frames_per_second = 60
    total_frames = int(duration * frames_per_second)

    # Delta per frame
    delta_x = (end_pixel_pos[0] - start_pixel_pos[0]) / total_frames
    delta_y = (end_pixel_pos[1] - start_pixel_pos[1]) / total_frames

    # Animate token movement
    for frame in range(total_frames):
        # Calculate intermediate position
        current_pixel_pos = (start_pixel_pos[0] + delta_x * frame, start_pixel_pos[1] + delta_y * frame)

        # Draw the board and tokens
        draw_board_with_tokens()

        # Draw the moving token in its intermediate position based on logic
        if token_image:
            # Draw the image token
            screen.blit(token_image, (current_pixel_pos[0] - token_image.get_width() // 2, 
                                      current_pixel_pos[1] - token_image.get_height() // 2))
        else:
            # Draw a circle as the token if no image is assigned
            pygame.draw.circle(screen, token_draw_color, (current_pixel_pos[0], current_pixel_pos[1]), token_radius)

        # Update the screen to show animation
        pygame.display.flip()

        # Control frame rate
        pygame.time.delay(int(1000 / frames_per_second))

    # Finally draw the token in its end position based on the logic
    draw_board_with_tokens()
    if token_image:
        screen.blit(token_image, (end_pixel_pos[0] - token_image.get_width() // 2, 
                                  end_pixel_pos[1] - token_image.get_height() // 2))
    else:
        pygame.draw.circle(screen, token_draw_color, (end_pixel_pos[0], end_pixel_pos[1]), token_radius)
    pygame.display.flip()

def move_token(tokens, path, dice_roll, selected_token):
    if tokens[selected_token] in path:
        current_position_index = path.index(tokens[selected_token])
        new_position_index = current_position_index + int(dice_roll)

        if new_position_index < len(path):
            new_position = path[new_position_index]

            # Check if the new position is occupied by an opponent's token
            all_tokens = yellow_tokens + blue_tokens + red_tokens + green_tokens
            for opponent_tokens, color in [
                (yellow_tokens, 'yellow'),
                (blue_tokens, 'blue'),
                (red_tokens, 'red'),
                (green_tokens, 'green')
            ]:
                # Determine the opponent's start positions dynamically
                opponent_start_positions = (
                    yellow_start_positions if opponent_tokens == yellow_tokens else
                    blue_start_positions if opponent_tokens == blue_tokens else
                    red_start_positions if opponent_tokens == red_tokens else
                    green_start_positions
                )
                
                if opponent_tokens != tokens and new_position in opponent_tokens:
                    opponent_index = opponent_tokens.index(new_position)

                    # Find an empty start position for the opponent token
                    for start_pos in opponent_start_positions:
                        if start_pos not in all_tokens:
                            opponent_tokens[opponent_index] = start_pos
                            print(f"{color.capitalize()} token sent back to start position: {start_pos}")
                            break

            # Move the selected token to the new position
            animate_token_movement(tokens[selected_token], new_position, 
                                   YELLOW if tokens == yellow_tokens else BLUE if tokens == blue_tokens else RED if tokens == red_tokens else GREEN, 
                                   dice_roll_counter)
            tokens[selected_token] = new_position
            print(f"Moved token to {new_position}")

            # Check if the token reached the end position
            if new_position == yellow_end_position and (tokens == yellow_tokens or tokens == yellow_one or tokens == yellow_two ):
                scores['yellow'] += 1
            elif new_position == blue_end_position and tokens == blue_tokens:
                scores['blue'] += 1
            elif new_position == red_end_position and tokens == red_tokens:
                scores['red'] += 1
            elif new_position == green_end_position and tokens == green_tokens:
                scores['green'] += 1

            animate_token_movement(tokens[selected_token], new_position, 
                                   YELLOW if tokens == yellow_tokens else BLUE if tokens == blue_tokens else RED if tokens == red_tokens else GREEN, 
                                   dice_roll_counter)
            tokens[selected_token] = new_position
            print(f"Moved token to {new_position}")
        
        elif new_position_index == len(path):
            # If it is out of range, meaning the score exceeds the end position and reached end position
            if tokens == yellow_tokens:
                scores['yellow'] += 1
                new_position = yellow_end_position
            elif tokens == blue_tokens:
                scores['blue'] += 1
                new_position = blue_end_position
            elif tokens == red_tokens:
                scores['red'] += 1
                new_position = red_end_position
            elif tokens == green_tokens:
                scores['green'] += 1
                new_position = green_end_position

            animate_token_movement(tokens[selected_token], new_position, 
                                   YELLOW if tokens == yellow_tokens else BLUE if tokens == blue_tokens else RED if tokens == red_tokens else GREEN, 
                                   dice_roll_counter)
            tokens[selected_token] = new_position
            print(f"Moved token to {new_position}")



# Move token from start
def move_token_from_start(tokens, path, start_positions, dice_roll, selected_token):
    if tokens[selected_token] in start_positions:
        new_position = path[0]
        if new_position not in tokens:
            animate_token_movement(tokens[selected_token], new_position, YELLOW if tokens == yellow_tokens else BLUE if tokens == blue_tokens else RED if tokens == red_tokens else GREEN, dice_roll_counter)
            tokens[selected_token] = new_position
            print(f"Moved token from start to {new_position}")

# Check win condition
def check_win_condition(tokens, end_position):
    return all(pos == end_position for pos in tokens)

# Select token by click
def select_token_by_click(mouse_pos, tokens):
    for i, pos in enumerate(tokens):
        if pos:
            token_pos = (pos[0] * grid_size + grid_size // 2, pos[1] * grid_size + grid_size // 2)
            distance = ((mouse_pos[0] - token_pos[0]) ** 2 + (mouse_pos[1] - token_pos[1]) ** 2) ** 0.5
            if distance <= token_radius:
                return i  # Return the index of the selected token
    return None

# Main game loop
running = True
# dice_roll = None
win = False
selected_token = None
waiting_for_six_choice = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not win:
            if button_rect.collidepoint(event.pos):  # Check if the button is clicked
                dice_roll = roll_dice()  # Roll the dice
                dice_roll_counter += 1
                current_turn = turn_order[current_turn_index]  # Determine the current player's turn

                # Set up the correct tokens, path, and start positions based on the current turn
                if current_turn == 'yellow':
                    tokens = yellow_tokens
                    path = yellow_path
                    start_positions = yellow_start_positions
                    end_position = yellow_end_position
                elif current_turn == 'blue':
                    tokens = blue_tokens
                    path = blue_path
                    start_positions = blue_start_positions
                    end_position = blue_end_position
                elif current_turn == 'red':
                    tokens = red_tokens
                    path = red_path
                    start_positions = red_start_positions
                    end_position = red_end_position
                elif current_turn == 'green':

                    tokens = green_tokens
                    path = green_path
                    start_positions = green_start_positions
                    end_position = green_end_position

                if dice_roll == 6:
                    waiting_for_six_choice = True
                else:
                    selected_token = None  # Reset selected token if no 6 is rolled
            else:
                if dice_roll is not None:  # If a dice roll has occurred
                    selected_token = select_token_by_click(event.pos, tokens)  # Allow the player to select a token to move
                    if selected_token is not None:
                        if waiting_for_six_choice:
                            if tokens[selected_token] in start_positions:
                                move_token_from_start(tokens, path, start_positions, dice_roll, selected_token)
                            else:
                                move_token(tokens, path, dice_roll, selected_token)
                                #def move_token(tokens, path, dice_roll, selected_token):
                            waiting_for_six_choice = False
                        else:
                            move_token(tokens, path, dice_roll, selected_token)

                        if check_win_condition(tokens, end_position):
                            win = True
                        else:
                            current_turn_index = (current_turn_index + 1) % len(turn_order)

                    dice_roll = None

    # Change button color on hover
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        button_color = LIGHT_BLUE
    else:
        button_color = BLUE

    # Draw the board and tokens with the current dice roll
    draw_board_with_tokens(dice_roll, win)

    # Animate ship after the 5th turn
    if dice_roll_counter == 15:
        animate_ship()
    #animate patent after 10
    if dice_roll_counter == 25:
        animate_patent()
    #animate COVID after 25
    if dice_roll_counter == 35:
        show_COVID()
    #animate reflective questions
    if dice_roll_counter == 40:
        show_reflect1()
    if dice_roll_counter == 45:
        show_reflect2()
    if dice_roll_counter == 50:
        show_reflect3()

pygame.quit()
sys.exit()
