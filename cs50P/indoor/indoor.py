"""CS50P Indoor Voice

This program takes user input containing mixed case characters, numbers,
and punctuation, and converts all alphabetical characters to lowercase,
simulating an "indoor voice."

Python concepts highlighted:
- Basic standard input/output (input, print)
- String manipulation (lower)
"""

# Get user input
text = input(
    "Please enter a few words or a line of text. Include mixed characters such as Caps, numbers, and puctuation: ")
# Use '.lower' function to change all alphabetical text to lowercase
low_text = text.lower()
# Print lowercasde text
print(low_text)
