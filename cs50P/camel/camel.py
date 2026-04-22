"""CS50 CamelCase to snake_case

This program converts a variable name from camelCase format into 
snake_case format.

Python concepts highlighted:
- String iteration and enumeration (for, enumerate)
- String methods (isupper, lower, join)
- List operations (append)
"""


def convention_conversion(name):
    """Converts camelCase names to snake_case.
    
    Iterates over each character, checking its case, and converts
    checking it's case, and converting as required including adding
    an underscore where appropriate.
    
    Args:
        name (str): The variable name to be converted.
        
    Returns:
        str: The converted snake_case name.
    """
    # Start with empty list
    camel_characters = []
    # Iterate over 'name'
    for i, character in enumerate(name):
        if i == 0:
            # in case the first character is upper case(or not)
            camel_characters.append(character.lower())
        elif character.isupper():
            # Other upper case characters are converted to lower with an underscore preceding them
            camel_characters.append('_')
            camel_characters.append(character.lower())
        else:
            # All other characters are added to list
            camel_characters.append(character)
    # List is joined
    snake_case = "".join(camel_characters)
    return snake_case


def main():
    """Run the main program to prompt the user and print the conversion."""
    # Main program code
    variable_name = input("Variable name: ")
    converted_name = convention_conversion(variable_name)
    print(converted_name)


if __name__ == '__main__':
    main()
