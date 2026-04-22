""" CS50P Tip calculator implemented with functions
to keep the code modular
"""


def main():
    """
    Main program loop
    """
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    """
    Converts 'd' str input to float while stripping off the leading '$' character if present
    param: d: str - cost of meal
    return: meal: cost of meal as clean float
    """
    d = d.strip('$')
    meal = float(d)
    return meal


def percent_to_float(p):
    """
    Converts 'p' str input to float while stripping off trailing '%' character if present
    param: p: str - tip percentage
    return: t: tip percent as clean float 
    """
    p = p.strip('%')
    t = float(p) / 100
    return t


if __name__ == '__main__':
    main()
