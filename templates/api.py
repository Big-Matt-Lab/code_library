"""API Request Examples

This file contains template snippets for making HTTP requests to external APIs 
and parsing the JSON responses.

Python concepts highlighted:
- Third-party library integration (requests module)
- JSON parsing (json module)
- Command line arguments (sys module)
- Exception handling (try/except blocks)
"""



import json # to work with file returned from request
import requests # properly makes actual request of URL
import sys # handles command line arguments and exit

# Error check command line arg
if len(sys.argv) != 2:
    sys.exit()

# Make request of URL and assign response to variable
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

# json() does it's magic and saves its work to another variable
o = response.json()

# iterate thru list and print desired results ( in this case, 'trackName')
for result in o["results"]:
    print(result["trackName"])




import json # to work with file returned from request
import requests # properly makes actual request of URL
import sys # handles command line arguments and exit

def main():
    """Run the main program to prompt for an artist and display matching artworks."""
    print("Search the Art Institute of Chicago!")
    artist = input("Artist: ")

    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": artist, "limit": 3}
        )
        response.raise_for_status()
    except requests.HTTPError:
        print("Couldn't complete request!")
        sys.exit(1)

    content = response.json()
    for artwork in content["data"]:
        print(f"* {artwork['title']}")


main()
