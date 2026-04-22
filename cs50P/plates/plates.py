"""CS50 Vanity Plates

This program prompts the user for a vanity license plate and checks 
whether it meets the required validity criteria.

Python concepts highlighted:
- String length checking (len)
- String methods (isalnum, isalpha, isnumeric)
- String slicing
- State tracking using flags
- Iteration (for loop)
"""


def is_valid(s):
    """Validate plate using mandated criterion.
    
    Args:
        s (str): The proposed vanity plate.
        
    Returns:
        bool: True if the plate is allowed, False if disqualified.
    """
    # Check length of proposed plate
    if len(s) < 2 or len(s) > 6:
        return False
    # Check for invalid characters
    if not s.isalnum():
        return False
    # Check for numerical characters in first two places
    if not s[0:2].isalpha():
        return False
    num_flag = 0
    for character in s:
        # Check for '0' as first numeric character
        if character == '0' and num_flag == 0:
            return False
        # Check for alpha character after numeric characters
        if character.isnumeric():
            num_flag = 1
        if character.isalpha() and num_flag == 1:
            return False
    return True


def main():
    """Run the main program to prompt the user and print the validation result."""
    # Get user plate
    plate = input("Plate: ")
    # Print results
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == '__main__':
    main()
