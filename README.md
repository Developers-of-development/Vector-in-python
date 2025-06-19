# 🚀 Vector Implementation in Python

A custom-built vector class in Python that replicates features of C++ STL Vectors — with user-defined methods for managing dynamic arrays including insertion, deletion, size tracking, searching, and more!

## 👨‍💻 Author

**Rustam Singh Bhadouriya**  
Class 9 | Python & C++ Developer | AI-ML Aspirant  
Founder @ [Developers-of-development](https://github.com/Developers-of-development)  

📌 *“Code not for syntax, but for structure and soul!”*

---

## 📂 Project Structure

**vector.py**
<pre>└── class vector
├── init() # Initialize vector with list
├── push_back() # Add value at end
├── pop_back() # Remove last element
├── size() # Get size of vector
├── front() # First element
├── back() # Last element
├── at() # Access by index
├── ease() # Remove specific value
├── In() # Find value's index
└── show() # Display vector content</pre>


---

## 🧠 Features

- ➕ **push_back(value)** – Add element to the end.
- ➖ **pop_back()** – Remove last element.
- 🔢 **size()** – Get total elements.
- ⏩ **front() / back()** – Get first or last element.
- 🔍 **at(index)** – Get element at specific index with bounds check.
- 🧽 **ease(value)** – Remove given value from vector.
- 👁 **show()** – Print all elements cleanly.
- 🔎 **In(value)** – Check if a value exists and return index.

---

## 🛠 Example Usage

```python
from vector import vector

vec = vector([1, 2, 3, 4])

vec.push_back(5)
vec.pop_back()
print(vec.size())
print(vec.front())
print(vec.back())
print(vec.at(2))
vec.ease(3)
vec.show()
print(vec.In(4))
```

```bash
git clone https://github.com/Developers-of-developmen/vector-in-python.git
```

