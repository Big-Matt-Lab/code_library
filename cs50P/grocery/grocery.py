"""CS50P Grocery List

This program allows the user to input grocery items one per line.
It tallies the items using a dictionary and, upon termination via EOF (Ctrl-D),
outputs the sorted list of items in uppercase along with their quantities.

Python concepts highlighted:
- Dictionaries for frequency counting
- Exception handling (try/except for KeyError and EOFError)
- Sorting collections
- String manipulation (strip, lower, upper)
"""
# Create empty dictionary
grocery_list = {}


def add_to_list(item):
    """Adds an item to the grocery list or increments its count.

    Args:
        item (str): The item to be added or incremented on our list.
    """
    try:
        # Increment entry
        grocery_list[item] += 1
    except KeyError:
        # Initial entry
        grocery_list[item] = 1


def output_list():
    """Prints the formatted and sorted grocery list.

    Iterates over the sorted dictionary items and prints the
    count and uppercase name of each grocery item.
    """

    for key, value in sorted(grocery_list.items()):
        print(f"{value} {key.upper()}")


def main():
    # Main program code
    pass
    while True:
        try:
            product = input()
        # Check for user termination(ctrl-d)
        except EOFError:
            print()
            break
        item = product.strip().lower()
        add_to_list(item)
    # Upon break, output list and terminate
    output_list()


if __name__ == '__main__':
    main()
