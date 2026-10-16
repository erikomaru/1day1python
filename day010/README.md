# Day 10: Working with CSV Files

## Goal

Learn how to write, append, and read CSV files, then calculate the average of numeric data.

## What I Learned

- `import csv`: Import Python's built-in CSV module.
- `csv.writer()`: Create a CSV writer.
- `writer.writerows()`: Write multiple rows.
- `writer.writerow()`: Write one row.
- `csv.reader()`: Read a CSV file row by row.
- `next(reader)`: Skip the header row.
- `float()`: Convert a string to a floating-point number.
- `list.append()`: Add an item to a list.
- `sum()` and `len()`: Calculate the sum and the number of items.

## Practice Code

```python
import csv

locations = [
    ["name", "latitude", "longitude"],
    ["Tokyo", 35.6762, 139.6503],
    ["Osaka", 34.6937, 135.5023],
    ["Fukuoka", 33.5902, 130.4017],
]

locations.append(["aichi", 3, 33])

with open("location.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(locations)

print("CSV saved")

with open("location.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Yokohama", 2, 2])

print(locations)

latitudes = []

with open("location.csv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        latitude = float(row[1])
        latitudes.append(latitude)

lat_ave = sum(latitudes) / len(latitudes)

print(latitudes, lat_ave)
```

## Key Concepts

### 1. File Modes

| Mode | Purpose |
|---|---|
| `"r"` | Read a file |
| `"w"` | Write a file, overwriting existing content |
| `"a"` | Append data to the end of a file |

### 2. Lists and CSV Files Are Different

`locations.append()` changes the Python list in memory.

`writer.writerow()` changes the CSV file.

Appending a row to a CSV file does not automatically add that row to the Python list.

### 3. Calculating an Average

```python
lat_ave = sum(latitudes) / len(latitudes)
```

- `sum(latitudes)` calculates the total.
- `len(latitudes)` counts the items.
- Dividing the total by the number of items gives the average.

## Important Note

The sample coordinates for Aichi and Yokohama are placeholder values. The program calculates the average correctly, but the result is not a meaningful geographic average.

Also, running the script rewrites `location.csv` before appending Yokohama. The Yokohama row is therefore added once per execution, rather than accumulating across executions.

## Next Challenge

Use the same CSV techniques to manage learning records:

- Save the date, topic, and study time.
- Read the saved records.
- Calculate total and average study time.
