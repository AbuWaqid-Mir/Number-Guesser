import random
import time

def intro():
    # Create a title using ASCII
    print("""
  _   _                 _                  ____                               
 | \ | |_   _ _ __ ___ | |__   ___ _ __   / ___|_   _  ___  ___ ___  ___ _ __ 
 |  \| | | | | '_ ` _ \| '_ \ / _ \ '__| | |  _| | | |/ _ \/ __/ __|/ _ \ '__|
 | |\  | |_| | | | | | | |_) |  __/ |    | |_| | |_| |  __/\__ \__ \  __/ |   
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \____|\__,_|\___||___/___/\___|_|   
                                                                              
    """)
    guesses = 0
    print("Welcome to the Number Guesser")
    time.sleep(1) # delay the program by 1 second
    print("I will randomly generate a number between 1 and 100")
    time.sleep(1)
    print("And you will have to guess it")
    time.sleep(1)
    print("I will give you hints by saying that your guess is too high or too low")
    time.sleep(1)
    return guesses

def main(guesses):
    rand_num = random.randint(1, 100)
    user_guess = int(input("Guess my number from the range 1-100: "))
    while user_guess != rand_num:
        if user_guess > rand_num:
            print("Your number is too high")
        elif user_guess < rand_num:
            print("Your number is too low")
        guesses += 1
        user_guess = int(input("Guess my number from the range 1-100: "))
    if user_guess == rand_num:
        guesses += 1
        print("Well Done, you guessed it!")
        time.sleep(1)
        print("You took", guesses, "guesses")

guesses = intro()
main(guesses)