# OPERATOR PRECEDENCE

# example
print(3 + 4)
# output 7

# Python operator precedence

# Give examples of operator precedence in Python
# Multiplication get evaluated before
# the addition operation
# Result: 17
print(5 + 4 * 3)

# Parentheses () overriding the precedence of the arithmetic operators
# Output: 27
print((5 + 4) * 3)


# Python operator associativity

# Give examples of associativity in Python
# Testing Left-right associativity
# Result: 1
print(4 * 7 % 3)

# Testing left-right associativity
# Result: 0
print(2 * (10 % 5))
# examples
# Checking right-left associativity of ** exponent operator
# Output: 256
print(4 ** 2 ** 2)

# Checking the right-left associativity
# of **
# Output: 256
print((4 ** 2) ** 2)

# Nonassociative operators

# Examples of nonassociative operators
# Set the values of a, b, c
x = 11
y = 12
z = 13

# Expression is incorrect
# Non-associative operators
# Error -> SyntaxError: invalid syntax
x = y = z
# print(x = y += 12)
print(x)
print(y)
print(z)