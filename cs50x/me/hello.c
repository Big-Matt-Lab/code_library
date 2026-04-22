#include <cs50.h>
#include <stdio.h>

// program entry point
int main(void)
{
    // Take imput from user
    string name = get_string("What's your name? ");
    printf("hello, %s\n", name);
}
