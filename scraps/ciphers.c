
#include <cs50.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(void)
{
    string plain_text = "aBcd";
    // Allocate memory for the string + null terminator
    string encrypted_text = malloc(strlen(plain_text) + 1);

    int cipher_key = 5;
    for (int i = 0, len = strlen(plain_text); i < len; i++)
    {
        if (plain_text[i] >= 'A' && plain_text[i] <= 'Z')
        {
            encrypted_text[i] = ((plain_text[i] - 'A' + cipher_key) % 26) + 'A';
        }
        else if (plain_text[i] >= 'a' && plain_text[i] <= 'z')
        {
            encrypted_text[i] = ((plain_text[i] - 'a' + cipher_key) % 26) + 'a';
        }
        else
        {
            encrypted_text[i] = plain_text[i];
        }
    }
    printf("%s\n", encrypted_text);
}
