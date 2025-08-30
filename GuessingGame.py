# Guess the number game
import random

def num_guessing_game():
    attempts = 0
    level = int(input("\n Enter the difficulty level (1 - easiest, 5 -toughest): "))
    if level==1:
        lower_bound = 1
        upper_bound = 20
        secret_number = random.randint(lower_bound, upper_bound)
        print(f"\n I'm thinking of a number between {lower_bound} and {upper_bound}.")
    elif level==2:
        lower_bound = 1
        upper_bound = 50
        secret_number = random.randint(lower_bound, upper_bound)
        print(f"\n I'm thinking of a number between {lower_bound} and {upper_bound}.")
    elif level==3:
        lower_bound = 1
        upper_bound = 100
        secret_number = random.randint(lower_bound, upper_bound)
        print(f"\n I'm thinking of a number between {lower_bound} and {upper_bound}.")
    elif level==4:
        lower_bound = 1
        upper_bound = 200
        secret_number = random.randint(lower_bound, upper_bound)
        print(f"\n I'm thinking of a number between {lower_bound} and {upper_bound}.")
    elif level==5:
        lower_bound = 1
        upper_bound = 500
        secret_number = random.randint(lower_bound, upper_bound)
        print(f"\n I'm thinking of a number between {lower_bound} and {upper_bound}.")
    else:
        print("\n Invalid Input, try again")
        num_guessing_game()
    while True:
        try:
            guess = int(input("\n Enter your guess: "))
            attempts += 1

            if guess < lower_bound or guess > upper_bound:
                print(f"Please guess a number within the range of {lower_bound} to {upper_bound}.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"\n Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

print("Let's Start the number guessing game!")

num_guessing_game()

i = str(input("\nNew game? (y/n) \n"))
while i=="y":
    num_guessing_game()
    i = str(input("\nNew game? (y/n) \n"))

print("Thank you for playing")