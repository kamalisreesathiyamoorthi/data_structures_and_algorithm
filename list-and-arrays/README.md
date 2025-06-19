# 📘 Arrays vs Lists in Python

## 📝 What is a List in Python?
- A **list** is a built-in **dynamic array** in Python.
- Can store elements of **different data types**
- Automatically resizes (dynamic)
- Highly flexible and easy to use

### 🔹 Example:
```python
my_list = [1, "hello", 3.14, True]
print(my_list[1])  # Output: hello
```

## 🧪 Common List Operations
```python
l = [1, 2, 3]
l.append(4)     # [1, 2, 3, 4]
l.pop()         # [1, 2, 3]
l.insert(1, 10) # [1, 10, 2, 3]
l.remove(2)     # [1, 10, 3]
l.sort()        # [1, 3, 10]
```

---

# 🧮 What is an Array in Python?
- Python provides a separate **array** module to work with typed arrays (like C-style arrays).
- Stores elements of same data type only
- More memory-efficient than lists
- Best suited for large numerical datasets

### 🔹 Example:
```python
import array
my_array = array.array('i', [1, 2, 3, 4])  # 'i' = integer
print(my_array[2])  # Output: 3
```

## 🧪 Common Array Operations
```python
import array

a = array.array('i', [10, 20, 30])
a.append(40)        # [10, 20, 30, 40]
a.insert(1, 15)     # [10, 15, 20, 30, 40]
a.pop()             # [10, 15, 20, 30]
```

## Type Codes for array.array
| Type Code | Python Type |
|-----------|-------------|
| i         | int         |
| f         | float       |
| d         | float       |
| u         | unicode     |

---
