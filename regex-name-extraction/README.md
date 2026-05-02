# Name Extraction with Regex & OS Path

Extract a first name, middle name, and last name from a text file using Python regex — and print your local file path using the `os` module.

---

## Project Overview

This project demonstrates two fundamental Python skills:

1. **File I/O + Regex** — reading a `.txt` file and extracting structured data (name parts) using regular expressions.
2. **OS Module** — using `os.getcwd()` to retrieve and display the current working directory path.

---

## Folder Structure

```
/regex
│
├── myname.txt          # Text file containing full name
├── name_extract.py     # Main Python script
├── regex_output.png    # Screenshot of output
└── README.md
```

---

## How It Works

1. The script opens `myname.txt` and reads the full name as a string.
2. A regex pattern matches the three name components: first, middle, and last.
3. The `os` module prints the full path to the current working directory.

---

## The Code

**myname.txt**
```
Anita Ewomazino Okele
```

**name_extract.py**
```python
import re
import os

with open("myname.txt") as file:
    full_name = file.read().strip()

match = re.match(r'(\w+)\s+(\w+)\s+(\w+)', full_name)

if match:
    first_name = match.group(1)
    middle_name = match.group(2)
    last_name = match.group(3)

    print("First Name:", first_name)
    print("Middle Name:", middle_name)
    print("Last Name:", last_name)
else:
    print("Name format not recognized.")

full_path = os.getcwd()
print("full path to file:", full_path)
```

---

## Expected Output

```
First Name: Anita
Middle Name: Ewomazino
Last Name: Okele

full path to file: /home/ahnnie/Documents/Projects/pythonbeginnersclass/regex
```

---

## Run the Script

```bash
python3 name_extract.py
```

---

## Key Concepts

- `re.match()` — matches a pattern at the start of a string
- `(\w+)` — captures one or more word characters (letters, digits, underscore)
- `\s+` — matches one or more whitespace characters between names
- `match.group(n)` — retrieves the nth captured group from the match
- `os.getcwd()` — returns the current working directory as a string

---

## Author

**Anita Okele** | November 2025