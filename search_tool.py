"""Code Library Search Tool

This script searches through the module-level docstrings of all Python files
in a specified directory to find keywords or concepts.

Python concepts highlighted:
- The 'ast' module for parsing Python code safely
- The 'pathlib' module for file and directory traversal
- Command line arguments via 'sys'
"""

import ast
import sys
from pathlib import Path

def search_library(directory: str, search_term: str):
    """Searches Python files in the directory for the given term in their docstrings.
    
    Args:
        directory (str): The base directory to search within.
        search_term (str): The keyword or concept to find in the docstrings.
    """
    base_path = Path(directory)
    search_term_lower = search_term.lower()
    matches_found = 0

    print(f"Searching for '{search_term}' in {directory}...\n")

    # rglob("*.py") recursively finds all Python files in the directory and subdirectories
    for filepath in base_path.rglob("*.py"):
        try:
            # Read the python file
            with open(filepath, "r", encoding="utf-8") as file:
                source_code = file.read()
            
            # Parse the code into an Abstract Syntax Tree (AST) to easily get the docstring
            parsed_code = ast.parse(source_code)
            docstring = ast.get_docstring(parsed_code)

            # Check if the docstring exists and contains our search term
            if docstring and search_term_lower in docstring.lower():
                print(f"✅ Match found in: {filepath.name}")
                print(f"   Path: {filepath}")
                print("-" * 40)
                matches_found += 1
                
        except Exception as e:
            # Skip files that can't be read or parsed
            continue
            
    print(f"\nTotal matches found: {matches_found}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python search_tool.py <search_term>")
        sys.exit(1)
        
    # Hardcoded to search your library directory, passing the first command line argument
    library_dir = "/home/mlab/Desktop/code_library"
    search_library(library_dir, sys.argv[1])
