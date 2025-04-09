# 📘 COMPARISON, LOGICAL, MEMBERSHIP, AND IDENTITY OPERATORS

---

## ✅ COMPARISON OPERATORS
**Used to compare two values. The result is always a Boolean (`True` or `False`).**

```python
# Declare two numeric variables for comparison
comp1 = 20
comp2 = 40

# Less than
print(comp1 < comp2)   # True

# Greater than
print(comp1 > comp2)   # False

# Greater than or equal to
print(comp1 >= comp2)  # False

# Less than or equal to
print(comp1 <= comp2)  # True

# Not equal
print(comp1 != comp2)  # True

# Equal
print(comp1 == comp2)  # False
```

---

## ✅ LOGICAL OPERATORS
**Used to combine conditional statements.**

| Operator | Meaning                      | Example             |
|----------|------------------------------|---------------------|
| `and`    | True if both are True        | `x > 3 and x < 10`  |
| `or`     | True if at least one is True | `x > 3 or x < 2`    |
| `not`    | Inverts the result           | `not(x > 3)`        |

```python
# Declare variables
log1 = 5
log2 = 6

# AND: returns True only if both are True
print((log1 > log2) and (log2 < log1))  # False

# NOT: negates the result of the condition
print(not (log2 < log1))  # True

# OR: returns True if at least one condition is True
print((log1 > log2) or (log2 < log1))  # False

# Logical evaluations with Boolean constants
print(True and True)   # True
print(True and False)  # False
print(not True)        # False
print(True or True)    # True
print(True or False)   # True
print(False or False)  # False
```

---

## ✅ SPECIAL OPERATORS IN PYTHON

---

### 1️⃣ MEMBERSHIP OPERATORS  
**Check if a value exists within a container (like a list, tuple, set, or string).**

| Operator | Description               |
|----------|---------------------------|
| `in`     | True if value is present  |
| `not in` | True if value is absent   |

```python
# Set of values
members = {20, 30, 40, 50}

# Check membership
print(20 in members)       # True
print(20 not in members)   # False

# String membership
name = "Ozzy"
print("o" not in name)     # True (case-sensitive)
print("O" not in name)     # False
```

---

### 2️⃣ IDENTITY OPERATORS  
**Used to compare the memory locations of two objects.**

| Operator  | Description                            |
|-----------|----------------------------------------|
| `is`      | True if both refer to the same object  |
| `is not`  | True if they don’t refer to the same object |

```python
# Identity comparison
print(20 is not members)   # True (20 is not the same object as the set)
print(20 is 20)            # True (both are the same integer object)
```

---

## 📝 NOTE

1. Always write comments **above the line** you're referring to.
2. Follow correct **English grammar and punctuation** for clarity.
3. There is an **assignment starting on Thursday** (check Google Classroom for details).

