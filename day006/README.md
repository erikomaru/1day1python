# Day 6: Python Data Structures

## What I Learned

### 1. Dictionaries (`dict`)

- Store data as key-value pairs.
- Access values using keys, such as `prices["apple"]`.
- Add new items and update existing values.
- Use `items()` to iterate over keys and values.
- Use `values()` and `sum()` to calculate the total.
- Use f-strings to format output.

### 2. Tuples (`tuple`)

- Store a sequence of values.
- Access elements using indexes starting from `0`.
- Tuples cannot be modified after creation.

### 3. Sets (`set`)

- Store unique values without duplicates.
- Convert a list into a set using `set()`.
- Add elements using `add()`.
- Check whether an element exists using `in`.

## What I Built

### 1. Managing Product Prices with a Dictionary

```python
prices = {
    "apple": 150,
    "banana": 100,
    "kiwi": 200
}

print(prices["apple"])
print(prices["banana"])

prices["peach"] = 300
prices["apple"] = 170

for item, cost in prices.items():
    print(f"{item} is {cost} yen")

print("All items cost is", sum(prices.values()))
```

**Output:**
```text
150
100
apple is 170 yen
banana is 100 yen
kiwi is 200 yen
peach is 300 yen
All items cost is 770
```

### 2. Accessing Tuple Elements

```python
station = (5, 6)

latitude = station[0]
longitude = station[1]

print(latitude, longitude)
```

**Output:**
```text
5 6
```

### 3. Removing Duplicates with a Set

```python
tags = ["ai", "python", "python"]

uniqtags = set(tags)

print(uniqtags)
print(len(uniqtags))

uniqtags.add("pyai")

print("ROS2" in uniqtags)
```

The set removes duplicate values. Since `"python"` appears twice, `uniqtags` contains two unique elements before adding `"pyai"`.

## Key Takeaways

- Dictionaries are useful for mapping names to values.
- `items()` provides key-value pairs for iteration.
- `sum()` can calculate the total of dictionary values.
- Tuples are suitable for fixed collections of values.
- Sets are useful for removing duplicates and checking membership.
- Meaningful variable names make code easier to understand.

## Next Steps

- Practice adding and deleting dictionary entries.
- Experiment with modifying a tuple and observe the error.
- Compare `len(tags)` and `len(uniqtags)`.
- Build a small shopping cart that tracks products and prices.