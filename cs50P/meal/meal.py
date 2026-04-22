"""CS50 Meal Time

This program prompts the user for a time and outputs whether it is 
breakfast time, lunch time, or dinner time based on specified ranges.

Python concepts highlighted:
- String manipulation (strip, lower, split)
- Type casting (float)
- Conditional logic (if/elif)
- Math operations
"""


def convert(text):
    """Converts a time string to a float.
    
    Args:
        text (str): Time expressed as a string (e.g., "7:30").
        
    Returns:
        float: The time converted to a decimal float.
    """
    # Prep string
    clean_text = text.strip().lower()
    # Split string
    x, y = clean_text.split(":")
    x = float(x)
    y = float(y)
    y = y / 60
    z = x + y
    return z


def main():
    """Run the main program loop to prompt for time and evaluate the meal period."""
    clock = input("What time is it? ")
    hour = convert(clock)
    # Check expression and return meal period
    if 7.00 <= hour <= 8.00:
        print("breakfast time")
    elif 12.00 <= hour <= 13.00:
        print("lunch time")
    elif 18.00 <= hour <= 19.00:
        print("dinner time")


if __name__ == '__main__':
    main()
