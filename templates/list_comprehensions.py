"""List Comprehension Examples

Demonstrates concise ways to process lists using generator expressions
and list comprehensions.

Python concepts highlighted:
- Iteration (for loops)
- Generator expressions and sum function
"""



def match_ends(words):
    """Counts the number of words that have a length of at least 2 and match at their ends.
    
    Args:
        words (list): A list of strings.
        
    Returns:
        int: The count of matching words.
    """
  # +++your code here+++
  count = 0
  for word in words:
    if len(word) >=2 and word[0] == word[-1]:
      count += 1
  return count



def match_ends(words):
    """Counts the number of words that have a length of at least 2 and match at their ends.
    
    Args:
        words (list): A list of strings.
        
    Returns:
        int: The count of matching words.
    """
    # We create a list of 'True' values for each word that matches, then sum them
    return sum(1 for word in words if len(word) >= 2 and word[0] == word[-1])
