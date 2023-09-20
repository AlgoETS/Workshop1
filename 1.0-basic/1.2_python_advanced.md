# Advanced Python 101 Tutorial

---

## Table of Contents

1. Generators and Yield Statement
2. Decorators
3. List Comprehensions and Generators Expressions
4. File Handling
5. Error and Exception Best Practices
6. Unit Testing
7. Context Managers
8. Working with JSON
9. Asynchronous Programming
10. Web Scraping Basics
11. Regular Expressions
12. Python and Databases
13. Web Frameworks Introduction
14. Packaging and Distributing Code
15. Virtual Environments

---

## 1. Generators and Yield Statement

### Overview

- Generators provide a way to iterate through a potentially large set of items without having to store the entire dataset in memory.

### Code Example

```python
def my_generator():
    yield 1
    yield 2
    yield 3
```

---

## 2. Decorators

### Overview

- Decorators wrap another function, extending its behavior without modifying its code.

### Code Example

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
```

---

## 3. List Comprehensions and Generators Expressions

### Overview

- List comprehensions provide a concise way to create lists, and generator expressions do the same for generators.

### Code Example

```python
squares = [x*x for x in range(5)]
squares_gen = (x*x for x in range(5))
```

---

## 4. File Handling

### Overview

- Python provides built-in functions for creating, reading, updating, and deleting files.

### Code Example

```python
with open("myfile.txt", "r") as f:
    print(f.read())
```

---

## 5. Error and Exception Best Practices

### Overview

- Proper error handling is crucial for writing robust programs.

### Code Example

```python
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")
```

---

## 6. Unit Testing

### Overview

- Unit tests help to ensure that your program works as expected.

### Code Example

```python
import unittest

class TestMyFunction(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
```

---

## 7. Context Managers

### Overview

- Context managers ensure resources are efficiently used and properly closed after operations are done.

### Code Example

```python
with open("myfile.txt", "r") as f:
    print(f.read())
```

---

## 8. Working with JSON

### Overview

- JSON (JavaScript Object Notation) is a lightweight data-interchange format and Python has built-in support for it.

### Code Example

```python
import json

data = {"name": "John", "age": 30}
json_data = json.dumps(data)
```

---

## 9. Asynchronous Programming

### Overview

- Asynchronous programming allows you to perform multiple operations simultaneously, improving the efficiency of IO-bound programs.

### Code Example

```python
import asyncio

async def main():
    print("Hello")
    await asyncio.sleep(1)
    print("World")
```

---

## 10. Web Scraping Basics

### Overview

- Web scraping involves extracting data from websites. It can be done in Python using libraries like BeautifulSoup and Selenium.

### Code Example

```python
from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.example.com')
soup = BeautifulSoup(page.content, 'html.parser')
```

---

## 11. Regular Expressions

### Overview

- Regular Expressions (RegEx) is a powerful tool for string manipulation and searching.

### Code Example

```python
import re

pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
```

---

## 12. Python and Databases

### Overview

- Python has built-in support for various databases like SQLite, MySQL, and PostgreSQL.

### Code Example

```python
import sqlite3

conn = sqlite3.connect("mydatabase.db")
```

---

## 13. Web Frameworks Introduction

### Overview

- Web frameworks like Django and Flask simplify the process of web development.

### Code Example

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

---

## 14. Packaging and Distributing Code

### Overview

- Python provides tools like `setuptools` for packaging and distributing code.

### Code Example

```bash
python setup.py sdist
```

---

## 15. Virtual Environments

### Overview

- Virtual environments provide isolated Python environments, allowing you to have project-specific dependencies.

### Code Example

```bash
python -m venv myenv
```
