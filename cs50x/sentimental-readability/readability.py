

def l_counter(text):

    # Keep track of score
    l_count = 0

    # Count letters.
    for i in range(len(text)):

        # Ignores numbers and punctuation
        if text[i].isalpha():

            l_count += 1

    return l_count


def w_counter(text):

    # Keep track of score
    w_count = 0

    # Count words.
    for i in range(len(text)):

        # Ignores numbers and punctuation
        if (text[i] == ' '):

            w_count += 1

    return w_count + 1


def s_counter(text):

    # Keep track of score
    s_count = 0

    # Count sentences.
    for i in range(len(text)):

        # Ignores numbers and punctuation
        if text[i] == '.' or text[i] == '!' or text[i] == '?':

            s_count += 1

    return s_count


def grading(letter_count, word_count, sentence_count):

    l = letter_count / word_count * 100
    s = sentence_count / word_count * 100
    grade = 0.0588 * l - 0.296 * s - 15.8
    rounded_grade = round(grade)
    return rounded_grade


def main():

    # Prompt the user for input
    text = input("Player 1 enter a word: ")

    # Call function to count
    letter_count = l_counter(text)
    word_count = w_counter(text)
    sentence_count = s_counter(text)

    # Pr results
    score = grading(letter_count, word_count, sentence_count)
    if (score < 1):

        print("Before Grade 1")

    elif score > 16:

        print("Grade 16+")

    else:

        print("Grade", score)


if __name__ == "__main__":
    main()
