# A simple number guessing game which continues until the user is able to guess the correct number
import random

def random_int():
    return random.randint(0, 10)

def guess_num():
    while True:
        try:
            n = int(input("Guess the Number (between 0 & 10): "))
            if 0 <= n <= 10 :
                return n
            else: 
                print("Please enter a number between 0 and 10...")
        except ValueError:
            print("Invalid Input!!! Please enter a valid integer...")

def play_game():
    random_num = random_int()
    attempt = 0
    while True:
        user_num = guess_num()
        attempt += 1
        if user_num == random_num: 
            print("\t\tCongratulations!!! You guessed it correct !!!")
            print(f"\t\tThe correct number was {random_num}")
            print(f"\t\tAttempts made: {attempt}")
            break
        else:
            print("\t\tSorry!! You guessed it wrong...\n\t\t\t...Try Again...")
            print(f"\t\tAttempts made: {attempt}")
play_game()
