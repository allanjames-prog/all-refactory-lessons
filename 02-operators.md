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

