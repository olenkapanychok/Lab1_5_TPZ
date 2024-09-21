# main.py

def add_elements(lst):
    return sum(lst)

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def integer_division(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a // b

def modulus(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a % b

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def abs_value(n):
    return abs(n)

def max_in_list(lst):
    if not lst:
        raise ValueError("List is empty")
    return max(lst)

def concatenate_strings(s1, s2):
    return s1 + s2

def find_substring(s, sub):
    return s.find(sub)
