"""CS50P Vowel Remover (Twttr)

This program prompts the user for a string of text and outputs that
same text with all vowels (A, E, I, O, and U) removed, maintaining 
original case, numbers, and punctuation.

Python concepts highlighted:
- Sets and membership testing (in / not in)
- String manipulation (joining lists)
- Iteration over iterables (for loops)
"""


def remove_vowels(message):
    """Removes vowels from a given text string.

    Iterates over each character in the message, checking it against
    an exclusion set of vowels, and removes it if it matches while
    maintaining case, numbers, and punctuation.

    Args:
        message (str): The user string to be processed.

    Returns:
        str: The converted message with all vowels removed.
    """
    # Start with empty list
    exclude = {'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'}
    camel_characters = []
    # Iterate over 'message'
    for character in message:
        # Exclude vowels
        if character not in exclude:
            camel_characters.append(character)
    # List is joined
    return "".join(camel_characters)


def main():
    """Main program loop.

    Prompts the user for a string, processes it to remove vowels,
    and prints the resulting string.
    """
    text = input("Input: ")
    converted_text = remove_vowels(text)
    print(f"Output: {converted_text}")


if __name__ == '__main__':
    main()
