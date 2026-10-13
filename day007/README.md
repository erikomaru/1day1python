# Day 7: Python Functions

## What I Learned

- Define a function using `def`.
- Pass data to a function through parameters.
- Use `for` loops to iterate over dictionary items.
- Use `print()` to display information.
- Use `return` to send a value back to the caller.
- Understand the difference between `print()` and `return`.

## What I Built

I created a function that displays product prices and returns the total cost.

```python
def print_prices(prices):
    for item, cost in prices.items():
        print(f"{item} is {cost} yen")
    return sum(prices.values())

prices = {
    "apple": 50,
    "sea": 400,
    "forest": 330
}

print("Total:", print_prices(prices))
```

### Output

```text
apple is 50 yen
sea is 400 yen
forest is 330 yen
Total: 780
```

## Key Takeaways

### 1. Function Definition

- `def` defines a function.
- Parameters receive values passed to the function.
- A function executes when it is called.

### 2. `print()` vs. `return`

- `print()` displays a value on the screen.
- `return` sends a value back to the caller.
- If a function has no explicit `return`, it returns `None` by default.

### 3. Using Dictionaries in Functions

- `items()` provides key-value pairs for iteration.
- `values()` retrieves the dictionary's values.
- `sum()` calculates the total of numeric values.

## What I Learned from Practice

I learned that a function can both display information using `print()` and return a calculated result using `return`.

I also practiced passing a dictionary to a function and calculating the total price of its values.

## Next Steps

- Create a separate function to calculate the total price.
- Calculate the average price using a function.
- Practice writing functions that accept multiple arguments.
