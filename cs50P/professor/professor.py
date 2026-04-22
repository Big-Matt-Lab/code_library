"""CS50 Little Professor

This program simulates a math learning toy. It prompts the user for a 
difficulty level, generates 10 random addition problems, allows 3 
attempts per problem, and outputs the final score.

Python concepts highlighted:
- Random number generation (random module)
- Exception handling (try/except for ValueError)
- Loop control (for, while, break, continue)
- Custom functions with return values
"""
import random


def main():
    """Run the main program loop to administer the math quiz and tally the score."""
    score = 0
    difficulty_level = get_level()
    # Iterate through creating 10 math addition problems
    for _ in range(10):

        # Get int's for math problems
        x = generate_integer(difficulty_level)
        y = generate_integer(difficulty_level)

        # Allow the user three(3) opportunities to
        # correctly solve the problem
        for _ in range(3):
            try:
                # Present the problem to the user
                answer = int(input(f"{x} + {y} = "))
                # Check for correct
                if answer == x + y:
                    # Increment score if correct
                    score += 1
                    break
                # Wrong answer
                else:
                    # Notify user of wrong answer
                    print("EEE")

            # Error catching
            except ValueError:
                # Notify user of error
                print("EEE")
                continue

        else:
            # Print correct answer
            print(f"{x} + {y} = {x + y}")

    # Print score tally
    print(f"Score: {score}")


def get_level():
    """Get user input to establish the difficulty range of the exercise.
    
    Returns:
        int: A difficulty level chosen by the user (1, 2, or 3).
    """
    while True:
        try:
            level = (input("Level: "))
            if level not in ['1', '2', '3']:
                raise ValueError
            else:
                break

        except ValueError:
            continue
    return int(level)


def generate_integer(level):
    """Randomly generates an integer within the range established by the difficulty level.
    
    Args:
        level (int): The difficulty passed by the get_level function.
        
    Returns:
        int: A randomly generated integer in a specific range.
    """
    range_limit = 0
    range_lower_limit = 0
    if level == 1:
        range_limit = 10
    elif level == 2:
        range_lower_limit = 10
        range_limit = 100
    else:
        range_lower_limit = 100
        range_limit = 1000

    return random.randrange(range_lower_limit, range_limit)


if __name__ == "__main__":
    main()
