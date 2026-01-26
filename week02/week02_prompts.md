# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**My Prompt**
> You are a senior Python developer. I have a Python function that is supposed
to calculate the sum of all even numbers in a list, but it is returning
incorrect results.
 
**Buggy code**:
```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 1:  # This line has a bug!
            total += num
    return total

> Context: The function currently adds the wrong numbers because of a logical
error in the conditional statement.
> Task: Please identify the bug and fix it.


**AI's Corrected Code:**
```python
def sum_of_evens(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

What I learned: I learned how a small logical condition can completely change a function’s behavior and how AI can quickly identify and explain simple logic errors.

## Problem 2: Refactoring

**My Prompt**

> You are a senior Python developer who writes clean, readable code.
> I have a function called get_names_of_adults that finds the names of adults from a list of users. It works, but it uses a complicated loop that isn’t easy to read.

 def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    results = []
    for i in range(len(users)):
        if users[i]['age'] >= 18:
            results.append(users[i]['name'])
    return results

> Rewrite the function to make it clearer and easier to read.
> Show the updated code in a Python code block and briefly explain why it is better and more Python-style.

**AI's Corrected Code:**
```python
def get_names_of_adults(users):
    """
    Returns a list of names of users who are 18 or older.
    
    Uses list comprehension for better readability and performance.
    """
    return [user['name'] for user in users if user['age'] >= 18]


## Problem 3: Documenting

**My Prompt**

> Context: I have a function called calculate_area that works but has no documentation. It raises an error if the inputs are not valid.

def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width

> Task: Write a NumPy-style docstring for this function.
> Format: Show the full function in a Python code block with sections for Parameters, Returns, and Raises.

**AI's Corrected Code:**
``python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters
    ----------
    length : float or int
        The length of the rectangle. Must be a positive value.
    width : float or int
        The width of the rectangle. Must be a positive value.

    Returns
    -------
    area : float or int
        The calculated area of the rectangle.

    Raises
    ------
    ValueError
        If either length or width is less than or equal to zero.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width




