# 🧠 PYTHON OPERATORS – STUDY NOTES

---

## 🔸 What Are Operators?

**Operators** in Python are special symbols used to perform operations on variables and values. Python provides several types of operators:

### Types of Operators:
1. Arithmetic Operators  
2. Comparison (Relational) Operators  
3. Logical Operators  
4. Bitwise Operators  
5. Assignment Operators  
6. Identity Operators  
7. Membership Operators  

---

## 1️⃣ Arithmetic Operators  
Used for basic mathematical operations.

| Operator | Name            | Example   | Result      |
|----------|-----------------|-----------|-------------|
| `+`      | Addition        | 5 + 3     | 8           |
| `-`      | Subtraction     | 5 - 3     | 2           |
| `*`      | Multiplication  | 5 * 3     | 15          |
| `/`      | Division        | 5 / 2     | 2.5         |
| `//`     | Floor Division  | 5 // 2    | 2           |
| `%`      | Modulus         | 5 % 2     | 1           |
| `**`     | Exponentiation  | 5 ** 2    | 25          |

```python
a = 10
b = 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

---

## 2️⃣ Comparison (Relational) Operators  
Used to compare two values.

| Operator | Name                      | Example    | Result |
|----------|---------------------------|------------|--------|
| `==`     | Equal to                  | 5 == 3     | False  |
| `!=`     | Not equal to              | 5 != 3     | True   |
| `>`      | Greater than              | 5 > 3      | True   |
| `<`      | Less than                 | 5 < 3      | False  |
| `>=`     | Greater than or equal to  | 5 >= 3     | True   |
| `<=`     | Less than or equal to     | 5 <= 3     | False  |

```python
x = 10
y = 5
print(x == y)  # False
print(x != y)  # True
print(x > y)   # True
print(x < y)   # False
print(x >= y)  # True
print(x <= y)  # False
```

---

## 3️⃣ Logical Operators  
Used to combine conditional expressions.

| Operator | Description                                  | Example                     |
|----------|----------------------------------------------|-----------------------------|
| `and`    | True if both conditions are true             | (5 > 3 and 10 > 5) → True   |
| `or`     | True if at least one condition is true       | (5 > 3 or 10 < 5) → True    |
| `not`    | Reverses the result of the condition         | not(5 > 3) → False          |

```python
x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False
```

---

## 4️⃣ Bitwise Operators  
Used for binary (bit-level) operations.

| Operator | Name         | Example     | Result |
|----------|--------------|-------------|--------|
| `&`      | AND          | 5 & 3       | 1      |
| `|`      | OR           | 5 \| 3      | 7      |
| `^`      | XOR          | 5 ^ 3       | 6      |
| `~`      | NOT          | ~5          | -6     |
| `<<`     | Left Shift   | 5 << 1      | 10     |
| `>>`     | Right Shift  | 5 >> 1      | 2      |

```python
a = 5  # binary: 101
b = 3  # binary: 011

print(a & b)   # 1
print(a | b)   # 7
print(a ^ b)   # 6
print(~a)      # -6
print(a << 1)  # 10
print(a >> 1)  # 2
```

---

## 5️⃣ Assignment Operators  
Used to assign values or modify variables.

| Operator | Example     | Equivalent To     |
|----------|-------------|-------------------|
| `=`      | x = 5       | x = 5             |
| `+=`     | x += 3      | x = x + 3         |
| `-=`     | x -= 3      | x = x - 3         |
| `*=`     | x *= 3      | x = x * 3         |
| `/=`     | x /= 3      | x = x / 3         |
| `//=`    | x //= 3     | x = x // 3        |
| `%=`     | x %= 3      | x = x % 3         |
| `**=`    | x **= 3     | x = x ** 3        |
| `&=`     | x &= 3      | x = x & 3         |
| `|=`     | x |= 3      | x = x \| 3        |
| `^=`     | x ^= 3      | x = x ^ 3         |
| `<<=`    | x <<= 3     | x = x << 3        |
| `>>=`    | x >>= 3     | x = x >> 3        |

```python
x = 10
x += 5
print(x)  # 15
```

---

## 6️⃣ Identity Operators  
Used to compare memory locations of two objects.

| Operator   | Description                                  | Example      |
|------------|----------------------------------------------|--------------|
| `is`       | True if both refer to the same object        | x is y       |
| `is not`   | True if they don’t refer to the same object  | x is not y   |

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)   # True
print(a is c)   # False
print(a == c)   # True (values are equal)
```

---

## 7️⃣ Membership Operators  
Used to check for presence in sequences (like lists, strings, sets).

| Operator   | Description                              | Example              |
|------------|------------------------------------------|----------------------|
| `in`       | True if value is in the sequence         | "a" in "apple"       |
| `not in`   | True if value is NOT in the sequence     | "x" not in "apple"   |

```python
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)        # True
print("grape" not in fruits)     # True
```

---

## 🧠 Relevance of Operators

- Operators are **fundamental** for calculations, logic, control flow, and data handling.
- Help form **expressions**, **conditions**, and **loop controls**.
- Mastery of operators is **essential** for solving programming problems.











### **WHAT IS OBJECT-ORIENTED PROGRAMMING (OOP)?**

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of objects. It structures a program so that the data (attributes) and the operations on that data (methods) are bundled together into objects. These objects are instances of classes, which define the blueprint or template for the objects.

In OOP, the focus is on creating objects that interact with each other to solve a problem, rather than focusing on functions and logic alone.

---

### **CORE CONCEPTS OF OOP**

OOP revolves around four main principles:

---

### **1. ENCAPSULATION**

Encapsulation means bundling the data (attributes) and the methods (functions) that operate on the data into a single unit called an object. This helps to hide the internal workings of an object and only expose what is necessary (i.e., the interface).

- **Data Hiding**: The internal data of an object can be hidden from the outside world and accessed only through specific methods.
  
- **Example**: Think of a bank account. You can deposit or withdraw money, but you don’t see the details of how the transaction is carried out inside the account. This is encapsulation in action.

**Example Code:**
```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute (hidden)

    def deposit(self, amount):
        self.__balance += amount  # Method to modify the balance

    def get_balance(self):
        return self.__balance  # Method to access the balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
```

In this example:
- The `__balance` attribute is hidden from direct access (private).
- You can deposit money or get the balance using the public methods `deposit()` and `get_balance()`.

---

### **2. ABSTRACTION**

Abstraction is the process of simplifying complex systems by hiding unnecessary details and showing only the essential features. In OOP, abstracting the implementation of objects allows the programmer to focus on the higher-level functionalities.

- **Example**: When you drive a car, you only care about the steering wheel, accelerator, and brakes, not the complex engine workings. This is abstraction.

**Example Code:**
```python
from abc import ABC, abstractmethod

class Animal(ABC):  # Abstract class
    @abstractmethod
    def sound(self):  # Abstract method
        pass

class Dog(Animal):
    def sound(self):
        return "Bark!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

# Create objects
dog = Dog()
cat = Cat()
print(dog.sound())  # Output: Bark!
print(cat.sound())  # Output: Meow!
```

- **Animal** is an abstract class that only defines the interface (`sound()` method) but doesn't implement it.
- **Dog** and **Cat** are concrete subclasses that implement the `sound()` method.

---

### **3. INHERITANCE**

Inheritance allows one class (called a subclass or derived class) to inherit the attributes and methods of another class (called a superclass or base class). This enables code reuse and establishes a hierarchy between classes.

- **Example**: A **Dog** class can inherit from a **Mammal** class and thus gain all the characteristics of a mammal (e.g., warm-blooded, has fur, etc.) while adding its own unique features (e.g., barking).

**Example Code:**
```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):  # Inheriting from Animal class
    def speak(self):
        return f"{self.name} barks!"

dog = Dog("Buddy")
print(dog.speak())  # Output: Buddy barks!
```

- **Dog** inherits from **Animal** and overrides the `speak()` method to add dog-specific behavior.
- **Dog** has access to all the attributes and methods of **Animal**.

---

### **4. POLYMORPHISM**

Polymorphism means "many shapes" and allows different classes to define methods that share the same name but have different implementations. This means you can use the same method name on objects of different classes, but each class can provide its own behavior for that method.

- **Example**: The `speak()` method works for both **Dog** and **Cat**, but they have different implementations (barking vs. meowing).

**Example Code:**
```python
class Dog:
    def speak(self):
        return "Bark!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_speak(animal):
    print(animal.speak())  # Same method name, but behavior depends on the object

# Create objects
dog = Dog()
cat = Cat()

animal_speak(dog)  # Output: Bark!
animal_speak(cat)  # Output: Meow!
```

- Polymorphism lets you treat objects of different classes in the same way (calling `speak()` on both dog and cat), but each object responds differently.

---

### **SUMMARY OF OOP PRINCIPLES**

| **Principle**   | **Description**                                                              |
|-----------------|-------------------------------------------------------------------------------|
| **Encapsulation**| Bundling data and methods inside objects while hiding unnecessary details.    |
| **Abstraction**  | Hiding complexity and showing only essential features.                       |
| **Inheritance**  | Allowing a class to inherit attributes and methods from another class.       |
| **Polymorphism** | Allowing different classes to define methods with the same name but different behavior. |

---

### **BENEFITS OF OOP**

- **Modularity**: Code is organized into separate objects, making it easier to manage and extend.
- **Reusability**: You can reuse existing code through inheritance and polymorphism.
- **Maintainability**: Encapsulation makes it easier to maintain and update code without affecting other parts of the system.
- **Scalability**: OOP helps in managing large and complex software systems by breaking them into smaller, more manageable pieces.

---

### **CONCLUSION**

Object-Oriented Programming (OOP) is a powerful paradigm that organizes code around objects that contain both data and methods. By using the principles of **encapsulation**, **abstraction**, **inheritance**, and **polymorphism**, you can write code that is more modular, flexible, and maintainable.

--- 


---

```python
# Class (Blueprint)
class Car:  
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model  # Attribute

# Creating different objects (instances)
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

print(car1.brand)  # Toyota
print(car2.brand)  # Honda

# Example for flat screen
class flatScreen:
  def __init__(self, brand, size):
    # Attribute 1
    self.size = size 
    # Attribute 2
    self.brand = brand 

# Creating different instances (in otherwords objects)
flatScreen1 = flatScreen("Hisense", "50 inch")
flatScreen2 = flatScreen("Samsung", "32 inch")
flatScreen3 = flatScreen("Sony", "42 inch")

print(flatScreen1.brand)
```
---


