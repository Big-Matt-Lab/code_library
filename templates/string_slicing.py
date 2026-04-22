"""String Slicing Examples

Various functions demonstrating standard string manipulation, slicing, 
and evaluation logic.

Python concepts highlighted:
- String slicing and manipulation
- String methods (find, replace)
- Conditional logic
"""
        # A. donuts
        # Given an int count of a number of donuts, return a string
        # of the form 'Number of donuts: <count>', where <count> is the number
        # passed in. However, if the count is 10 or more, then use the word 'many'
        # instead of the actual count.
        # So donuts(5) returns 'Number of donuts: 5'
        # and donuts(23) returns 'Number of donuts: many'
def donuts(count):
    """Creates a string detailing the number of donuts.
    
    Args:
        count (int): The number of donuts.
        
    Returns:
        str: A formatted string stating the number of donuts, or 'many' if 10 or more.
    """
  if count > 9:
    return 'Number of donuts: many'
  return f'Number of donuts: {count}'


        # B. both_ends
        # Given a string s, return a string made of the first 2
        # and the last 2 chars of the original string,
        # so 'spring' yields 'spng'. However, if the string length
        # is less than 2, return instead the empty string.
def both_ends(s):
    """Creates a string made of the first 2 and last 2 chars of the original string.
    
    Args:
        s (str): The original string.
        
    Returns:
        str: The modified string, or an empty string if the length is less than 2.
    """
  if len(s) < 2:
    return''
  return s[:2] + s[-2:]


        # C. fix_start
        # Given a string s, return a string
        # where all occurences of its first char have
        # been changed to '*', except do not change
        # the first char itself.
        # e.g. 'babble' yields 'ba**le'
        # Assume that the string is length 1 or more.
        # Hint: s.replace(stra, strb) returns a version of string s
        # where all instances of stra have been replaced by strb.
def fix_start(s):
    """Replaces all occurrences of the first char with '*' except the first char itself.
    
    Args:
        s (str): The original string.
        
    Returns:
        str: The modified string.
    """
  first_char = s[0]
  return first_char + s[1:].replace(s[0], '*')



        # D. MixUp
        # Given strings a and b, return a single string with a and b separated
        # by a space '<a> <b>', except swap the first 2 chars of each string.
        # e.g.
        #   'mix', pod' -> 'pox mid'
        #   'dog', 'dinner' -> 'dig donner'
        # Assume a and b are length 2 or more.
def mix_up(a, b):
    """Creates a single string with a and b separated by a space and their first 2 chars swapped.
    
    Args:
        a (str): The first string.
        b (str): The second string.
        
    Returns:
        str: The combined and modified string.
    """
  return b[:2] + a[2:] + " " + a[:2] + b[2:]

def not_bad(s):
    """Replaces the first 'not...bad' substring with 'good' if 'not' appears before 'bad'.
    
    Args:
        s (str): The original string.
        
    Returns:
        str: The modified string.
    """
  # +++your code here+++
  not_index = s.find('not')
  bad_index = s.find('bad')
  if not_index > -1 and bad_index > -1:
    if not_index < bad_index:
      new_string = s[:not_index] + 'good' + s[bad_index + 3:]
      return new_string
    return s
  return s


def front_back(a, b):
    """Divides two strings in halves and combines their front and back halves respectively.
    
    Args:
        a (str): The first string.
        b (str): The second string.
        
    Returns:
        str: The combined string from the respective halves.
    """
    # Calculate the split point for 'a'
    # Adding 1 before floor dividing by 2 effectively "rounds up"
    a_middle = (len(a) + 1) // 2
    a_front = a[:a_middle]
    a_back = a[a_middle:]

    # Now do the exact same for 'b'
    b_middle = (len(b) + 1) // 2
    b_front = b[:b_middle]
    b_back = b[b_middle:]
