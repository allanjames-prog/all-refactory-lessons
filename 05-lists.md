# **LISTS and DICTIONARIES**

## **Lists in Python**

A **list** in Python is an **ordered, mutable collection** of items that can hold elements of different data types — integers, floats, strings, objects, even other lists. Lists are one of the most commonly used data structures in Python.

---

### **1. Creating Lists**

**1.1 Empty List**
```python
my_list = []
my_list = list()  # Using the list() constructor
```

**1.2 List with Elements**
```python
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.5, True]
nested = [[1, 2], [3, 4]]
```

---

### **2. Accessing Elements**

**2.1 Indexing (Starts at 0)**
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])     # apple
print(fruits[1])     # banana
print(fruits[-1])    # cherry (last item)
```

**2.2 Slicing [start:stop:step]**
```python
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])    # [20, 30, 40]
print(numbers[:3])     # [10, 20, 30]
print(numbers[::2])    # [10, 30, 50]
```

---

### **3. Modifying Lists**

**3.1 Changing Elements**
```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']
```

**3.2 Adding Elements**
```python
fruits.append("mango")
fruits.insert(1, "orange")
fruits.extend(["grapes", "kiwi"])
print(fruits)  
# ['apple', 'orange', 'blueberry', 'cherry', 'mango', 'grapes', 'kiwi']
```

**3.3 Removing Elements**
```python
fruits.remove("cherry")
popped_item = fruits.pop(2)
del fruits[0]
fruits.clear()  # Empties the list
```

---

### **4. List Operations**

**4.1 Concatenation and Repetition**
```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2        # [1, 2, 3, 4, 5, 6]
repeated = list1 * 3            # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

**4.2 Membership Testing**
```python
print(3 in list1)         # True
print(7 not in list1)     # True
```

---

### **5. Iterating Through Lists**

```python
fruits = ["apple", "banana", "cherry"]

# Loop through items
for fruit in fruits:
    print(fruit)

# Loop with index
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

---

### **6. Useful List Methods**

| Method            | Description                                |
|-------------------|--------------------------------------------|
| `append(x)`       | Adds x to the end                          |
| `insert(i, x)`    | Inserts x at index i                       |
| `extend(iterable)`| Adds multiple elements                     |
| `remove(x)`       | Removes first occurrence of x              |
| `pop(i)`          | Removes and returns element at index i     |
| `clear()`         | Removes all elements                       |
| `index(x)`        | Returns index of first occurrence of x     |
| `count(x)`        | Counts occurrences of x                    |
| `sort()`          | Sorts the list                             |
| `reverse()`       | Reverses the list                          |
| `copy()`          | Returns a shallow copy                     |

**Example:**
```python
numbers = [3, 1, 4, 1, 5, 9, 2]
numbers.sort()       # [1, 1, 2, 3, 4, 5, 9]
numbers.reverse()    # [9, 5, 4, 3, 2, 1, 1]
```

---

### **7. List Comprehension**

A concise way to create lists:
```python
squares = [x**2 for x in range(1, 6)]          # [1, 4, 9, 16, 25]
even_numbers = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

---

### **8. Copying Lists**

**8.1 Incorrect Copy (Reference)**
```python
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)  # [1, 2, 3, 4]
```

**8.2 Correct Copy**
```python
list2 = list1.copy()
# or
list2 = list1[:]
list2.append(4)
print(list1)  # [1, 2, 3]
```

---

### **9. Nested Lists**

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # 6
```

---

### **10. Common Mistakes**

**10.1 IndexError**
```python
fruits = ["apple", "banana"]
print(fruits[2])  # IndexError: list index out of range
```

**10.2 Using `=` Instead of `copy()`**
```python
list1 = [1, 2, 3]
list2 = list1  # Refers to same list!
```

---

### **When to Use Lists**
- When you need an **ordered collection**.
- When you want to **modify elements** (unlike tuples).
- When you need **fast iteration** and **random access**.

---

### **Relevance**
✔ Lists are ordered and mutable.  
✔ Support indexing, slicing, and iteration.  
✔ Can hold different data types.  
✔ Provide many methods for manipulation.  
✔ Use list comprehension for efficient construction.  
✔ Use `.copy()` to avoid reference issues.

