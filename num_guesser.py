import random
import time

def intro():
    # Create a title using ASCII
    print("""
##### NUMBER GUESSER ######
    """)
    time.sleep(1)
    print("Welcome to the Number Guesser")
    time.sleep(1) # delay the program by 1 second
    print("I will randomly generate a number between 1 and 100")
    time.sleep(1)
    print("And you will have to guess it")
    time.sleep(1)
    print("I will give you hints by saying that your guess is too high or too low")
    time.sleep(1)

def main():
    guesses = 0
    rand_num = random.randint(1, 100) # generate a random integer in 1-100 range
    while True:
        try:
            user_guess = int(input("Guess my number from the range 1-100: ")) # user input
            while user_guess != rand_num:
                    if user_guess > rand_num:
                        print("Your number is too high")
                    elif user_guess < rand_num:
                        print("Your number is too low")
                    guesses += 1 # 1 will be added to the guesses variable
                    user_guess = int(input("Guess my number from the range 1-100: "))
            if user_guess == rand_num:
                guesses += 1
                print("Well Done, you guessed it!")
                time.sleep(0.5)
                print("You took", guesses, "guesses")
                break
        except ValueError:
            print("Invalid input - input must be an integer")

intro()
main()