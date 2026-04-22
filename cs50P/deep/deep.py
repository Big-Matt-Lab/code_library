"""CS50 Deep Thought

This program asks the user for the answer to the Great Question of Life, 
the Universe, and Everything, and checks if their response matches "42" 
or its word equivalents.

Python concepts highlighted:
- Conditional logic (if/else)
- String manipulation (strip, lower)
- Logical operators (or)
"""


def check_answer(text):
    """Checks the user's response to the Great Question.
    
    Args:
        text (str): The user's answer to the question.
    """
    if text.strip() == '42' or text.lower() == 'forty-two' or text.lower() == 'forty two':
        print('Yes')
    else:
        print('No')


def main():
    """Run the main program to prompt the user and evaluate their answer."""
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    check_answer(answer)


if __name__ == '__main__':
    main()
