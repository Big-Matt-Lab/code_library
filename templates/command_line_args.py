"""Command Line Arguments Template

Boilerplate code to evaluate and handle command line arguments.

Python concepts highlighted:
- Command line argument evaluation (sys.argv)
- System exit (sys.exit)
"""



def main():
    """Run the main program to evaluate command line arguments."""
    # Main program
    # Check for command line args
    if len(sys.argv) == 1:
        pass
    # Check for correct number of command line args
    elif len(sys.argv) != 3:
        sys.exit()

    # End of program


if __name__ == '__main__':
    main()
