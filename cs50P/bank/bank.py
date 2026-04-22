"""CS50 Bank

This program prompts the user for a greeting and determines a monetary 
payout based on whether the greeting starts with "hello", "h", or 
something else.

Python concepts highlighted:
- String manipulation (strip, lower, startswith)
- Conditional logic (if/elif/else)
"""


def check_greeting(text):
    """Checks the user's greeting response and evaluates the payout.
    
    Args:
        text (str): The user's greeting.
    """
    clean_text = text.strip().lower()
    if clean_text.startswith('hello'):
        print('$0')
    elif clean_text.startswith('h'):
        print('$20')
    else:
        print('$100')


def main():
    """Run the main program to prompt the user for a greeting."""
    answer = input("Greeting: ")
    check_greeting(answer)


if __name__ == '__main__':
    main()
