# LAST STEP - Organise the timing

import random
import time

# Displays the game's introduction & starts the difficulty selection
def intro():
    time.sleep(1) # delay the program by 1 second
    print("""
##### NUMBER GUESSER ###################################################################################################
    """)
    time.sleep(1)
    print("Welcome to the Number Guesser")
    time.sleep(1)
    print("I will randomly generate a number between a selected range")
    time.sleep(1)
    print("You will have a specific amount of guesses")
    time.sleep(1)
    print("I will give you hints by saying that your guess is too high or too low")
    time.sleep(1)
    difficulty_selection() # call the difficulty_selection() function

# Allow the player to choose a difficulty level
def difficulty_selection():
    time.sleep(1)
    print("""
##### DIFFICULTY LEVEL SELECTION #######################################################################################
        """)
    time.sleep(1)
    print("You have 3 difficulty levels to choose from:")
    time.sleep(0.5)
    print("1. Easy")
    time.sleep(0.5)
    print("2. Medium")
    time.sleep(0.5)
    print("3. Hard")
    # Select a difficulty level based on what number the player enters
    while True:
        try:
            time.sleep(1)
            choice = int(input("Choose your difficulty - 1, 2 or 3: "))
            if choice == 1:
                print("You have selected EASY - please wait...")
                time.sleep(1)
                easy_difficulty()
                break
            elif choice == 2:
                print("You have selected MEDIUM - please wait...")
                time.sleep(1)
                medium_difficulty()
                break
            elif choice == 3:
                print("You have selected HARD - please wait...")
                time.sleep(1)
                hard_difficulty()
                break
            else:
                print("Please choose 1, 2 or 3")
        except ValueError:
            print("Invalid input - must select an existing difficulty")

# Runs the easy difficulty game mode
def easy_difficulty():
    time.sleep(1)
    print("""
##### Level - EASY #####################################################################################################
        """)
    time.sleep(1)
    print("You will have 5 chances to guess my number")
    time.sleep(1)
    print("Guess my number, and you WIN!")
    time.sleep(1)
    print("However, if you fail to guess my number, you LOSE...")
    guesses = 0
    max_guesses = 5
    rand_num = random.randint(1, 50)
    while True: # keeps asking until the player wins/runs out of guesses
        try:
            time.sleep(1)
            user_guess = int(input("Guess my number from the range 1-50: "))
            # Check if the guess is within the allowed range
            if user_guess < 1 or user_guess > 50:
                print("Your guess must be between 1 and 50")
                time.sleep(1)
                continue
            while user_guess != rand_num:
                if user_guess > rand_num:
                    time.sleep(0.5)
                    print("Your number is too high")
                elif user_guess < rand_num:
                    time.sleep(0.5)
                    print("Your number is too low")
                guesses += 1
                if guesses == max_guesses:
                    print("You have run out of guesses")
                    print("The correct number was", rand_num)
                    return
                time.sleep(0.5)
                user_guess = int(input("Guess my number from the range 1-50: "))
                if user_guess < 1 or user_guess > 50:
                    print("Your guess must be between 1 and 50")
                    time.sleep(1)
                    continue
            if user_guess == rand_num:
                guesses += 1
                print("Well Done, you guessed it!")
                time.sleep(0.5)
                print("You took", guesses, "guesses")
                break
        except ValueError:
            time.sleep(1)
            print("Invalid input - input must be an integer")

# Runs the medium difficulty game mode
def medium_difficulty():
    time.sleep(1)
    print("""
##### Level - MEDIUM #####################################################################################################
        """)
    time.sleep(1)
    print("You will have 8 chances to guess my number")
    time.sleep(1)
    print("Guess my number, and you WIN!")
    time.sleep(1)
    print("However, if you fail to guess my number, you LOSE...")
    time.sleep(1)
    guesses = 0
    max_guesses = 8
    rand_num = random.randint(1, 100)
    while True: # keeps asking until the player wins/runs out of guesses
        try:
            user_guess = int(input("Guess my number from the range 1-100: "))
            # Check if the guess is within the allowed range
            if user_guess < 1 or user_guess > 100:
                print("Your guess must be between 1 and 100")
                time.sleep(1)
                continue
            while user_guess != rand_num:
                if user_guess > rand_num:
                    time.sleep(0.5)
                    print("Your number is too high")
                elif user_guess < rand_num:
                    time.sleep(0.5)
                    print("Your number is too low")
                guesses += 1
                if guesses == max_guesses:
                    print("You have run out of guesses")
                    print("The correct number was", rand_num)
                    return
                time.sleep(0.5)
                user_guess = int(input("Guess my number from the range 1-100: "))
                if user_guess < 1 or user_guess > 100:
                    print("Your guess must be between 1 and 100")
                    time.sleep(1)
                    continue
            if user_guess == rand_num:
                guesses += 1
                print("Well Done, you guessed it!")
                time.sleep(0.5)
                print("You took", guesses, "guesses")
                break
        except ValueError:
            time.sleep(1)
            print("Invalid input - input must be an integer")

# Runs the hard difficulty game mode
def hard_difficulty():
    time.sleep(1)
    print("""
##### Level - HARD #####################################################################################################
        """)
    time.sleep(1)
    print("You will have 12 chances to guess my number")
    time.sleep(1)
    print("Guess my number, and you WIN!")
    time.sleep(1)
    print("However, if you fail to guess my number, you LOSE...")
    time.sleep(1)
    guesses = 0
    max_guesses = 12
    rand_num = random.randint(1, 150)
    while True: # keeps asking until the player wins/runs out of guesses
        try:
            user_guess = int(input("Guess my number from the range 1-150: "))
            # Check if the guess is within the allowed range
            if user_guess < 1 or user_guess > 150:
                print("Your guess must be between 1 and 150")
                time.sleep(1)
                continue
            while user_guess != rand_num:
                if user_guess > rand_num:
                    time.sleep(0.5)
                    print("Your number is too high")
                elif user_guess < rand_num:
                    time.sleep(0.5)
                    print("Your number is too low")
                guesses += 1
                if guesses == max_guesses:
                    print("You have run out of guesses")
                    print("The correct number was", rand_num)
                    return
                time.sleep(0.5)
                user_guess = int(input("Guess my number from the range 1-150: "))
                if user_guess < 1 or user_guess > 150:
                    print("Your guess must be between 1 and 150")
                    time.sleep(1)
                    continue
            if user_guess == rand_num:
                guesses += 1
                print("Well Done, you guessed it!")
                time.sleep(0.5)
                print("You took", guesses, "guesses")
                break
        except ValueError:
            time.sleep(1)
            print("Invalid input - input must be an integer")

intro()