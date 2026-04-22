"""
Adding fuctions to the mix in CS50P
"""


def convert(text):
    """ This function looks for the designated emoticons and converts them
    to emojis.
    param: text: Text str to be converted
    return:emojied_text: str to return
    """
    emojied_text = text.replace(":)", '🙂')
    emojied_text = emojied_text.replace(":(", '🙁')
    return emojied_text


def main():
    """ Main program loop"""
    text = input(
        "Please enter a few words or a line of textincluding some old school emoticons ")
    updated_text = convert(text)
    print(updated_text)


if __name__ == '__main__':
    main()
