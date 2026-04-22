"""CS50 File Extensions

This program prompts the user for a filename and outputs the corresponding 
media type (MIME type) based on the file's extension.

Python concepts highlighted:
- String manipulation (strip, lower, rpartition)
- Conditional logic (if/elif/else)
- Slicing and list indexing
"""


def check_extension(text):
    """Checks the filename extension and prints its media type.
    
    Args:
        text (str): The user's filename.
    """
    # Prep string
    clean_text = text.strip().lower()
    # Split string
    file_split = clean_text.rpartition('.')
    # Check extension and print media type
    if file_split[-1] == 'jpeg' or file_split[-1] == 'jpg':
        print(f"image/jpeg")
    elif file_split[-1] == 'png' or file_split[-1] == 'gif':
        print(f"image/{file_split[-1]}")
    elif file_split[-1] == 'pdf' or file_split[-1] == 'zip':
        print(f"application/{file_split[-1]}")
    elif file_split[-1] == 'txt':
        print("text/plain")
    else:
        print('application/octet-stream')


def main():
    """Run the main program to prompt the user for a file name."""
    filename = input("File name: ")
    check_extension(filename)


if __name__ == '__main__':
    main()
