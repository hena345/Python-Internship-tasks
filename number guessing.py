# Task 3: Number Guessing Game

import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("\nI'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

def main():
    print("=== Number Guessing Game ===")
    while True:
        play_game()
        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
