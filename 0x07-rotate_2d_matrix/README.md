#!/bin/bash

cat <<EOF > README.md
# Rotate 2D Matrix

This project contains a solution to rotate an n x n 2D matrix 90 degrees clockwise.

## Task Description

Given an n x n 2D matrix, rotate it 90 degrees clockwise.

### Function Prototype

\`\`\`python
def rotate_2d_matrix(matrix):
    """Rotate a 2D matrix 90 degrees clockwise."""
\`\`\`

- **Input:** An n x n 2D matrix.
- **Output:** None. The matrix must be edited in-place.
- **Assumptions:** The matrix will have 2 dimensions and will not be empty.

## Usage

To test the implementation, use the provided main file:

\`\`\`python
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    rotate_2d_matrix(matrix)
    print(matrix)
\`\`\`

### Expected Output

The output of running the main file will be:

\`\`\`
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]
\`\`\`

## Execution

To execute the project, ensure you have the required environment and run the main file (e.g., \`./main_0.py\`) to test the rotation function

