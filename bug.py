def my_function(a, b):
    if a > b:
        return a
    else:
        return b

result = my_function(5, 2)
print(result)  # Output: 5

result = my_function(2, 5)
print(result)  # Output: 5

result = my_function(-1, 1)
print(result) # Output: 1

#However, this produces unexpected result when we call this function with strings
result = my_function('apple', 'banana')
print(result) # Output: banana

result = my_function('banana', 'apple')
print(result) #Output: banana