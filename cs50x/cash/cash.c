/*
Making change using a greedy algorithm
Resubmitted after style changes per Style50 guidelines
*/
#include <cs50.h>
#include <stdio.h>

// Function declarations
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

// Variable declarations. Had scope issues that were solved by declaring here.
int change;
int quarters;
int dimes;
int nickels;
int pennies;

// Main program
int main(void)
{
# Get proper user input for height
while True:
    try:
        change = int(input("How much change do you need in dollars (i.e. 9.50, 1.33, 0r ): "))
        if height >= 1 and height <= 8:
            break
        else:
            print('Invalid response. Please try again.')
    except ValueError:
        print('Invalid response. Please try again.')

    // Introductory statement
    printf("\nLet's figure out your change in the fewest amount of coins possible.\n");
    // Get user's input with type enforcement
    do
    {
        change = get_int("How much change do you need (in cents): ");
    }
    while (change <= 0);

    // Loop to call functions
    while (change > 0)
    {
        if (change >= 25)
        {
            quarters = calculate_quarters(change);
            change = change - (quarters * 25);
        }
        if (change >= 10)
        {
            dimes = calculate_dimes(change);
            change = change - (dimes * 10);
        }
        if (change >= 5)
        {
            nickels = calculate_nickels(change);
            change = change - (nickels * 5);
        }
        if (change > 0)
        {
            pennies = calculate_pennies(change);
            change = change - (pennies * 1);
        }
        int total = quarters + dimes + nickels + pennies;
        // Print results
        printf("Quarters: %d\n", quarters);
        printf("Dimes: %d\n", dimes);
        printf("Nickels: %d\n", nickels);
        printf("Pennies: %d\n", pennies);
        printf("The total number of coins is: %d\n", total);
    }
}
// Function definitions
// Calculate how many quarters you should give customer
int calculate_quarters(int cents)
{
    quarters = 0;
    while (cents >= 25)
    {
        quarters++;
        cents = cents - 25;
    }
    return quarters;
}
// Calculate how many dimes you should give customer
int calculate_dimes(int cents)
{
    dimes = 0;
    while (cents >= 10)
    {
        dimes++;
        cents = cents - 10;
    }
    return dimes;
}
// Calculate how many nickels you should give customer
int calculate_nickels(int cents)
{
    nickels = 0;
    while (cents >= 5)
    {
        nickels++;
        cents = cents - 5;
    }
    return nickels;
}
// Calculate how many pennies you should give customer
int calculate_pennies(int cents)
{
    pennies = 0;
    while (cents >= 1)
    {
        pennies++;
        cents = cents - 1;
    }
    return pennies;
}
