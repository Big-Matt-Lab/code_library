rm answer.txt#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Introductory statement
    printf("\nWelcome to Mario's Hill Climb.\n");
    int height;
    do
    {
        height = get_int("How many blocks high should we draw the pyramid: ");
    }
    while (height <= 0);
    // Use loop to build pyramid
    for (int i = height; i > 0; i--)
    {
        // Loop for spaces
        for (int j = i - 1; j > 0; j--)
            printf(" ");
        // Loop for hashes
        for (int h = 0; h < height - (i - 1); h++)
            printf("*");
        printf("\n");
    }
}
