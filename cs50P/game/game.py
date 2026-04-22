"""CS50P Guessing Game

This program implements a simple number guessing game. It prompts the
user for an upper bound to set the difficulty level, generates a random
number, and then gives hints until the user guesses correctly.

Python concepts highlighted:
- Random number generation (random.randint)
- Exception handling (ValueError)
- Infinite loops with breaking conditions
- Input validation and type casting
"""

import random


def configure_game():
    """Establishes the high limit and generates the secret number.

    Prompts the user repeatedly until a valid positive integer is entered
    to serve as the upper bound.

    Returns:
        tuple: A tuple containing:
            - int: The randomly generated secret number.
            - int: The validated upper bound limit.
    """
    while True:
        try:
            maximum = int(input("Level: "))
            if maximum > 0:
                break

        except ValueError:
            continue

    number = random.randint(1, maximum)
    return number, maximum


def get_user_guess(high_limit):
    """Prompts the user for a guess and validates that it is a positive integer.

    Args:
        high_limit (int): The upper bound of the guessing range.

    Returns:
        int: The validated user guess.
    """

    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                continue
            else:
                break
        except ValueError:
            continue
    return guess


def main():
    """
    Main game loop. Orchestrates the game flow, and win/loss conditions.
    """
    number, limit = configure_game()
    while True:
        guess = get_user_guess(limit)
        if guess == number:
            print("Just right!")
            break
        elif guess < number:
            print("Too small!")
        else:
            print("Too large!")


if __name__ == "__main__":
    main()
