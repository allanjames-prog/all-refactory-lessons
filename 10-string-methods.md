## **Python String Methods and Their Descriptions**

### 📝 **Case Conversion Methods**
| Method        | Description |
|---------------|-------------|
| `capitalize()` | Converts the first character to upper case |
| `casefold()`   | Converts string into lower case (more aggressive than `lower()`) |
| `lower()`      | Converts a string into lower case |
| `upper()`      | Converts a string into upper case |
| `swapcase()`   | Swaps case: lowercase becomes uppercase and vice versa |
| `title()`      | Converts the first character of each word to upper case |

---

### 🔍 **Search & Find Methods**
| Method      | Description |
|-------------|-------------|
| `find()`    | Returns the first position of a specified value |
| `rfind()`   | Returns the last position of a specified value |
| `index()`   | Same as `find()`, but raises an error if not found |
| `rindex()`  | Same as `rfind()`, but raises an error if not found |
| `count()`   | Returns the number of times a value appears in the string |
| `startswith()` | Returns True if the string starts with a specified value |
| `endswith()`   | Returns True if the string ends with a specified value |

---

### 🔡 **Validation Methods (Returns True/False)**
| Method        | Description |
|---------------|-------------|
| `isalnum()`    | Checks if all characters are alphanumeric |
| `isalpha()`    | Checks if all characters are alphabetic |
| `isascii()`    | Checks if all characters are ASCII |
| `isdecimal()`  | Checks if all characters are decimals |
| `isdigit()`    | Checks if all characters are digits |
| `isnumeric()`  | Checks if all characters are numeric |
| `isidentifier()` | Checks if the string is a valid identifier |
| `islower()`    | Checks if all characters are lowercase |
| `isupper()`    | Checks if all characters are uppercase |
| `isprintable()`| Checks if all characters are printable |
| `isspace()`    | Checks if the string contains only whitespace |
| `istitle()`    | Checks if string follows title case rules |

---

### 🧱 **Formatting Methods**
| Method        | Description |
|---------------|-------------|
| `center()`     | Returns a centered string |
| `ljust()`      | Returns a left-justified string |
| `rjust()`      | Returns a right-justified string |
| `zfill()`      | Pads the string with zeros on the left |
| `format()`     | Formats values in a string |
| `format_map()` | Same as `format()` but takes a dictionary |
| `expandtabs()` | Sets the tab size in a string |

---

### ✂️ **Modification Methods**
| Method        | Description |
|---------------|-------------|
| `replace()`    | Replaces a value with another |
| `strip()`      | Removes whitespace from both ends |
| `lstrip()`     | Removes leading whitespace |
| `rstrip()`     | Removes trailing whitespace |

---

### 🧩 **Splitting and Joining**
| Method        | Description |
|---------------|-------------|
| `split()`      | Splits the string at a separator into a list |
| `rsplit()`     | Splits from the right side |
| `splitlines()` | Splits at line breaks |
| `join()`       | Joins iterable elements into a string |

---

### 🔁 **Translation & Encoding**
| Method        | Description |
|---------------|-------------|
| `maketrans()`  | Creates a mapping table for translation |
| `translate()`  | Translates string using the mapping table |
| `encode()`     | Returns an encoded version of the string |

---

### 🧪 **Partitioning Methods**
| Method          | Description |
|-----------------|-------------|
| `partition()`    | Splits the string into 3 parts using a separator |
| `rpartition()`   | Same as `partition()`, but splits from the right |

