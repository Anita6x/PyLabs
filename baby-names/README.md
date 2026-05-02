# Baby Names — Regex Extraction, Bubble Sort & Binary Search

Extract baby names from an HTML file using regex, sort them with bubble sort, and search them with binary search — all without relying on Python's built-in sort or search functions.

---

## Project Overview

This project demonstrates three core computer science concepts implemented from scratch in Python:

| Concept | Implementation |
|---|---|
| Data extraction | Regex on raw HTML |
| Sorting algorithm | Bubble sort |
| Search algorithm | Binary search |

No `sorted()`. No `list.sort()`. No `in` operator for search. Everything is hand-built.

---

## Folder Structure

```
/babynames
│
├── baby2008.html           # Source HTML file with baby names
├── name_extract.py         # Main script
├── sorted_babynames.txt    # Output: sorted names with index
└── README.md
```

---

## How It Works

### 1. Read the HTML file

```python
with open("baby2008.html") as file:
    content = file.read()
```

### 2. Extract names with regex

```python
import re
names = re.findall(r'([A-Za-z]+)', content)
```

The pattern `([A-Za-z]+)` matches any HTML table cell containing only letters — isolating the name values from the surrounding markup.

### 3. Sort with bubble sort

```python
def bubble_sort(names):
    n = len(names)
    for i in range(n):
        for j in range(0, n - i - 1):
            if names[j].lower() > names[j + 1].lower():
                names[j], names[j + 1] = names[j + 1], names[j]
    return names

sorted_names = bubble_sort(names)
```

Bubble sort compares adjacent elements and swaps them if out of order. It repeats until no swaps are needed. Time complexity: O(n²).

### 4. Save sorted names to file

```python
with open("sorted_babynames.txt", "w") as f:
    for index, name in enumerate(sorted_names):
        f.write(f"{index}: {name}\n")
```

### 5. Search with binary search

```python
def binary_search(names, target):
    low, high = 0, len(names) - 1
    target = target.lower()
    while low <= high:
        mid = (low + high) // 2
        mid_val = names[mid].lower()
        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

result = binary_search(sorted_names, "Emily")
if result != -1:
    print(f"Emily found at index {result}")
else:
    print("Name not found.")
```

Binary search requires a sorted list. It halves the search space on every step. Time complexity: O(log n).

---

## Sample Output

```
Sorted names have been saved to sorted_babynames.txt
Emily found at index 654
```

---

## Run the Script

```bash
python3 name_extract.py
```

---

## Algorithm Complexity

| Algorithm | Time Complexity | Space Complexity |
|---|---|---|
| Bubble Sort | O(n²) | O(1) |
| Binary Search | O(log n) | O(1) |

---

## Author

**Anita Okele** | November 2025