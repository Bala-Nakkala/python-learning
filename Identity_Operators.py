# Identity Operators in Python
# Identity operators are used to compare the memory locations of two objects.

a= [1, 2, 3]
b = a  # b is assigned the same reference as a
result = a is b
print(result)  # Output: True

a= "hello"
b= "world"
result = a is b
print(result)  # Output: False

a= 10
b= 10
result = a is b
print(result)  # Output: True (small integers are cached by Python)
