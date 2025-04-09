## 🧺 **Tuples in Python**

A **tuple** is an **ordered**, **immutable** collection of items in Python. Similar to lists, but once created, tuples **cannot be modified**.

---

### 🔑 **Key Features of Tuples**

1. ✅ **Ordered** – Elements maintain insertion order.
2. 🔒 **Immutable** – Cannot be changed after creation (no add, remove, or update).
3. ♻️ **Allows Duplicates** – Values can repeat.
4. 🔀 **Mixed Data Types** – Can store strings, numbers, lists, etc.
5. ⚡ **Faster Than Lists** – More memory efficient and performant.

---

### 🛠️ **Creating Tuples**

```python
# Tuple with multiple values
my_tuple = (10, 20, 30, "Hello", 50.5)
print(my_tuple)  # Output: (10, 20, 30, 'Hello', 50.5)

# Tuple without parentheses (comma-separated values)
my_tuple = 10, 20, 30
print(my_tuple)  # Output: (10, 20, 30)
```

---

### 🎯 **Accessing Elements**

```python
print(my_tuple[0])   # Output: 10 (First element)
print(my_tuple[-1])  # Output: 30 (Last element)
```

---

### 📦 **Tuple Unpacking**

```python
a, b, c = (1, 2, 3)
print(a, b, c)  # Output: 1 2 3
```

---

### 🧱 **Immutability Example**

```python
my_tuple[1] = 100  
# ❌ TypeError: 'tuple' object does not support item assignment
```

---

### 🔧 **Tuple Methods**

> Tuples have **limited built-in methods**, unlike lists.

```python
t = (1, 2, 3, 2, 2, 4)

print(len(t))      # Output: 6 (Total number of elements)
print(t.count(2))  # Output: 3 (Occurrences of 2)
print(t.index(3))  # Output: 2 (First index of 3)
```

---

### 💡 **When to Use Tuples Instead of Lists?**

- When **data should not be changed**.
- When **performance matters** (tuples are faster).
- For **fixed collections** like coordinates, RGB values, or database records.
