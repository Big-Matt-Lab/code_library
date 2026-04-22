"""
Making change using a greedy algorithm
This is a C program rewritten in Python
for cs50, 2026, Problem Set 6
"""


def calculate_coins(cents, coin, value):
    """ Calculate how many coins you should give customer

    :param cents: The remaining change
    :param coin: The coin that was passed in the function call
    :param value: The value of the passed coin
    :return: The number of coins needed
    """
    while (cents >= value):

        coin += 1
        cents = cents - value

    return coin


def main():

    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    print("\nLet's figure out your change in the fewest amount of coins possible.")
    # Get user's input with type enforcement
    while True:
        try:
            change = float(
                input("How much change do you need in dollars (i.e. 9.50, 1.33, or 0.91, etc.): "))
            if change >= 0:
                break
            else:
                print('Invalid response. Please try again.')
        except ValueError:
            print('Invalid response. Please try again.')
    # Convert to cents and round to avoid fractional cents
    change = round(change * 100)
    if change >= 25:
        quarters = calculate_coins(change, quarters, 25)
        change = change % 25
    if change >= 10:
        dimes = calculate_coins(change, dimes, 10)
        change = change % 10
    if change >= 5:
        nickels = calculate_coins(change, nickels, 5)
        change = change % 5
    if change > 0:
        pennies = calculate_coins(change, pennies, 1)

    total = quarters + dimes + nickels + pennies
    # Print results
    print(f"\nQuarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}\n")
    print(f"{total}\n")


if __name__ == "__main__":
    main()
