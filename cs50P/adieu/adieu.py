"""CS50 Adieu

This program prompts the user for names until an EOFError is raised
(Ctrl-D), then prints a grammatically correct farewell using the 
inflect library to join the names.

Python concepts highlighted:
- Exception handling (try/except blocks)
- Indefinite iteration (while True)
- Third-party library usage (inflect)
- List manipulation
"""

import inflect

p = inflect.engine()


def main():
    """Run the main program loop to collect names and output the farewell."""
    # Main program
    name_list = []
    while True:
        try:
            # Get user input
            name = input("Name: ")
            # Add name to list
            name_list.append(name)
        # Check for user termination(ctrl-d)
        except EOFError:
            print() # IMPORTANT when using ctrl-d move to new line
            break
    # Use join from inflect to format list
    names = p.join(name_list)
    # Output formatted name list
    print(f"Adieu, adieu, to {names}")
    # End of program


if __name__ == '__main__':
    main()
