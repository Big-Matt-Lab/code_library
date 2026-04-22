"""CS50 Credit Card Validator

This program prompts the user for a credit card number and validates it.
It first checks if the input is a valid 13-16 digit sequence, then verifies
the number's checksum using Luhn's Algorithm. Finally, it identifies the
card brand (VISA, MASTERCARD, AMEX) based on the starting digits and length.

Python concepts highlighted in this program:
- Regular expressions (re module) for input validation
- List comprehensions and list slicing (e.g., reversing lists)
- Iteration and enumeration (for, while, enumerate)
- String slicing and manipulation
- Arithmetic operations (modulo % and integer division //)
- Conditional logic and membership testing (in)
- Standard __main__ execution block
"""
import re

def get_number():
    """Prompt the user for a credit card number and validate its format.

    Loops until a string containing 13 to 16 digits is entered.

    Returns:
        str: The validated credit card number as a string.

    """
    pattern = r"^[0-9]{13,16}$"
    while True:
        user_input = input("Number: ").strip()
        if re.fullmatch(pattern, user_input):
            return user_input
        print("Invalid format. Please enter 13-16 digits.")

def is_valid_luhn(num_str):
    """Perform Luhn's Algorithm to check for card number validity.

    Args:
        num_str (str): The card number as a string of digits.

    Returns:
        bool: True if the number is valid according to Luhn's algorithm,
              False otherwise.

    """
    digits = [int(d) for d in num_str]
    # Reverse the digits to work from right to left
    check_digits = digits[::-1]
    
    total_sum = 0
    for i, digit in enumerate(check_digits):
        if i % 2 == 1:
            product = digit * 2
            # Sum the digits of the product (e.g., 12 -> 1 + 2)
            total_sum += (product // 10) + (product % 10)
        else:
            total_sum += digit
            
    return total_sum % 10 == 0

def get_brand(num_str):
    """Determine the card brand from the card number.

    Identifies the brand (AMEX, MASTERCARD, VISA) based on the number's
    length and starting digits.

    Args:
        num_str (str): The card number as a string of digits.

    Returns:
        str: The card brand as a string ("AMEX", "MASTERCARD", "VISA"),
             or "INVALID" if no known brand is matched.
    """
    length = len(num_str)
    first_two = int(num_str[:2])
    first_one = int(num_str[0])

    if first_one == 4 and length in (13, 16):
        return "VISA"
    if length == 15 and first_two in (34, 37):
        return "AMEX"
    if length == 16 and 51 <= first_two <= 55:
        return "MASTERCARD"
    
    return "INVALID"

def main():
    """Run the main credit card validation program.

    Orchestrates the process of getting a card number from the user,
    validating it with Luhn's algorithm, and identifying and printing
    the card brand.
    """
    # 1. Get Input
    card_number = get_number()
    
    # 2. Validate Checksum
    if not is_valid_luhn(card_number):
        print("INVALID (Checksum failed)")
        return

    # 3. Identify and Print Brand
    brand = get_brand(card_number)
    print(brand)

if __name__ == "__main__":
    main()