# Python 101 Tutorial

---

## Table of Contents

1. History of Python Language
2. History of Python Versions
3. Variables
4. If Statements and Walrus Operator
5. For Loops
6. While Loops
7. Try-Catch (Exception Handling)
8. Functions
9. Class and Polymorphism
10. Typing
11. Basic Libraries
12. Data Science Essentials
13. HTTP Requests Using `httpx`
14. Import Statements
15. Working with `requirements.txt`

---

## 1. History of Python Language

Python was created by Guido van Rossum and first released in 1991. The language emphasizes readability and simplicity, and it's widely used for web development, data science, artificial intelligence, and more.

## 2. History of Python Versions

### Python 1.0 (1994)

- The first official version.
- Included features like lambda, map, filter, and reduce.

### Python 2.0 (2000)

- Introduced list comprehensions for more concise lists.
- Added garbage collection for cyclical references.

### Python 2.7 (2010)

- The last of the 2.x series.
- Included many features that were backported from Python 3.x.
  
### Python 3.0 (2008)

- A major revamp of the language, making it not backward-compatible with Python 2.x.
- Print became a function, integer division resulted in a float, etc.

### Python 3.6 (2016)

- Introduced f-strings, a way to embed expressions inside string literals.
  
### Python 3.7 (2018)

- Introduced data classes that simplify the classes used for storing data.
  
### Python 3.8 (2019)

- Introduced the Walrus Operator (`:=`), which allows both assignment and evaluation of variables within an expression.

## 3. Variables

```python
x = 10  # Integer
y = 20.5  # Float
name = "Alice"  # String
is_valid = True  # Boolean
```

## 4. If Statements and Walrus Operator

```python
# Traditional If Statement
if x > y:
    print("x is greater than y")

# Using Walrus Operator (Python 3.8+)
if (n := x * 2) > y:
    print(f"n ({n}) is greater than y ({y})")
```

## 5. For Loops

```python
for i in range(5):
    print(i)
```

## 6. While Loops

```python
i = 0
while i < 3:
    print(i)
    i += 1
```

## 7. Try-Catch (Exception Handling)

```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
```

## 8. Functions

```python
def greet(name):
    return f"Hello, {name}"
```

## 9. Class and Polymorphism

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"
```

## 10. Typing

```python
from typing import List

def add_numbers(numbers: List[int]) -> int:
    return sum(numbers)
```

## 11. Basic Libraries

```python
import math
import datetime
```

## 12. Data Science Essentials

- NumPy: For numerical operations.
- Pandas: For data manipulation.
- Matplotlib: For plotting and visualization.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

### Matplotlib

Matplotlib is a 2D plotting library which produces high-quality charts and figures.

```python
import matplotlib.pyplot as plt

# Basic Plot
plt.plot([1, 2, 3], [1, 4, 9])
plt.title("Basic Plot")
plt.show()
```

### Pandas

Pandas provide data structures for efficiently storing large amounts of data and time-series functionality.

```python
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': ['a', 'b', 'c']})

# Data manipulation
filtered_df = df[df['Column1'] > 1]
```

### NumPy

NumPy (Numerical Python) is the foundational package for numerical computing in Python.

```python
import numpy as np

# Create an array
arr = np.array([1, 2, 3])

# Perform operations
mean_val = np.mean(arr)
```

## 13. HTTP Requests Using `httpx`

```python
import httpx

async def fetch_data():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://jsonplaceholder.typicode.com/todos/1')
    return response.json()
```

## 14. Import Statements

```python
import math
from datetime import datetime
```

## 15. Working with `requirements.txt`

```
httpx==0.18.2
```

To install all dependencies, run:

```bash
pip install -r requirements.txt
```

