# Day 8: Python Error Handling and Conditional Logic

## What I Learned

- Use `if`, `elif`, and `else` to handle different conditions.
- Define functions using `def`.
- Use `return` to return a result from a function.
- Handle invalid numeric input using `try` and `except ValueError`.
- Validate input values separately from type conversion.
- Understand that `continue` is used inside loops, while `return` can exit a function.

## What I Built

I created an age-checking program that categorizes a person as an adult or a child and handles invalid input.

```python
def check_age(age):
    if age > 17:
        category = "adult"
    elif age < 0:
        return "age should be 0 or more"
    else:
        category = "child"

    return category


try:
    age = int(input("Enter your age: "))
    result = check_age(age)

    if age < 0:
        print("really?")
    else:
        print(f"You are {age} old now.")
        print(result)

except ValueError:
    print("please input valid numbers.")
```

## Example Outputs

### Adult

```text
Enter your age: 20
You are 20 old now.
adult
```

### Negative Age

```text
Enter your age: -5
really?
```

### Invalid Input

```text
Enter your age: hello
please input valid numbers.
```

## Key Takeaways

### 1. Conditional Logic

- `if` checks the first condition.
- `elif` checks another condition if previous conditions are false.
- `else` handles the remaining cases.

### 2. Functions and `return`

- Functions organize code into reusable blocks.
- `return` sends a value back to the caller and ends the function.
- A function without an explicit return value returns `None`.

### 3. Error Handling

- `int()` converts a string into an integer when possible.
- `ValueError` occurs when a string cannot be converted into an integer.
- Negative numbers are valid integers, so they require a separate validation check.

### 4. `continue` vs. `return`

- `continue` skips to the next iteration of a loop.
- `return` exits a function and optionally returns a value.

## Next Steps

- Improve the error messages for invalid ages.
- Prevent negative ages from being displayed as valid ages.
- Practice input validation with loops.
