
"""CS50 Nutrition Facts

This program provides the number of calories in a portion of fruit 
based on the FDA's poster for raw fruits.

Python concepts highlighted:
- Dictionary mapping and lookups
- String manipulation (strip, lower)
- Infinite iteration (while True) and breaking (break)
"""

fruits = {
    'apple': 130, 'avocado': 50,
    'banana': 110, 'cantaloupe': 50,
    'grapefruit': 60, 'grapes': 90,
    'honeydew melon': 50, 'kiwifruit': 90,
    'lemon': 15, 'lime': 20,
    'nectarine': 60, 'orange': 80,
    'peach': 60, 'pear': 100,
    'pineapple': 50, 'plums': 70,
    'strawberries': 50, 'sweet cherries': 100,
    'tangerine': 50, 'watermelon': 80,
}


def function_one(fruit):
    """Retrieves the calorie count for a given fruit.
    
    Args:
        fruit (str): User input of fruit to check.
        
    Returns:
        int: Calories per serving of the fruit.
    """
    calories = fruits[fruit]
    return calories


def main():
    """Run the main program to prompt the user and output fruit calories."""
    # Get user inout of fruit
    while True:
        item = input("Item: ")
        cleaned_fruit = item.strip().lower()
        if cleaned_fruit not in fruits:
            break
        # Print results
        print(f"Calories: {function_one(cleaned_fruit)}")
        break


if __name__ == '__main__':
    main()
