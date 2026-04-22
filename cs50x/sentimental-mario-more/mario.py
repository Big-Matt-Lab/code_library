""" This is a python version of CS50 mario-more
The loops iterate thru the user defined height and create leading spaces
(loop j), create the first pyramid blocks (loop k), add a space and then create the mirror
pyramid (loop l). Finally, a print() advances to the next row. """

print("Welcome to Mario's Hill Climb.")

# Get proper user input for height
while True:
    try:
        height = int(input("How high should we draw the pyramid (enter 1-8): "))
        if height >= 1 and height <= 8:
            break
        else:
            print('Invalid response. Please try again.')
    except ValueError:
        print('Invalid response. Please try again.')

# Use loop to build pyramid
# This loop iterates thru the height setting the number of horizontal rows
for row in range(height, 0, -1):

    # Loop for leading spaces
    for j in range(row - 1):
        print(" ", end='')

    # Loop for first pyramid blocks
    for k in range(height - row + 1):
        print("#", end='')

    # Space between pyramids
    print("  ", end='')

    # Loop for second pyramid blocks
    for l in range(height - row + 1):
        print("#", end='')

    # Advance a line, ready for next row
    print()
