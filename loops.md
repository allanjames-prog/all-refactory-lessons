In Python, **loops** are essential control flow structures that allow you to execute a block of code repeatedly, based on certain conditions. There are two primary types of loops in Python:

1. **`for` loop**
2. **`while` loop**

In addition to the basic loops, there are other important concepts such as **loop control statements** (like `break`, `continue`, and `else`), **nested loops**, and **iterators**.

### 1. **`for` loop**
The `for` loop is used to iterate over a sequence (such as a list, tuple, string, or range) or any iterable object.

#### Basic Syntax:
```python
for item in iterable:
    # Code to execute for each item in the iterable
```

#### Example: Iterating over a list
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```
This will print:
```
apple
banana
cherry
```

#### Example: Using `range()` to iterate a specific number of times
```python
for i in range(5):  # Will iterate from 0 to 4
    print(i)
```
This will print:
```
0
1
2
3
4
```

#### `range()` Function:
`range()` generates a sequence of numbers that can be used with a `for` loop. It can take up to three arguments:
- **start** (optional) — The starting value (inclusive).
- **stop** — The stopping value (exclusive).
- **step** (optional) — The increment (or step size) between numbers.

Example:
```python
for i in range(2, 10, 2):  # Starts from 2, ends before 10, step size is 2
    print(i)
```
This will print:
```
2
4
6
8
```

### 2. **`while` loop**
The `while` loop runs as long as a condition is `True`. It’s generally used when the number of iterations isn’t known beforehand, and you want to repeat the loop until a specific condition is met.

#### Basic Syntax:
```python
while condition:
    # Code to execute as long as condition is True
```

#### Example: Counting with `while`
```python
count = 0
while count < 5:
    print(count)
    count += 1  # Increment count to avoid infinite loop
```
This will print:
```
0
1
2
3
4
```

#### Infinite Loop:
If the condition in a `while` loop never becomes `False`, it creates an **infinite loop**.

Example:
```python
while True:
    print("This is an infinite loop!")
    break  # To exit the infinite loop
```

### 3. **Loop Control Statements**

#### a) `break`
The `break` statement is used to terminate the loop prematurely. It can be used in both `for` and `while` loops.

Example:
```python
for i in range(10):
    if i == 5:
        break  # Exit the loop when i equals 5
    print(i)
```
This will print:
```
0
1
2
3
4
```

#### b) `continue`
The `continue` statement is used to skip the current iteration of the loop and move on to the next iteration.

Example:
```python
for i in range(5):
    if i == 3:
        continue  # Skip iteration when i equals 3
    print(i)
```
This will print:
```
0
1
2
4
```

#### c) `else` with loops
In Python, both `for` and `while` loops can have an `else` clause. The `else` block is executed after the loop finishes normally (i.e., without hitting a `break` statement).

Example:
```python
for i in range(5):
    print(i)
else:
    print("Loop finished without break")
```
This will print:
```
0
1
2
3
4
Loop finished without break
```

If the loop is terminated with a `break`, the `else` block will **not** execute.

### 4. **Nested Loops**
You can use a loop inside another loop, which is called a **nested loop**. This is useful when you need to iterate over multiple dimensions (e.g., matrices or lists of lists).

Example:
```python
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"i = {i}, j = {j}")
```
This will print:
```
i = 0, j = 0
i = 0, j = 1
i = 1, j = 0
i = 1, j = 1
i = 2, j = 0
i = 2, j = 1
```

### 5. **Iterators and `iter()`**
An **iterator** is an object that can be iterated upon, meaning you can traverse through all the values. In Python, iterators are objects that implement two methods:
- `__iter__()` — Returns the iterator object itself.
- `__next__()` — Returns the next item in the sequence.

#### Example of creating and using an iterator:
```python
numbers = [1, 2, 3]
it = iter(numbers)

print(next(it))  # Output: 1
print(next(it))  # Output: 2
print(next(it))  # Output: 3
# next(it) will raise StopIteration error if the list is exhausted
```

### 6. **Comprehensions**
Python allows you to write concise loops in the form of **list comprehensions**, **set comprehensions**, and **dictionary comprehensions**. They are compact and often more efficient.

#### List Comprehension:
```python
squares = [x**2 for x in range(5)]
print(squares)
```
This will print:
```
[0, 1, 4, 9, 16]
```

#### Dictionary Comprehension:
```python
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)
```
This will print:
```
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

#### Set Comprehension:
```python
unique_squares = {x**2 for x in range(5)}
print(unique_squares)
```
This will print:
```
{0, 1, 4, 9, 16}
```

### 7. **Performance Considerations**
When choosing between `for` and `while` loops, remember:
- **`for` loops** are often used when the number of iterations is known or finite, like iterating over items in a list.
- **`while` loops** are better when the number of iterations is not known in advance and depends on a condition that is evaluated during execution.

### 8. **Loop Optimization**
To optimize loops, you can:
- **Use list comprehensions** for more compact and efficient code.
- **Avoid excessive function calls** inside loops that are repeated many times.
- **Use `enumerate()`** instead of manually keeping track of the index when iterating over a sequence.

#### Example of `enumerate()` in a `for` loop:
```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```
This will print:
```
0: apple
1: banana
2: cherry
```

---

### Conclusion
Python loops are powerful tools for iterating over data structures and performing repeated actions. Here's a recap:
- **`for` loop**: Ideal for iterating over a sequence or iterable.
- **`while` loop**: Best when the number of iterations depends on a condition.
- **Control statements** (`break`, `continue`, `else`) enhance the functionality of loops.
- **Nested loops** are used to work with multi-dimensional data.
- **Comprehensions** provide concise and readable ways to create lists, sets, and dictionaries.






























## 🗝️ **Key-Value Pairs in Python**

A **key-value pair** consists of:

- 🔑 **Key**: A unique identifier (e.g., `"name"`, `"age"`).
- 📦 **Value**: The data associated with that key (e.g., `"Allan"`, `25`, or a list).

### 📌 **Example**
```python
student = {"name": "Allan", "age": 25, "city": "Kampala"}
# "name" → Key | "Allan" → Value
# More pairs: "age": 25, "city": "Kampala"
```

---

## 🛠️ **1. Creating Dictionaries (Key-Value Pairs)**

### Method 1: Using `{}`  
```python
person = {
    "name": "James",
    "age": 30,
    "city": "Nairobi"
}
```

### Method 2: Using `dict()`  
```python
person = dict(name="James", age=30, city="Nairobi")
```

### Method 3: Creating Empty Dictionary  
```python
person = {}
person["name"] = "James"
person["age"] = 30
person["city"] = "Nairobi"
```

---

## 🔍 **2. Accessing Values**

### Using Square Brackets
```python
print(person["name"])  # James
# ❗ Raises KeyError if key not found
```

### Using `get()` Method
```python
print(person.get("name"))  # James
print(person.get("gender", "Not Found"))  # Not Found
```

---

## 🔄 **3. Modifying Dictionary**

```python
person["age"] = 31  # Update value
person["country"] = "Kenya"  # Add new key-value pair
```

---

## ❌ **4. Removing Key-Value Pairs**

```python
del person["city"]       # Removes key "city"
age = person.pop("age")  # Removes and returns value of "age"
```

---

## 🔁 **5. Looping Through a Dictionary**

### Loop through keys
```python
for key in person:
    print(key)
```

### Loop through values
```python
for value in person.values():
    print(value)
```

### Loop through key-value pairs
```python
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## ✅ **6. Checking for a Key**

```python
if "name" in person:
    print("Key exists!")
```

---

## ⚙️ **7. Dictionary Methods Overview**

| Method | Description |
|--------|-------------|
| `keys()` | Returns all keys |
| `values()` | Returns all values |
| `items()` | Returns key-value pairs as tuples |
| `get(key, default)` | Returns value or default |
| `pop(key, default)` | Removes and returns value |
| `update(dict2)` | Merges another dictionary |

### Example:
```python
print(person.keys())     # dict_keys(['name', 'country'])
print(person.values())   # dict_values(['James', 'Kenya'])
print(person.items())    # dict_items([('name', 'James'), ('country', 'Kenya')])
```

---

## 🧩 **8. Nested Dictionaries**

```python
students = {
    "student1": {"name": "Allan", "age": 22},
    "student2": {"name": "Dorothy", "age": 23}
}
print(students["student1"]["name"])  # Allan
```

---

## 📚 **9. Other Structures with Key-Value Pairs**

### List of Dictionaries
```python
people = [
    {"name": "Alice", "age": 28},
    {"name": "Bob", "age": 25}
]
```

### Tuples for Key-Value Pairs
```python
pairs = (("name", "James"), ("age", 30))
person = dict(pairs)
```

---

## 🚀 **10. Use Cases**

- 🗃️ Databases (user data)
- 🌐 API Responses (JSON)
- ⚙️ Configuration files
- ⚡ Caching (fast data access)

---

## 🔄 **11. Converting to/from JSON**

### Convert Dictionary → JSON
```python
import json
data = {"name": "James", "age": 30}
json_data = json.dumps(data)
print(json_data)  # {"name": "James", "age": 30}
```

### Convert JSON → Dictionary
```python
dict_data = json.loads(json_data)
print(dict_data["name"])  # James
```

---

## 🎯 **Relevance of Key-Value Pairs**

- Essential for efficient **data storage & retrieval**.
- Used widely in **Python dictionaries**, **JSON**, and **APIs**.
- `.keys()`, `.values()`, `.items()` make iteration and data handling clean and powerful.







