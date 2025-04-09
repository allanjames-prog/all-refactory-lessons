## 🏷️ **Conditional Statements in Python**

Conditional statements allow your program to execute different blocks of code based on certain conditions. The main conditional statements in Python are `if`, `elif`, and `else`.

---

### 📌 **1. The `if` Statement**

The `if` statement evaluates a condition and executes a block of code if the condition is `True`.

#### 🛠️ **Syntax:**
```python
if condition:
    # Code block executed if condition is True
```

#### 📝 **Example:**
```python
age = 18
if age >= 18:
    print("You are an adult.")  # This runs because the condition is True
```

---

### 📌 **2. The `if-else` Statement**

The `else` statement is used to execute a block of code when the `if` condition is `False`.

#### 🛠️ **Syntax:**
```python
if condition:
    # Executes if condition is True
else:
    # Executes if condition is False
```

#### 📝 **Example:**
```python
age = 16
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")  # This runs because the condition is False
```

---

### 📌 **3. The `if-elif-else` Statement**

The `elif` (short for "else if") allows checking multiple conditions.

#### 🛠️ **Syntax:**
```python
if condition1:
    # Executes if condition1 is True
elif condition2:
    # Executes if condition1 is False and condition2 is True
else:
    # Executes if all conditions are False
```

#### 📝 **Example:**
```python
score = 75
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")  # This runs because 75 >= 70
else:
    print("Grade: F")
```

---

### 📌 **4. Nested `if` Statements**

You can nest `if` statements inside other `if` statements to handle more complex conditions.

#### 🛠️ **Example:**
```python
num = 10
if num > 0:
    print("Positive number")
    if num % 2 == 0:
        print("Even number")  # This runs because num is positive and even
```

---

### 📌 **5. Logical Operators in Conditional Statements**

Logical operators combine multiple conditions:
- `and`: Returns `True` if both conditions are `True`.
- `or`: Returns `True` if at least one condition is `True`.
- `not`: Negates a condition (True becomes False and vice versa).

#### 🛠️ **Example:**
```python
x = 7
if x > 5 and x < 10:
    print("x is between 5 and 10")  # This runs because both conditions are True
```

---

### 📌 **6. Conditional Expressions (Ternary Operator)**

A shorthand way of writing `if-else` expressions using the ternary operator:

```python
value_if_true if condition else value_if_false
```

#### 📝 **Example:**
```python
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult
```

---

### 📌 **7. Using `in` with `if` Statements**

You can check if a value exists in a list, tuple, dictionary, or string.

#### 🛠️ **Example:**
```python
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list.")
```

---

### 📌 **8. `pass` Statement in Conditional Blocks**

The `pass` statement is used when a block is syntactically required but you don’t want to execute any code.

#### 🛠️ **Example:**
```python
x = 10
if x > 5:
    pass  # Placeholder for future code
```

---

### 📌 **9. Short-Circuiting in Logical Operators**

- For `and`: If the first condition is `False`, Python doesn’t evaluate the second condition.
- For `or`: If the first condition is `True`, Python doesn’t evaluate the second condition.

#### 📝 **Example:**
```python
x = 10
y = 0
if y != 0 and x / y > 5:
    print("This won't run")  # The second condition is never checked to avoid ZeroDivisionError
```

---

### 📌 **10. Comparing Values in Conditional Statements**

Python supports different comparison operators in conditional statements:
- `==`: Equal to
- `!=`: Not equal to
- `>`: Greater than
- `<`: Less than
- `>=`: Greater than or equal to
- `<=`: Less than or equal to

#### 🛠️ **Example:**
```python
a = 5
b = 10
print(a == b)  # False
print(a != b)  # True
print(a > b)   # False
print(a < b)   # True
print(a >= b)  # False
print(a <= b)  # True
```

---

### 📌 **11. Handling Multiple Conditions with `match` (Python 3.10+)**

Python 3.10 introduced the `match` statement, similar to `switch-case` in other languages.

#### 🛠️ **Example:**
```python
status_code = 200
match status_code:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown Status")  # Default case
```

---

### 📝 **Key Takeaways**
- Use `if`, `elif`, and `else` for flow control.
- Combine conditions using logical operators (`and`, `or`, `not`).
- Use ternary expressions for compact `if-else` statements.
- Use `match` for multi-case conditions (Python 3.10+).
- Short-circuiting improves performance in complex conditions.

---

Let me know if you'd like any more clarification or examples!