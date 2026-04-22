#include "helpers.h"
#include <math.h>

// Function to check max value in 'Sepia'
int cap(int value);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Get RGB of pixel and round avg for gray
            float sum = image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue;
            int avg = round(sum / 3.0);

            // Save RGB(grayed)
            image[i][j].rgbtRed = avg;
            image[i][j].rgbtGreen = avg;
            image[i][j].rgbtBlue = avg;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Get RGB of pixel and apply sepia algorithm
            float sepiaRed = .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen +
                             .189 * image[i][j].rgbtBlue;
            float sepiaGreen = .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen +
                               .168 * image[i][j].rgbtBlue;
            float sepiaBlue = .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen +
                              .131 * image[i][j].rgbtBlue;

            // Convert to int and check for > 255
            int sRed = round(sepiaRed);
            sRed = cap(sRed);
            int sGreen = round(sepiaGreen);
            sGreen = cap(sGreen);
            int sBlue = round(sepiaBlue);
            sBlue = cap(sBlue);

            // Save RGB(sepia)
            image[i][j].rgbtRed = sRed;
            image[i][j].rgbtGreen = sGreen;
            image[i][j].rgbtBlue = sBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            // 'Extra container swap', minus 1 to account for zero indexing
            int tmpRed = image[i][width - j - 1].rgbtRed;
            image[i][width - j - 1].rgbtRed = image[i][j].rgbtRed;
            image[i][j].rgbtRed = tmpRed;

            int tmpGreen = image[i][width - j - 1].rgbtGreen;
            image[i][width - j - 1].rgbtGreen = image[i][j].rgbtGreen;
            image[i][j].rgbtGreen = tmpGreen;

            int tmpBlue = image[i][width - j - 1].rgbtBlue;
            image[i][width - j - 1].rgbtBlue = image[i][j].rgbtBlue;
            image[i][j].rgbtBlue = tmpBlue;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Make a copy of image
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }
    // Iterate through image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            float redTotal = 0, greenTotal = 0, blueTotal = 0;
            int count = 0;
            // Checking neighboring values for averaging
            for (int row = i - 1; row <= i + 1; row++)
            {
                for (int col = j - 1; col <= j + 1; col++)
                {
                    // Limits the rounding to 'pixels' within the border of the image
                    if (row >= 0 && row < height && col >= 0 && col < width)
                    {
                        redTotal += copy[row][col].rgbtRed;
                        greenTotal += copy[row][col].rgbtGreen;
                        blueTotal += copy[row][col].rgbtBlue;
                        count++;
                    }
                }
            }
            // Write back to original array
            image[i][j].rgbtRed = round(redTotal / count);
            image[i][j].rgbtGreen = round(greenTotal / count);
            image[i][j].rgbtBlue = round(blueTotal / count);
        }
    }
    return;
}

// Caps value at 255. No RGB value > 255
int cap(int value)
{
    if (value > 255)
    {
        value = 255;
    }
    return value;
}
