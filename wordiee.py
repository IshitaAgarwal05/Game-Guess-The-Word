# Author: Ishita Agarwal

# Importing Libraries
import random
import sys
import pygame
from list import *

# Initiating pygame and game window
pygame.init()
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption("Guess the Word!")

# Loading background image
bgimg = pygame.image.load("bg.jpg").convert()
bgimg = pygame.transform.scale(bgimg, (700, 1245))

# Creating a translucent rectangle on the screen for better visibility
def create_transparent_rect(width, height, color, alpha):
    rect_surf = pygame.Surface((width, height), pygame.SRCALPHA)
    rect_surf.fill((*color, alpha))
    return rect_surf

# Function for displaying text in the game
def display_text(text, x, y, size):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

# Function for displaying instructions in the beginning of the game
def display_instructions():
    screen.blit(bgimg, (0, 0))

    # Create and blit the transparent rectangle
    transparent_rect = create_transparent_rect(600, 600, (0, 0, 0), 192)  # 75% transparency
    screen.blit(transparent_rect, (50, 50))  # Centered at (50, 50)

    font = pygame.font.SysFont(None, 50)
    text = font.render("Guess The Word!", True, (0, 0, 255))
    text_rect = text.get_rect(center=(350, 250))
    screen.blit(text, text_rect)

    instructions = [
        "Welcome to the Word Game!",
        "Guess the word to clear the game.",
        "Upper case letters denote,", 
        "correct letters at correct position.",
        "Lower case letters denote,", 
        "correct letters at incorrect position.",
        "Underscores (_) denote incorrect letters.", 
        "Press any key to continue!"
    ]

    for i, instruction in enumerate(instructions):
        display_text(instruction, 350, 350 + i * 30, 30)

    pygame.display.flip()
    wait_for_key()

# Function for making the game wait, until the user signals to move ahead by pressing a key
def wait_for_key():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                return 

# Function to choose a word and its hint randomly from the list.py file
def choose_word(used_words):
    available_words = [word for word in words if word not in used_words]
    if not available_words:
        return None, None
    
    chosen_one = random.choice(available_words)
    hint = random.choice(words_dict.get(chosen_one, "None"))
    used_words.add(chosen_one)
    return chosen_one, hint

# Function to compare and check the guess made by user with the chosen word
def check_guess(chosen_one, guess, result):
    chosen_one_list = list(chosen_one)
    new_result = list(result)

    # First pass: Check for correct letters in the correct positions
    for i in range(len(chosen_one)):
        if guess[i].upper() == chosen_one[i].upper():
            new_result[i] = guess[i].upper()
            chosen_one_list[i] = '_'

    # Second pass: Check for correct letters in incorrect positions
    for i in range(len(chosen_one)):
        if new_result[i] == '_' and guess[i] in chosen_one_list:
            new_result[i] = guess[i].lower()
            chosen_one_list[chosen_one_list.index(guess[i])] = '_'

    return new_result

# Funtion to get the user's input for the guess
def get_user_guess(num, num2, num3, chosen_one, result, attempt, hint):
    guess = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    guess = guess[:-1]
                elif event.key == pygame.K_RETURN:
                    return guess
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    if len(guess) < len(chosen_one):
                        guess += event.unicode

        screen.blit(bgimg, (0, 0))
        transparent_rect = create_transparent_rect(600, 600, (0, 0, 0), 192)  # 75% transparency
        screen.blit(transparent_rect, (50, 50))  # Centered at (50, 50)
        display_text(f"Attempts Left: {attempt}", 200, 100, 40)
        display_text(f"Round: {round_go}", 550, 100, 40)
        display_text(f"Hint: {hint}", 350, 150, 30)
        
        for i in range(len(chosen_one)):
            if attempt == 3:
                if i == num or i == num2 or i == num3: 
                    # print(chosen_one[i], sep="", end="")
                    display_text(chosen_one[i], 200+ i*30, 300, 50)
                    result[i] = chosen_one[i]
                elif chosen_one[i] == " ":
                    display_text(chosen_one[i], 200+ i*30, 300, 50)
                    result[i] = chosen_one[i]
                else: 
                    # print("_", sep="", end="")
                    display_text("_", 200+ i*30, 300, 50)
            else:
                display_text(result[i], 200+ i*30, 300, 50)

        transparent_rect2 = create_transparent_rect(500, 100, (0, 75, 0), 230)
        screen.blit(transparent_rect2, (100, 500)) 
        display_text(guess, 350, 550, 50)
        pygame.display.flip()

# Main game looping function
def play_game():
    global round_go
    round_go = 0
    used_words = set()
    display_instructions()
    
    while True:
        round_go += 1
        cleared = False
        chosen_one, hint = choose_word(used_words)
        if not chosen_one:
            display_text("You WON the Game!", 350, 450, 30)
            pygame.display.flip()
            wait_for_key()
            return

        attempt = 3
        result = ['_'] * len(chosen_one)
        num = random.randint(0,len(chosen_one)-1)
        num2 = None
        num3 = None

        if len(chosen_one) > 9:
            while num2 == num:
                num2 = random.randint(0,len(chosen_one)-1)
            while num3 == num or num3 == num2:
                num3 = random.randint(0,len(chosen_one)-1)
        elif len(chosen_one) > 5:
            while num2 == num:
                num2 = random.randint(0,len(chosen_one)-1)
        
        # print('-'*25)
        # print("Welcome to the Word Game!")
        # print("Guess the word to clear the game.")
        # print("Upper case letters denote, correct letters at correct position.")
        # print("Lower case letters denote, correct letters at incorrect position.")
        # print("Underscores (_) denote incorrect letters.")
        # print('-'*25)
        
        while attempt > 0:
            screen.blit(bgimg, (0, 0))
            transparent_rect = create_transparent_rect(600, 600, (0, 0, 0), 192)  # 75% transparency
            screen.blit(transparent_rect, (50, 50))  # Centered at (50, 50)
            display_text(f"Attempts Left: {attempt}", 200, 100, 40)
            display_text(f"Round: {round_go}", 550, 100, 40)
            pygame.display.flip()
            # print()
            
            for i in range(len(chosen_one)):
                if attempt == 3:
                    if i == num or i == num2 or i == num3: 
                        # print(chosen_one[i], sep="", end="")
                        display_text(chosen_one[i], 200+ i*30, 300, 50)
                        result[i] = chosen_one[i]
                    elif chosen_one[i] == " ":
                        display_text(chosen_one[i], 200+ i*30, 300, 50)
                        result[i] = chosen_one[i]
                    else: 
                        # print("_", sep="", end="")
                        display_text("_", 200+ i*30, 300, 50)
                else:
                    display_text(result[i], 200+ i*30, 300, 50)

            display_text(f"Attempts Left: {attempt}", 200, 100, 40)
            display_text(f"Round: {round_go}", 550, 100, 40)
            display_text(f"Hint: {hint}", 350, 150, 30)
            pygame.display.flip()
            guess = get_user_guess(num, num2, num3, chosen_one, result, attempt, hint)

            # print(f"\n{attempt} Attempts Left.")
            # guess = input("Enter your guess: \t")
            
            if len(guess) != len(chosen_one):
                # print("Incorrect word entered.\nHint: The word is some food or a country.")
                display_text("Incorrect word length. Try again.", 350, 450, 30)
                pygame.display.flip()
                wait_for_key()
                attempt -= 1
                continue

            result = check_guess(chosen_one, guess, result)
            screen.blit(bgimg, (0, 0))
            transparent_rect = create_transparent_rect(600, 600, (0, 0, 0), 192)  # 75% transparency
            screen.blit(transparent_rect, (50, 50))  # Centered at (50, 50)
            display_text(f"Attempts Left: {attempt}", 200, 100, 40)
            display_text(f"Round: {round_go}", 550, 100, 40)
            for i in range(len(result)):
                display_text(result[i], 200+ i*30, 300, 50)
            pygame.display.flip()

            # screen.blit(bgimg, (0, 0))
            # print(f"Result: {result}")

            if ''.join(result).upper() == chosen_one.upper():
                # print(f"Congratulations! You've guessed the word!\t{chosen_one.upper()}")
                display_text(f"Congratulations! You've guessed the word: {chosen_one.upper()}", 350, 450, 30)
                cleared = True
                pygame.display.flip()
                wait_for_key()
                break
            
            display_text("Incorrect Guess! Try Again.", 350, 420, 30)
            display_text(f"Hint: {hint}", 350, 150, 30)
            pygame.display.flip()
            wait_for_key()

            attempt -= 1

        if not cleared: 
            screen.blit(bgimg, (0, 0))
            transparent_rect = create_transparent_rect(600, 600, (0, 0, 0), 192)  # 75% transparency
            screen.blit(transparent_rect, (50, 50))  # Centered at (50, 50)
            transparent_rect2 = create_transparent_rect(500, 100, (0, 75, 0), 230)
            screen.blit(transparent_rect2, (100, 500)) 
            display_text(f"Attempts Left: {attempt}", 200, 100, 40)
            display_text(f"Round: {round_go}", 550, 100, 40)
            display_text(guess, 350, 550, 50)

            for i in range(len(chosen_one)):
                display_text(result[i], 200+ i*30, 300, 50)

            # print(f"You've run out of attempts. The word was: {chosen_one}")
            display_text("You've run out of attempts.", 350, 420, 30)
            display_text(f"The word was: {chosen_one}", 350, 450, 30)
            pygame.display.flip()
            wait_for_key()



play_game()
