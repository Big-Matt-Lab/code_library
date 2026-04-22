"""CS50P Frank, Ian and Glen's Letters (Figlet)

This program takes user input and outputs it in a large ASCII art font
using the pyfiglet library. It supports random font selection or a
user-specified font via command-line arguments.

Python concepts highlighted:
- Command-line arguments (sys.argv)
- Third-party modules (pyfiglet)
- Random choice (random module)
- Exiting with error messages (sys.exit)
"""

from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
font_list = figlet.getFonts()


def random_font():
    """Displays user input using a randomly selected font.

    Prompts the user for text, selects a random font from the
    available Figlet fonts, and prints the rendered text.
    """
    message = get_user_input()
    output_font = random.choice(font_list)
    figlet.setFont(font=output_font)
    print(figlet.renderText(message))
    return


def defined_font():
    """Displays user input using a specified font from command-line arguments.

    Validates the requested font against the available fonts. Exits
    if the font is invalid, otherwise prompts for input and renders it.
    """
    if sys.argv[2] not in font_list:
        sys.exit("Invalid usage")
    else:
        message = get_user_input()
        output_font = sys.argv[2]
        figlet.setFont(font=output_font)
        print(figlet.renderText(message))
        return


def get_user_input():
    """Prompts the user for a string to display.

    Returns:
        str: The user's input string.
    """
    user_str = input("Input: ")
    return user_str


def main():
    # Main program
    # Check for command line args
    if len(sys.argv) == 1:
        # Use random font with no user specified font
        random_font()
    # Check for correct number of command line args
    elif len(sys.argv) != 3:
        sys.exit("Invalid usage")
    # Check for correct usage
    elif sys.argv[1] not in ['-f', ' --font']:
        sys.exit("Invalid usage")
    else:
        defined_font()
    # End of program


if __name__ == '__main__':
    main()
