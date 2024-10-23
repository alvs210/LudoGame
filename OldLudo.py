import pygame
import sys
import random

current_turn = None

# Initialize Pygame
pygame.init()

# Screen setup
screen_width, screen_height = 600, 630   #Extra room at bottom for button
screen = pygame.display.set_mode((screen_width, screen_height))

#BACKGROUND
try:
    map_image = pygame.image.load('Ludo.jpeg')  #IMAGE MUST BE IN SAME DIRECTORY
    map_image = pygame.transform.scale(map_image, (screen_width, screen_height-30))
except pygame.error:
    print("Unable to load image. Please ensure 'Ludo.jpeg' is in the same directory.")
    sys.exit()

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 155, 0)
BLUE = (0, 100, 255)
YELLOW = (255, 155, 0)
LIGHT_BLUE = (0, 155, 255)

#GRID AND TOKENS
grid_size = 40
token_radius = grid_size // 3

#TOKEN PATHS AND STARTS AND END POSITIONS
yellow_start_positions = [(11, 2), (11, 3), (12, 2), (12, 3)]
yellow_path = [
    (8,1), #Starting, yellow
    (8, 2), (8,3),(8, 4), (8, 5), (8, 6),  #Rest of # Right side, yellow
    (9,6), (10,6), (11,6), (12,6),(13,6),(14,6),   #Top, blue
    (14,7), (14,8),   #Top to bottom, blue
    (13,8), (12,8), (11,8), (10,8), (9,8), (8,8),   #Bottom, blue
    (8,9), (8,10), (8,11), (8,12), (8,13), (8,14),  #Right, red
    (7,14), (6,14), #Right to left, red
    (6,13), (6,12), (6,11), (6,10), (6,9), (6,8),  #Left, red
    (5,8), (4,8), (3,8), (2,8), (1,8), (0,8), #Bottom, green
    (0,7), (0,6),   #Bottom to top, green
    (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), #Top, green
    (6,5), (6,4), (6,3), (6,2), (6,1), (6,0),  #Left, yellow
    (7,0),  #Before home run, yellow
    (7,1), (7,2), (7,3), (7,4), (7,5), (7,6)   #Home run, yellow
]
yellow_end_position = [(7,6)]

blue_start_positions = [(11, 11), (11, 12), (12, 11), (12, 12)]
blue_path = [ 
    (13,8), #Starting, blue
    (12,8), (11,8), (10,8), (9,8), (8,8),   #Rest of #Bottom, blue
    (8,9), (8,10), (8,11), (8,12), (8,13), (8,14),  #Right, red
    (7,14), (6,14), #Right to left, red
    (6,13), (6,12), (6,11), (6,10), (6,9), (6,8),  #Left, red
    (5,8), (4,8), (3,8), (2,8), (1,8), (0,8), #Bottom, green
    (0,7), (0,6),   #Bottom to top, green
    (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), #Top, green
    (6,5), (6,4), (6,3), (6,2), (6,1), (6,0),  #Left, yellow
    (7,0),  #Before home run, yellow
    (8,0),  #Connecting yellow right and left
    (8,1), #Starting, yellow
    (8, 2), (8,3),(8, 4), (8, 5), (8, 6),  #Rest of # Right side, yellow
    (9,6), (10,6), (11,6), (12,6),(13,6),(14,6),   #Top, blue
    (14,7),   #Before home run, blue
    (13,7), (12,7), (11,7), (10,7), (9,7), (8,7),   #Home run, blue
]
blue_end_position = [(8,7)]

red_start_positions = [(2, 11), (2, 12), (3, 11), (3, 12)]
red_path = [ 
    (6,10), #Starting position, red
    (6,12), (6,11), (6,10), (6,9), (6,8),  #Rest of #Left, red
    (5,8), (4,8), (3,8), (2,8), (1,8), (0,8), #Bottom, green
    (0,7), (0,6),   #Bottom to top, green
    (0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), #Top, green
    (6,5), (6,4), (6,3), (6,2), (6,1), (6,0),  #Left, yellow
    (7,0),  #Before home run, yellow
    (8,0),  #Connecting yellow right and left
    (8,1), #Starting, yellow
    (8, 2), (8,3),(8, 4), (8, 5), (8, 6),  #Rest of # Right side, yellow
    (9,6), (10,6), (11,6), (12,6),(13,6),(14,6),   #Top, blue
    (14,7), (14,8),   #Top to bottom, blue
    (13,8), (12,8), (11,8), (10,8), (9,8), (8,8),   #Bottom, blue
    (8,9), (8,10), (8,11), (8,12), (8,13), (8,14),  #Right, red
    (7,14),  #Before home base, red
    (7,13), (7,12), (7,11), (7,10), (7,9), (7,8) #Home run! Red
]
red_end_positions = [(7,8)]

green_start_positions = [(2, 2), (2, 3), (3, 2), (3, 3)]
green_path = [
    (0,6), #Green start position
    (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), #Top, green
    (6,5), (6,4), (6,3), (6,2), (6,1), (6,0),  #Left, yellow
    (7,0),  #Before home run, yellow
    (8,0),  #Connecting yellow right and left
    (8,1), #Starting, yellow
    (8, 2), (8,3),(8, 4), (8, 5), (8, 6),  #Rest of # Right side, yellow
    (9,6), (10,6), (11,6), (12,6),(13,6),(14,6),   #Top, blue
    (14,7), (14,8),   #Top to bottom, blue
    (13,8), (12,8), (11,8), (10,8), (9,8), (8,8),   #Bottom, blue
    (8,9), (8,10), (8,11), (8,12), (8,13), (8,14),  #Right, red
    (7,14), (6,14), #Right to left, red
    (6,13), (6,12), (6,11), (6,10), (6,9), (6,8),  #Left, red
    (5,8), (4,8), (3,8), (2,8), (1,8), (0,8), #Bottom, green
    (0,7), #Before home base, green
    (0,7), (1,7), (2,7), (3,7), (4,7), (5,7), (6,7) #Home run!! Green
]
green_end_position = [(6,7)]

#INITIALIZE TOKENS
yellow_tokens = yellow_start_positions.copy()
green_tokens = green_start_positions.copy()
red_tokens = red_start_positions.copy()
blue_tokens = blue_start_positions.copy()

#FONT
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)
turn_font = pygame.font.Font(None, 30)

#BUTTON DIMENSIONS AND PLACEMENT
button_width, button_height = 150, 35
button_color = BLUE
button_hover_color = LIGHT_BLUE
button_text = "Roll Dice"
button_rect = pygame.Rect((screen_width // 2 - button_width // 2, screen_height - button_height - 10), (button_width, button_height))

#TURNS
turn_order = ['yellow', 'green', 'red', 'blue']
current_turn_index = 0

def roll_dice():
    return random.randint(1, 6)

def draw_board_with_tokens(dice_roll=None, win=False):
    #BOARD BACKGROUND
    screen.blit(map_image, (0, 0))
    
    # Draw tokens on top of the board
    for x, y in green_tokens:
        pygame.draw.circle(screen, GREEN, (x * grid_size + grid_size // 2, y * grid_size + grid_size // 2), token_radius)
    for pos in yellow_tokens:
        if pos:  # Only draw if the token has a valid position
            pygame.draw.circle(screen, YELLOW, (pos[0] * grid_size + grid_size // 2, pos[1] * grid_size + grid_size // 2), token_radius)
    for x, y in blue_tokens:
        pygame.draw.circle(screen, BLUE, (x * grid_size + grid_size // 2, y * grid_size + grid_size // 2), token_radius)
    for x, y in red_tokens:
        pygame.draw.circle(screen, RED, (x * grid_size + grid_size // 2, y * grid_size + grid_size // 2), token_radius)
    
    #DICE DIMENSIONS AND DRAWING  #2.06 because dimensions of image vs. board not perfectly aligned
    if dice_roll is not None and not win:
        dice_text = font.render(str(dice_roll), True, BLACK)
        screen.blit(dice_text, (screen_width // 2 - dice_text.get_width() // 2, screen_height // 2.06 - dice_text.get_height() // 2))

    if current_turn is not None:
        if current_turn == 'yellow':
        # Display "Yellow's Turn" on the game screen
            text = turn_font.render("Yellow's Turn", True, YELLOW)  # Yellow color
            screen.blit(text, (415, 10))  # Position the text on the screen (adjust as necessary)
        if current_turn == 'green':
            # Display "Green's Turn" on the game screen
            text = turn_font.render("Green's Turn", True, GREEN)  # Green color
            screen.blit(text, (55, 10))  # Position the text on the screen (adjust as necessary)
        if current_turn == 'red':
            # Display "Green's Turn" on the game screen
            text = turn_font.render("Red's Turn", True, RED)  # Green color
            screen.blit(text, (75, 575))  # Position the text on the screen (adjust as necessary)
        if current_turn == 'blue':
            # Display "Green's Turn" on the game screen
            text = turn_font.render("Blue's Turn", True, BLUE)  # Green color
            screen.blit(text, (425, 575))  # Position the text on the screen (adjust as necessary)

    #NOT WON, DRAW BOARD
    if not win:
        pygame.draw.rect(screen, button_color, button_rect)
        text_surf = small_font.render(button_text, True, WHITE)
        screen.blit(text_surf, (button_rect.centerx - text_surf.get_width() // 2, button_rect.centery - text_surf.get_height() // 2))
    else:
        #YOU WIN!
        win_text = font.render("YOU WIN!", True, BLACK)
        screen.blit(win_text, (screen_width // 2 - win_text.get_width() // 2, screen_height // 2 - win_text.get_height() // 2))

    pygame.display.flip()

def move_token(tokens, path, start_position, dice_roll, selected_token):
    # Check if the selected token is on the path
    if tokens[selected_token] in path:
        current_position_index = path.index(tokens[selected_token])
        new_position_index = current_position_index + dice_roll

        # Check if the new position is within the path boundary
        if new_position_index < len(path):
            new_position = path[new_position_index]

            # Check if the new position is occupied by an opponent's token
            for opponent_tokens, opponent_start_positions in zip(
                    [yellow_tokens, green_tokens, red_tokens, blue_tokens],
                    [yellow_start_positions, green_start_positions, red_start_positions, blue_start_positions]):

                # Ensure we're not checking the player's own tokens
                if opponent_tokens != tokens and new_position in opponent_tokens:
                    # Find the opponent's token that occupies the new position
                    opponent_token_index = opponent_tokens.index(new_position)

                    # Find an empty start position for the opponent's token
                    found_empty_start = False
                    for start_position in opponent_start_positions:
                        if start_position not in opponent_tokens:  # Check if the start position is empty
                            opponent_tokens[opponent_token_index] = start_position  # Move the opponent's token to the start
                            found_empty_start = True
                            break  # Exit the loop once an empty start position is found

                    if not found_empty_start:
                        print("Error: No empty start position available for opponent's token!")
                    break  # Exit the loop since we've already handled the collision

            # If the new position is not occupied by another of the player's tokens, move the token
            if new_position not in tokens:
                tokens[selected_token] = new_position
                print(f"Moved token to {new_position}")

        else:  # If the new position index is beyond the path's end, move to the final position
            final_position = path[-1]
            if final_position not in tokens:
                tokens[selected_token] = final_position
                print(f"Moved token to final position {final_position}")


def move_token_from_start(tokens, path, start_positions, dice_roll, selected_token):

        # Move a token out of the starting position if the dice roll is 6
        if tokens[selected_token] in start_positions:
            new_position = path[0]
            if new_position not in tokens:  #NO STACKING, too much complexity uggh add later
                tokens[selected_token] = new_position

        # Check if the new position is occupied by an opponent's token
            for opponent_tokens, opponent_start_positions in zip(
                    [yellow_tokens, green_tokens, red_tokens, blue_tokens],
                    [yellow_start_positions, green_start_positions, red_start_positions, blue_start_positions]):

                # Ensure we're not checking the player's own tokens
                if opponent_tokens != tokens and new_position in opponent_tokens:
                    # Find the opponent's token that occupies the new position
                    opponent_token_index = opponent_tokens.index(new_position)

                    # Find an empty start position for the opponent's token
                    found_empty_start = False
                    for start_position in opponent_start_positions:
                        if start_position not in opponent_tokens:  # Check if the start position is empty
                            opponent_tokens[opponent_token_index] = start_position  # Move the opponent's token to the start
                            found_empty_start = True
                            break  # Exit the loop once an empty start position is found

                    if not found_empty_start:
                        print("Error: No empty start position available for opponent's token!")
                    break  # Exit the loop since we've already handled the collision

            # If the new position is not occupied by another of the player's tokens, move the token
            if new_position not in tokens:
                tokens[selected_token] = new_position
                print(f"Moved token to {new_position}")


def check_win_condition(tokens, end_position):
    # Check if all tokens have reached their end position
    return all(pos == end_position for pos in tokens)

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
dice_roll = None
win = False
selected_token = None
waiting_for_six_choice = False

# Main game loop
running = True
dice_roll = None
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
                current_turn = turn_order[current_turn_index]  # Determine the current player's turn

                # Set up the correct tokens, path, and start positions based on the current turn
                if current_turn == 'yellow':
                    tokens = yellow_tokens
                    path = yellow_path
                    start_positions = yellow_start_positions
                    end_position = yellow_end_position
                elif current_turn == 'green':
                    tokens = green_tokens
                    path = green_path  # Ensure this is defined
                    start_positions = green_start_positions
                    end_position = green_end_position  # Ensure this is defined
                elif current_turn == 'red':
                    tokens = red_tokens
                    path = red_path  # Ensure this is defined
                    start_positions = red_start_positions
                    end_position = red_end_positions  # Ensure this is defined
                elif current_turn == 'blue':
                    tokens = blue_tokens
                    path = blue_path
                    start_positions = blue_start_positions
                    end_position = blue_end_position

                if dice_roll == 6:
                    # If a 6 is rolled, the player may choose to move a token out of the start position or move another token
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
                                move_token(tokens, path, start_positions, 6, selected_token)
                            waiting_for_six_choice = False  # Reset after handling the 6 roll case
                        else:
                            move_token(tokens, path, start_positions, dice_roll, selected_token)

                        # Check if the current player has won
                        if check_win_condition(tokens, end_position):
                            win = True
                        else:
                            # Move to the next player's turn if no win
                            current_turn_index = (current_turn_index + 1) % len(turn_order)

                    dice_roll = None  # Reset the dice roll after the move

    # Change button color on hover
    if button_rect.collidepoint(pygame.mouse.get_pos()):
        button_color = LIGHT_BLUE
    else:
        button_color = BLUE

    # Draw the board and tokens with the current dice roll
    draw_board_with_tokens(dice_roll, win)

pygame.quit()
sys.exit()
