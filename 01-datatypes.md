## 🧠 What Are Data Types?

In Python, **data types** define the kind of value a variable holds. Python automatically assigns the type when you create a variable (this is called **dynamic typing**).

---

## 🧱 Basic Built-in Data Types

### 1. **Numeric Types**

| Type       | Description                | Example       |
|------------|----------------------------|---------------|
| `int`      | Integer (whole numbers)     | `x = 5`       |
| `float`    | Decimal numbers             | `y = 3.14`    |
| `complex`  | Complex numbers             | `z = 1 + 2j`  |

```python
a = 10        # int
b = 3.14      # float
c = 2 + 3j    # complex
```

---

### 2. **Text Type**

| Type     | Description | Example        |
|----------|-------------|----------------|
| `str`    | String       | `name = "Allan"` |

```python
greeting = "Hello, World!"
```

---

### 3. **Boolean Type**

| Type      | Description               | Example         |
|-----------|---------------------------|-----------------|
| `bool`    | Logical values (True/False) | `flag = True`   |

```python
is_ready = False
```

---

### 4. **Sequence Types**

| Type     | Description               | Example               |
|----------|---------------------------|------------------------|
| `list`   | Ordered, changeable        | `[1, 2, 3]`            |
| `tuple`  | Ordered, unchangeable      | `(1, 2, 3)`            |
| `range`  | Sequence of numbers        | `range(5)`            |

```python
fruits = ["apple", "banana"]
point = (10, 20)
nums = range(5)  # 0 to 4
```

---

### 5. **Set Types**

| Type     | Description                 | Example             |
|----------|-----------------------------|----------------------|
| `set`    | Unordered, unique elements  | `{1, 2, 3}`          |
| `frozenset` | Immutable version of set  | `frozenset([1, 2])`  |

```python
colors = {"red", "green", "blue"}
```

---

### 6. **Mapping Type**

| Type      | Description               | Example                         |
|-----------|---------------------------|----------------------------------|
| `dict`    | Key-value pairs           | `{"name": "James", "age": 25}`  |

```python
student = {"name": "James", "age": 22}
```

---

### 7. **None Type**

| Type     | Description                 | Example     |
|----------|-----------------------------|-------------|
| `None`   | Represents "no value"        | `x = None`  |

---

## 🧪 Type Checking and Conversion

### ✅ Checking the type
```python
x = 10
print(type(x))  # <class 'int'>
```

### 🔄 Type Conversion (Casting)
```python
x = int("5")       # string to int
y = float("3.14")  # string to float
z = str(100)       # int to string
```

---

## ⚙️ Mutability Summary

| Type       | Mutable?  |
|------------|-----------|
| `int`      | ❌ No     |
| `float`    | ❌ No     |
| `str`      | ❌ No     |
| `list`     | ✅ Yes    |
| `tuple`    | ❌ No     |
| `dict`     | ✅ Yes    |
| `set`      | ✅ Yes    |

---

## 🎯 Bonus: Use Cases

| Data Type | Common Uses                      |
|-----------|----------------------------------|
| `int`     | Counting, IDs                    |
| `float`   | Prices, measurements             |
| `str`     | Names, text data                 |
| `list`    | Collections you can change       |
| `tuple`   | Fixed sets of values             |
| `dict`    | Records, structured data         |
| `set`     | Unique items, fast lookups       |
| `bool`    | Conditions, flags                |

---
