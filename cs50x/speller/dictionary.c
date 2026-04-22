// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"
//
unsigned int word_count = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Increase bucket size to a prime number
const unsigned int N = 90001;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int word_index = hash(word);
    node *cursor = table[word_index];
    while (cursor != NULL)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // DJB2 hash seems a common implementation
    unsigned long hash = 5381;
    int c;

    while ((c = tolower(*word++)) != 0)
    {
        hash = ((hash << 5) + hash) + c;
    }
    return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open dictionary with read attribute
    FILE *dct = fopen(dictionary, "r");
    // Error check for file existance and load
    if (dct == NULL)
    {
        printf("Could not open file.");
        return false;
    }
    char buffer[LENGTH + 1];
    while (fscanf(dct, "%s", buffer) != EOF)
    {
        // Memory allocation
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            fclose(dct);
            return false;
        }

        strcpy(n->word, buffer);
        unsigned int index = hash(buffer);

        n->next = table[index];
        table[index] = n;

        word_count++;
    }

    fclose(dct);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // Returns number of words loaded in load function
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        while (table[i] != NULL)
        {
            node *tmp = table[i]->next;
            free(table[i]);
            table[i] = tmp;
        }
    }
    return true;
}
