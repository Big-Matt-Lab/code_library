"""CS50 Felipe's Taqueria

This program enables a user to place an order, prompting them for items,
until the user inputs control-d. After each inputted item, it displays 
the total cost of all items inputted thus far.

Python concepts highlighted:
- Dictionary mapping and lookups
- String manipulation (strip, lower, title)
- Exception handling (try/except for EOFError)
- Infinite iteration (while True)
- String formatting (to 2 decimal places)
"""
# Dict storing menu items
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def main():
    """Run the main program loop to collect orders and tally the total cost."""
    # Get user input of menu selection
    cost = 0
    print("Please enter your menu choices.")
    while True:
        try:
            item = input("Item: ")
        # Check for user termination(ctrl-d)
        except EOFError:
            break
        cleaned_item = item.strip().lower().title()
        # Check that user selection is in menu dict
        if cleaned_item not in menu:
            continue
        # Increment cost
        cost += menu[cleaned_item]
        # Print results
        print(f"Total: ${cost:.2f}")


if __name__ == '__main__':
    main()
