#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n = get_int("What is n? \n");
    if (n < 0)
    {
        n = get_int("What's n? \n");
    }

    for (int i = 0; i < n; i++)
    {
        printf("Meow\n");
    }
}
