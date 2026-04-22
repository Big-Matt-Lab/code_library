"""CS50P Fuel Gauge

This program prompts the user for a fraction representing a fuel gauge
reading (e.g., X/Y) and calculates the percentage of fuel remaining.
It handles errors such as ValueError and ZeroDivisionError and outputs
'E' for empty, 'F' for full, or the percentage.

Python concepts highlighted:
- Exception handling (try/except)
- String splitting and stripping
- Infinite loops with break conditions (while True)
- Type conversion (int, float)
- String formatting
"""


def convert(one, two):
    """Calculates the percentage from a numerator and denominator.

    Args:
        one (int or float): The numerator.
        two (int or float): The denominator.

    Returns:
        float: The percentage value (numerator / denominator * 100).
    """
    percent = (one / two) * 100
    return percent


def main():
    # Get user input fraction
    while True:
        fraction = input("Fraction(X/Y): ")
        # Clean and split into a list
        break_down = fraction.strip().split('/')
        # Convert to int, catching any error
        try:
            num = int(break_down[0])
            if num < 0:
                continue
            denom = int(break_down[1])
            if num > denom:
                continue
            if denom == 0:
                continue
        except ValueError:
            continue
        break
    percent = convert(num, denom)
    # Print results
    if percent >= 99:
        print("F")
    elif percent <= 1:
        print("E")
    else:
        print("{:.0f}%".format(percent))


if __name__ == '__main__':
    main()
