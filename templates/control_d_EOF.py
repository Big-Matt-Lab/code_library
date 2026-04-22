"""EOFError Handling Template

Adding an EOFError catch routine for user termination of a program 
with Ctrl-D.

Python concepts highlighted:
- Exception handling (try/except blocks)
- Infinite loops (while True)
"""

def main():
    """Run the main program loop handling EOFError for user termination."""
    # Main program
    while True:
        try:
            # Get user input
            name = input("Prompt: ") # Check prompt
        # Check for user termination(ctrl-d)
        except EOFError:
            print() # IMPORTANT when using ctrl-d move to new line
            break
