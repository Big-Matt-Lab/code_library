"""CS50P Playback Speed

This program slows down a user's inputted text by replacing all spaces
with ellipses (...), simulating a slower playback speed.

Python concepts highlighted:
- Standard input/output operations
- String manipulation (replace)
"""

# Get user input
text = input(
    "Please enter a few words or a line of text. Include mixed characters such as Caps, numbers, and puctuation: ")
# Use .replace function to replaces spaces with '...'
low_text = text.replace(' ', '...')
# Print spaced text
print(low_text)
