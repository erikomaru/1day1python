# Day 5 — Python Lists

## Today's Learning Goals

- Create and use lists
- Add elements with `append()`
- Access list elements using a `for` loop
- Count elements with `len()`
- Use `while` to repeat input
- Use `break` and `continue` to control loops
- Validate user input

## What I Built

A shopping-list program that:
- Accepts food items from the user
- Rejects empty input
- Accepts `done` in any capitalization to finish input
- Displays all food items
- Shows the total number of items

## Code

```python
foods = []

while True:
    item = input("What do you want to buy? ")

    if item == '':
        print("Please enter something.")
        continue

    if item.lower() == 'done':
        print("Your order is:")
        for food in foods:
            print(food)
        print("Total items:", len(foods))
        break

    foods.append(item)
```

## What I Learned

### 1. Lists

An empty list can be created with `[]`.

```python
foods = []
foods.append("sushi")
```

`append()` adds an element to the end of the list.

### 2. Iterating over a list

```python
for food in foods:
    print(food)
```

A `for` loop processes each element in the list.

### 3. Counting elements

```python
len(foods)
```

`len()` returns the number of elements in a list.

### 4. Case-insensitive comparison

```python
item.lower() == 'done'
```

`lower()` converts a string to lowercase, so inputs such as `DONE`, `Done`, and `done` can all be recognized.

### 5. `break` vs. `continue`

- `break`: exits the loop completely.
- `continue`: skips the rest of the current iteration and starts the next one.

In this program, `continue` prevents empty strings from being added to the list, while `break` exits when the user enters `done`.

## Key Takeaway

**Lists allow multiple values to be stored and processed together.** Combining lists with loops and conditional statements makes it possible to build interactive programs.

## Next Steps

- Prevent duplicate food items.
- Remove an item from the shopping list.
- Display the list with item numbers.
- Handle whitespace-only input using `strip()`.