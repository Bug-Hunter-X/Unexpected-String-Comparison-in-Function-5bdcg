def my_function(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a > b:
            return a
        else:
            return b
    elif isinstance(a, str) and isinstance(b, str):
        if a > b:
            return a
        else:
            return b
    else:
        return "Error: Inputs must be numbers or strings"

result = my_function(5, 2)
print(result)  # Output: 5

result = my_function(2, 5)
print(result)  # Output: 5

result = my_function(-1, 1)
print(result) # Output: 1

result = my_function('apple', 'banana')
print(result) # Output: banana

result = my_function('banana', 'apple')
print(result) # Output: banana

result = my_function(1, 'apple')
print(result) # Output: Error: Inputs must be numbers or strings