// Offset cipher ala Caesar
#include <cs50.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// function prototypes
bool only_digits(string key);
void incorrect_args();
string caesar_encrypt(string plain_text, int cipher_key);

// Program entry with command line arguments
int main(int argc, string argv[])
{
    int cipher_key = 0;

    // Checks for correct number of command line arguments
    if (argc <= 1 || argc > 2)
    {
        incorrect_args();
    }
    string key = argv[1];
    bool good_key = only_digits(key);
    // Check for numeric value of passed key string
    if (good_key == false)
    {
        incorrect_args();
    }
    // Passed checks for good command line arguments, continue
    cipher_key = atoi(key);
    string plain_text = get_string("plaintext: ");
    string cipher_text = caesar_encrypt(plain_text, cipher_key);
    printf("ciphertext: %s\n", cipher_text);
    free(cipher_text);
    cipher_text = NULL;
}

// Functions below
bool only_digits(string key)
{
    for (int i = 0; i < strlen(key); i++)
    {
        if (isdigit(key[i]) == 0)
        {
            return false;
        }
    }
    return true;
}
void incorrect_args()
{
    printf("Usage: ./caesar2 key\n");
    exit(1);
}
string caesar_encrypt(string plain_text, int cipher_key)
{
    string encrypted_text = malloc(strlen(plain_text) + 1);
    for (int i = 0, len = strlen(plain_text); i < len; i++)
    {
        if (isupper(plain_text[i]))
        {
            encrypted_text[i] = ((plain_text[i] - 65 + cipher_key) % 26) + 65;
        }
        else if (islower(plain_text[i]))
        {
            encrypted_text[i] = ((plain_text[i] - 97 + cipher_key) % 26) + 97;
        }
        else
        {
            encrypted_text[i] = plain_text[i];
        }
    }
    return encrypted_text;
}
