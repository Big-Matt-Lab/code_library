"""CS50 Coke Machine

This program simulates a vending machine that dispenses a bottle of coke 
for 50 cents, accepting only 25, 10, and 5 cent coins, and calculating 
the change owed.

Python concepts highlighted:
- Iteration (while loops)
- Conditional logic (if/elif)
- Membership testing (in list)
- Arithmetic operations (subtraction, absolute value)
"""


def main():
    """Run the main program simulating the coke machine coin insertion."""
    # Main program code
    coke = 50
    amount_due = coke
    while amount_due >= 0:
        # Get coin inserted
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert coin: "))
        # Coin validation
        if coin not in [5, 10, 25]:
            continue
        amount_due = amount_due - coin
        # Over payment, offer change and exit
        if amount_due < 0:
            change = abs(amount_due)
            print(f"Change Owed: {change}")
        # Completed sale, exit
        elif amount_due == 0:
            print("Change Owed: 0")
            break


if __name__ == '__main__':
    main()
