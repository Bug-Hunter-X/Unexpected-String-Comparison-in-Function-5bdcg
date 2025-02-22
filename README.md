# Python Function Bug: Unexpected String Comparison

This repository demonstrates a common subtle bug in Python functions that involves unexpected behavior when comparing strings.

The function `my_function` intends to return the larger of two input values.  It works correctly for numbers, but when given strings, the comparison uses lexicographical ordering rather than a numerical one, leading to incorrect results.

The `bug.py` file contains the buggy code. The `bugSolution.py` file demonstrates a corrected version.

## How to reproduce the bug:

1. Clone this repository.
2. Run `bug.py`.
3. Observe the output for numerical and string inputs.  The string comparison will produce unexpected results.

## Solution

The solution involves adding a check to determine the data type of the inputs before performing comparison using the appropriate method (numerical comparison for numbers and lexicographical for strings). See `bugSolution.py` for implementation.