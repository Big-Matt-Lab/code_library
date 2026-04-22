#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#define BUFFERSIZE 512

int main(int argc, char *argv[])
{
    // Checks for correct number of command line arguments
    if (argc != 2)
    {
        // Explain proper verbiage
        printf("Usage: ./recover FILE\n");
        return 1;
    }
    // Open file and check validity
    FILE *file = fopen(argv[1], "r");
    if (file == NULL)
    {
        printf("Bad card or file.\n");
        return 1;
    }

    // Create data buffer
    uint8_t buffer[BUFFERSIZE];
    int count = 0;
    FILE *out_file = NULL;
    char new_file[8];

    // Read from the cards memory
    while (fread(buffer, 1, BUFFERSIZE, file) == 512)
    {
        // Search for JPEG headers
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            if (out_file != NULL)
            {
                fclose(out_file);
            }

            // Create new file name
            sprintf(new_file, "%03i.jpg", count);

            // Open new file
            out_file = fopen(new_file, "w");
            if (out_file == NULL)
            {
                printf("The file failed to open.\n");
                fclose(file);
                return 1;
            }

            // Increment file naming counter
            count++;
        }

        // Write code to file
        if (out_file != NULL)
        {
            fwrite(buffer, 1, BUFFERSIZE, out_file);
        }
    }

    // Close all files at conclusion
    if (out_file != NULL)
    {
        fclose(out_file);
    }
    fclose(file);

    return 0;
}
