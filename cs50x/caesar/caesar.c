// Offset cipher ala Caesar
#include <cs50.h>
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// function prototypes
bool only_digits(string key);
void bad_exit();
string encrypt(string plain_text, int cipher_key);

// Program entry with command line arguments
int main(int argc, string argv[])
{
    int cipher_key = 0;

    // Checks for correct number of command line arguments
    if (argc <= 1 || argc > 2)
    {
        bad_exit();
    }
    string key = argv[1];
    bool good_key = only_digits(key);
    // Check for numeric value of passed key string
    if (good_key == false)
    {
        bad_exit();
    }
    // Passed checks for good command line arguments, continue
    cipher_key = atoi(key);
    string plain_text = get_string("plaintext: ");
    string cipher_text = encrypt(plain_text, cipher_key);
    printf("ciphertext: %s\n", cipher_text);
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
void bad_exit()
{
    printf("Usage: ./caesar key\n");
    exit(1);
}
string encrypt(string plain_text, int cipher_key)
{
    string encrypted_text = malloc(strlen(plain_text) + 1);
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
    return encrypted_text;
}
