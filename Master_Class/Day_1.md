# Day 1 — Python Basics

This file covers core Python fundamentals: variables and data types, I/O, operators, control flow, functions, and a short introduction to object-oriented programming (OOP). Examples are small and focused so you can run them interactively.

---

## Variables and Data Types

Python is a dynamically typed language, which means a variable's type is determined at runtime:

```python
a = 10
b = 20
is_dev = True
```

Note: dynamic typing is convenient but can lead to subtle bugs (e.g., mixing strings and numbers). Use type hints and tests to reduce those issues.

---

## Strings

Anything that represents text is a string (names, emails, passwords, etc.).

```python
first_name = "Hem"
last_name = "Pradhan"

# Concatenate with a space
full_name = first_name + " " + last_name

# Recommended: f-strings for readability
print(f"My name is {full_name}! I am a Python student.")
```

---

## Lists and Dictionaries

Lists store ordered collections:

```python
skills = ["Python", "SQL", "DSA"]
print(skills[0])  # prints "Python"
```

Dictionaries store key-value pairs and are often used for structured data (e.g., API payloads):

```python
user = {
    "name": "Hem",
    "age": 22,
    "city": "Jamshedpur"
}

print(user["name"])  # prints "Hem"
```

Keys are case-sensitive. Use `.get()` if a key may be missing: `user.get("email", "no-email")`.

---

## Input / Output

Basic console I/O:

```python
name = input("Enter name: ")
print(f"Welcome, {name}!")

age = int(input("Enter your age: "))  # convert input from str to int
print(age)
```

Always validate and convert input before using it (e.g., use try/except for conversions).

---

## Operators

Arithmetic operators:

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.3333333333333335 (float division)
print(a // b)  # 3 (floor division)
print(a % b)   # 1 (remainder)
print(a ** b)  # 1000 (exponentiation)
```

Comparison operators:

```python
a > b
a < b
a == b
a != b
a >= b
a <= b
```

Logical operators:

```python
x = True
y = False
print(x and y)
print(x or y)
print(not x)
```

---

## Control Flow

Conditionals (proper syntax and indentation are essential):

```python
age = int(input("Enter your age: "))
if age >= 18:
    print("You can vote.")
else:
    print("You are under age.")
```

Chained conditionals with `elif`:

```python
marks = int(input("Enter marks: "))
if marks >= 90:
    print("A")
elif marks >= 75:
    print("B+")
elif marks >= 60:
    print("B")
else:
    print("C or below")
```

---

## Loops

For loop with `range()`:

```python
for i in range(5):
    print(i)  # prints 0,1,2,3,4
```

Note: `range(5)` goes from 0 up to (but not including) 5.

While loop:

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

---

## Functions

Write reusable, readable code with functions. Use type hints and docstrings for clarity.

```python
def greet_name(name: str) -> str:
    """Return a greeting for the given name."""
    return f"Hello {name}"

print(greet_name("Hem"))

def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b
```

Type hints improve readability and help static analysis tools catch bugs early.

---

## Object-Oriented Programming (OOP)

Classes are blueprints; objects are instances of classes. Attributes are data stored on an object, methods are functions attached to an object.

Simple class example:

```python
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def set_name(self, name: str) -> str:
        self.name = name
        return f"Hello, I am {self.name}"

u = User("Hem", 22)
print(u.set_name("Hem Pradhan"))
```

Constructor in Python is the `__init__` method.

---

## Encapsulation and Conventions

Use a single leading underscore to indicate an attribute is intended for internal use (it's a convention, not enforced):

```python
class Bank:
    def __init__(self, balance: int):
        self._balance = balance  # leading underscore = "internal use"

    def deposit(self, amount: int):
        if amount <= 0:
            raise ValueError("Invalid amount")
        self._balance += amount

    def get_balance(self) -> int:
        return self._balance
```

- Prefer `self._balance` for the internal value.
- Validate inputs and raise meaningful exceptions (e.g., `ValueError`) when needed.

---

## Best Practices / Notes

- Follow PEP 8 for naming and formatting.
- Use descriptive variable and function names.
- Prefer `f-strings` for string formatting.
- Validate user input and handle exceptions.
- Use type hints to improve readability and enable static checking.
- Write small functions that do one thing (single responsibility).
- Add docstrings and comments where helpful.
- Test code interactively and write unit tests for production code.

---

That's a cleaned-up, corrected version of Day 1 notes. Would you like me to commit this updated file to the repository (create a new commit on the same branch)? If so, I can push the change for you.
