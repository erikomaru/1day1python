# Day 9: Python File I/O

## Goal

Learn how to write data to a text file, append new data, and read saved data.

## What I Learned

- `open()` opens a file.
- `"w"` opens a file for writing and overwrites existing content.
- `"a"` opens a file for appending without deleting existing content.
- `"r"` opens a file for reading.
- `write()` writes strings to a file.
- `read()` reads the file content.
- `with` automatically closes a file when the block finishes.
- `\n` adds a newline.
- `list.append()` adds an element to a list.

## Practice Code

```python
location = ["0", "0", "2", "4", "6", "8", "0", "0"]

new_point = input("Enter lat/lon:")
location.append(new_point)

with open("location.txt", "w") as file:
    for point in location:
        file.write(point + "\n")

with open("location.txt", "r") as file:
    content = file.read()

print("saved")
print(content)
```

## What I Learned from Debugging

### 1. Using `append()`

Incorrect:

```python
location.append = input("Enter lat/lon:")
```

Correct:

```python
location.append(input("Enter lat/lon:"))
```

`append()` is a method, so I need parentheses to call it.

### 2. Understanding File Modes

| Mode | Purpose | Existing content |
|---|---|---|
| `"r"` | Read | Preserved |
| `"w"` | Write | Overwritten |
| `"a"` | Append | Preserved; new content is added |

Opening a file in append mode does not write anything by itself. I must call `file.write()` to add content.

### 3. Appending Directly to a File

```python
new_point = input("Enter lat/lon:")

with open("location.txt", "a") as file:
    file.write(new_point + "\n")
```

This adds a new line to the file without overwriting its existing content.

## Key Takeaway

A Python list and a text file are different things. `list.append()` changes a list in memory, while `file.write()` saves text to a file.

## Next Challenge

- Input multiple coordinates.
- Store latitude and longitude separately.
- Handle invalid input with `try` and `except`.
