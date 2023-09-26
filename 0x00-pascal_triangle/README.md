# Pascal's Triangle

This project involves creating a Python function that generates Pascal's Triangle. Pascal's Triangle is a mathematical concept that provides a triangular array of binomial coefficients. Each number in the triangle is the sum of the two directly above it.

## Project Task

### Task 0: Pascal's Triangle

**File**: `0-pascal_triangle.py`

**Function**: `def pascal_triangle(n):`

**Description**:
- Create a function `pascal_triangle` that returns a list of lists of integers representing Pascal's Triangle of `n`.

**Specifications**:
- The function should return an empty list if `n` is less than or equal to 0.
- You can assume that `n` will always be an integer.

## Usage

You can use the `pascal_triangle` function in your Python code to generate Pascal's Triangle. Here's an example of how to use it:

```python
from pascal_triangle import pascal_triangle

def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row]))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```

This code will print Pascal's Triangle up to the 5th row.

## Example Output

When running the example code, you should get the following output:

```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

## Repository

You can find the source code for this project in the [GitHub repository](https://github.com/seb-art/alx-interview) under the `0x00-pascal_triangle` directory.
