# This is a single-line comment
x = 10  # You can also put a comment after code
print(x)

# This program calculates
# the area of a rectangle
length = 5
width = 3
area = length * width
print(area)

"""
This is a multi-line string,
often used as a multi-line comment.
But technically, Python stores it in memory
if not used as a docstring.
"""
x = x + 1  # Increase x by 1

def greet(name):
    """This function greets the person passed as an argument."""
    print("Hello, " + name + "!")
def factorial(n):
    """
    Calculate factorial using recursion.
    n: integer
    returns: factorial of n
    """
    # Base case: factorial of 0 or 1 is 1
    if n <= 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    return n * factorial(n - 1)
