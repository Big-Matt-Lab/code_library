"""CS50 Einstein

This program calculates the equivalent energy of a given mass using 
Einstein's formula E = mc^2.

Python concepts highlighted:
- Arithmetic operations (multiplication, exponentiation)
- Type casting (int)
- Functions with return values
"""


def energy(mass):
    """Calculate energy from mass using Einstein's equation.
    
    Args:
        mass (int): User input mass in kilograms.
        
    Returns:
        int: The calculated energy in Joules.
    """
    e = mass * (300000000 ** 2)
    return e


def main():
    """Run the main program loop to retrieve mass and print equivalent energy."""
    mass = int(input("Please enter the mass of an object: "))
    big_e = energy(mass)
    print(f"{big_e} J")


if __name__ == '__main__':
    main()
