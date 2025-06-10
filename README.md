# ⚙️ Python Generators and Decorators

This repository contains learning materials and examples to help you understand **Generators** and **Decorators** in Python — two powerful concepts for building efficient and elegant Python programs.

---

## 🔁 Generators

Generators allow you to iterate over data without storing it entirely in memory. They are memory-efficient and lazy-evaluated.

### 📘 Topics Covered
- Generator functions using `yield`
- Generator expressions
- Iterating with `next()`
- Comparing generators vs lists

### 📄 Example

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)
```

---

## 🧩 Decorators

Decorators are functions that modify the behavior of another function without permanently changing it. Commonly used for logging, validation, timing, etc.

### 📘 Topics Covered
- Basic decorators
- Decorators with arguments
- Using `functools.wraps`
- Nesting multiple decorators

### 📄 Example

```python
def log_func(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_func
def greet(name):
    return f"Hello, {name}"
```

---

## 🚀 How to Use

1. Clone or download this repository.
2. Navigate into the folders: `generators/` or `decorators/`
3. Run the Python scripts using:

```bash
python example.py
```

---

## 📂 Folder Structure

```
/generators
    example_generator.py
/decorators
    example_decorator.py
```

---

## 👩‍💻 Created by BHUVANESWARI KAPULRU 
Happy coding and learning Python step-by-step!
