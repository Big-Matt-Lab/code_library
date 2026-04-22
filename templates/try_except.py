"""Exception Handling Template

Basic Try / Except block to catch and handle various errors.

Python concepts highlighted:
- Exception handling (try/except blocks)
- Input validation
"""


def main():
    """Run the main program loop demonstrating basic try/except usage."""
    while True:
            try:
                user_input = int(input("Prompt: ")) # Check prompt, Check type
                break

            except ValueError:
                # Action
