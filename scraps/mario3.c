#include <cs50.h>
#include <stdio.h>

// Program entry
int main(void)
{
    // Introductory statement
    printf("\nWelcome to Mario's Hill Climb.\n");
    int height;
    do
    {
        height = get_int("How high should we draw the pyramid (enter 1-8): ");
    }
    while (height <= 0 || height > 8);
    // Use loop to build pyramid
    for (int i = height; i > 0; i--)
    {
        // Loop for spaces
        for (int j = i - 1; j > 0; j--)
        {
            printf(" ");
        }
        // Loop for hashes
        for (int k = 0; k < height - (i - 1); k++)
        {
            printf("##");
        }
        // Move to new line at end of 'i' loop iteration
        printf("\n");
    }
        for (int i = 2; i <= height; i++)
    {
        // Loop for spaces
        for (int j = i - 1; j > 0; j--)
        {
            printf(" ");
        }
        // Loop for hashes
        for (int k = 0; k < height - (i - 1); k++)
        {
            printf("##");
        }
        // Move to new line at end of 'i' loop iteration
        printf("\n");
    }
}

