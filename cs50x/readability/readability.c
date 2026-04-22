// Written word grading

#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int l_counter(string text);
int w_counter(string text);
int s_counter(string text);
int grading(int letter_count, int word_count, int sentence_count);

int main(void)
{
    // Prompt the user for input
    string text = get_string("Player 1 enter a word: \n");

    // Call function to count
    int letter_count = l_counter(text);
    int word_count = w_counter(text);
    int sentence_count = s_counter(text);

    // Print results
    int score = grading(letter_count, word_count, sentence_count);
    if (score < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (score > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %d\n", score);
    }
}
int l_counter(string text)
{
    // Keep track of score
    int l_count = 0;

    // Count letters.
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        // Ignores numbers and punctuation
        if (isalpha(text[i]))
        {
            l_count += 1;
        }
    }
    return l_count;
}
int w_counter(string text)
{
    // Keep track of score
    int w_count = 0;

    // Count words.
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        // Ignores numbers and punctuation
        if (text[i] == ' ')
        {
            w_count += 1;
        }
    }
    return w_count + 1;
}
int s_counter(string text)
{
    // Keep track of score
    int s_count = 0;

    // Count sentences.
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        // Ignores numbers and punctuation
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            s_count += 1;
        }
    }
    return s_count;
}
int grading(int letter_count, int word_count, int sentence_count)
{
    double l = (double) letter_count / word_count * 100;
    double s = (double) sentence_count / word_count * 100;
    double grade = 0.0588 * l - 0.296 * s - 15.8;
    int rounded_grade = round(grade);
    return rounded_grade;
}
