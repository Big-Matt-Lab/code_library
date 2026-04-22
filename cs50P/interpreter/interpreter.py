"""CS50P Math Interpreter

This program prompts the user for a basic arithmetic expression
(in the format 'x y z') and calculates the result. It acts as a
simple interpreter for addition, subtraction, multiplication, and division.

Python concepts highlighted:
- String splitting and formatting
- Conditional logic (if/elif/else statements)
- Type conversion (float)
"""


def check_expression(text):
    """Evaluates a mathematical equation expressed as a string.

    Args:
        text (str): The mathematical expression to evaluate (e.g., '1 + 1').

    Returns:
        float: The numerical result of the evaluated expression.
    """
    # Prep string
    clean_text = text.strip().lower()
    # Split string
    x, y, z = clean_text.split(" ")
    x = float(x)
    z = float(z)
    # Check expression and return solution
    if y == '+':
        return x + z
    if y == '-':
        return x - z
    if y == '*':
        return x * z
    if y == '/':
        return x / z


def main():
    expression = input("Expression: ")
    solution = check_expression(expression)
    print(f"{solution:.1f}")


if __name__ == '__main__':
    main()
