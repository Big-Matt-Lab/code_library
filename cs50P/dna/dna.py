"""CS50 DNA

This program identifies a person based on their DNA sequence by comparing
the longest runs of Short Tandem Repeats (STRs) in a sequence against a
database of individuals.

Python concepts highlighted:
- File I/O operations (open, read)
- CSV parsing (csv.DictReader)
- Command line arguments via 'sys'
- Dictionary and List manipulation
- Nested iteration and slicing
"""
import csv
import sys


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence.
    
    Args:
        sequence (str): The DNA sequence to search.
        subsequence (str): The STR to look for within the sequence.
        
    Returns:
        int: The length of the longest consecutive run of the subsequence.
    """

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        # Thank goodness this section was provided!
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match` in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for matches at each character in sequence, return longest run found
    return longest_run


def main():
    """Run the main DNA matching program.
    
    Reads DNA database and sequence files, compares STR counts, and prints match.
    """

    # TODO: Check for command-line usage
    # Check if two arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python dna.py <database_name.csv> <sequence_name.txt>")
        sys.exit(1)

    database_name = sys.argv[1]
    sequence_name = sys.argv[2]

    # TODO: Read database file into a variable
    database = []
    with open(database_name) as file:
        reader = csv.DictReader(file)
        for row in reader:
            database.append(row)
    # TODO: Read DNA sequence file into a variable
    with open(sequence_name) as file_2:
        sequence = file_2.read()

    # Find longest match of each STR in DNA sequence
    #
    str_list = list(database[0].keys())[1:]

    # Store the str counts for the sequence
    # Create dictionary
    sequence_str_counts = {}
    for str_name in str_list:
        # Call longest_match function
        count = longest_match(sequence, str_name)
        sequence_str_counts[str_name] = count

    # Check database for matching profiles
    for person in database:
        # Presumed match until rejected
        match = True
        for str_name in str_list:
            # Convert the stored database string value to an int to avoid Type error
            if int(person[str_name]) != sequence_str_counts[str_name]:
                match = False
                break

        # If all STR counts matched, print the person's name and exit
        if match:
            print(person['name'])
            return

    # If no match was found after checking all names in list
    print("No match")
    return


if __name__ == "__main__":
    main()
