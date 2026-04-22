
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int scoring(string word);

int main(void)
{
    // Prompt the user for input
    string userWord1 = get_string("Player 1 enter a word: \n");
    string userWord2 = get_string("Player 2 enter a word: \n");

    // Call function to determine score
    int score1 = scoring(userWord1);
    int score2 = scoring(userWord2);

    // Print results
    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score2 > score1)
    {
        printf("Player 2 wins!\n");
    }
    else
    {
        printf("It's a tie!\n");
    }
}

int scoring(string word)
{
    // Keep track of score
    int score = 0;
    int LETTER_VALUES[] = {1, 3, 3, 2,  1, 4, 2, 4, 1, 8, 5, 1, 3,
                           1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    // Compute score for each character and add to total
    for (int i = 0, len = strlen(word); i < len; i++)
    {
        // Ignores numbers and punctuation
        if (isalpha(word[i]))
        {
            score += LETTER_VALUES[toupper(word[i]) - 'A'];
        }
    }
    return score;
}
