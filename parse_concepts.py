"""Python Concept Parser

This script traverses a specified directory to find Python files, parses their 
abstract syntax trees (AST) to extract module-level docstrings, and aggregates 
a master list of Python concepts highlighted in those files.

Python concepts highlighted:
- Abstract Syntax Tree parsing (ast module)
- File system traversal (os.walk)
- Set operations
- String manipulation and list comprehensions
- Type hinting
"""
import ast
import os

def extract_concepts(file_path: str) -> list:
    """Extracts Python concepts documented in the module docstring of a given file.
    
    Args:
        file_path (str): The path to the Python file to parse.
        
    Returns:
        list: A list of extracted concept strings, or an empty list if none are found.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            tree = ast.parse(f.read())
            docstring = ast.get_docstring(tree)
            if docstring:
                # Look for the standardized header established in the code library
                if "Python concepts highlighted:" in docstring:
                    concepts_section = docstring.split("Python concepts highlighted:")[1]
                    # Extract bulleted list items following the header
                    return [line.lstrip("- ").strip() for line in concepts_section.split('\n') if line.strip().startswith("-")]
        except Exception as e:
            print(f"Error parsing {file_path}: {e}")
    return []

def main() -> None:
    """Run the main program to aggregate and output all concepts.
    
    Traverses the project directory, extracts concepts from each Python file,
    updates a master set to ensure uniqueness, and outputs the sorted results
    to both the terminal and a text file.
    """
    all_concepts = set()
    project_root = "." # Change this to your project path if needed
    output_file = "concepts_output.txt"

    with open(output_file, "w", encoding="utf-8") as f_out:
        for root, _, files in os.walk(project_root):
            for file in files:
                if file.endswith(".py"):
                    path = os.path.join(root, file)
                    concepts = extract_concepts(path)
                    if concepts:
                        msg = f"Found in {file}: {concepts}"
                        print(msg)
                        f_out.write(msg + "\n")
                        all_concepts.update(concepts)

        header = "\n--- Master List of Python Concepts Used ---"
        print(header)
        f_out.write(header + "\n")
        for concept in sorted(all_concepts):
            msg = f"- {concept}"
            print(msg)
            f_out.write(msg + "\n")

    print(f"\nResults successfully saved to {output_file}")

if __name__ == "__main__":
    main()
    # EOF
