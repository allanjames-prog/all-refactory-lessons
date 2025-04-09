## 🏷️ **Static and Dynamic Functions in Python**

In Python, **static functions** and **dynamic functions** have distinct characteristics. Let's dive into what each term means:

### 📌 **1. Static Functions (Static Methods)**

A **static method** is a method that belongs to the class itself, rather than an instance of the class. It doesn't have access to the instance (`self`) or class (`cls`) attributes. Static methods are used when you want to perform a task related to the class but without needing to interact with any instance-specific data.

#### 🛠️ **How to Define a Static Method**

You define a static method using the `@staticmethod` decorator.

#### 📝 **Example:**
```python
class MyClass:
    @staticmethod
    def greet():
        print("Hello from a static method!")

# Usage
MyClass.greet()  # No need to create an instance of the class
```

#### Key Points:
- **No access** to instance or class attributes.
- **Called on the class** itself, not on an instance.
- **Cannot modify instance state**.

---

### 📌 **2. Dynamic Functions (Instance Methods)**

**Dynamic functions** typically refer to instance methods, which are bound to a specific instance of a class. These functions operate on the instance and can access and modify its attributes. In Python, **instance methods** always take at least one argument, which is `self`, representing the instance.

#### 🛠️ **How to Define an Instance Method**

Instance methods are the default methods within a class, requiring an instance to be created before they can be called.

#### 📝 **Example:**
```python
class MyClass:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello, {self.name}!")

# Usage
obj = MyClass("Alice")
obj.greet()  # Calls the instance method on the object
```

#### Key Points:
- **Bound to the instance** of the class.
- **Accesses and modifies instance attributes** (`self`).
- **Requires an instance** to be called.

---

### 🧩 **Dynamic Nature of Python Functions**

Python, being a dynamically typed language, allows functions to be created, modified, or deleted during runtime. This means functions can be assigned to variables, passed around, and modified dynamically.

#### 📝 **Example:**
```python
def add(a, b):
    return a + b

# Dynamically changing the function
add = lambda a, b: a * b  # Change the function to multiplication

print(add(2, 3))  # Output: 6 (multiplication instead of addition)
```

Here, the `add` function is **dynamically redefined** during runtime to perform multiplication instead of addition.

---

## 📝 **Takeaways**

- **Static methods** belong to the class and **don’t depend on instance-specific data**.
- **Dynamic functions** are often **instance methods**, which interact with the instance and its attributes, or **functions that can be modified during runtime**.
- **Python's dynamic nature** allows flexibility in how functions are used or defined, offering opportunities for runtime modifications.

