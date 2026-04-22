"""CS50 Emojize

This program prompts the user for a string of text and converts any 
emoji aliases or codes within the string into actual emojis.

Python concepts highlighted:
- Third-party library integration (emoji module)
- String manipulation (strip, lower)
- Standard __main__ execution block
"""

# Import the necessary module
from emoji import emojize


def main():
    """Run the main emojize program.
    
    Prompts the user for a text string, processes it to lowercase
    and removes whitespace, then converts alias codes to emojis and prints.
    """
    # Main program
    # Get user message
    user_str = input("Input: ")
    # Clean and split into a list
    message = user_str.strip().lower()
    # Convert to emoji
    message_emo = emojize(message, language='alias')
    # Print output
    print(f"Output: {message_emo}")
    # End of program


if __name__ == '__main__':
    main()
# EOF
