"""Basic Loops Examples

Code examples demonstrating various styles of basic loops in Python.

Python concepts highlighted:
- For loops and while loops
- Range function and nested loops
- Loop/else constructs
"""

items = ['a', 'b', 'c']
for item in items:
    # Actionable code

for i in range(n):
    # Actionable code using i

    for j in range(x):
        # Nested loop using j

for _ in range(n):
    # Actionable code loop variable ( _ ) not used

i = 1
while i < 4:
    print(i)
    i += 1
else:
    print("Loop completed and i is no longer less than 4")
