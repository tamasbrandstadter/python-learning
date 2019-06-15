fibonacci_dict = {0: 0, 1: 1}


# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.
def add(n):
    if n == 1:
        return n
    return n + add(n - 1)


# Given a non-negative integer n, return the sum of its digits recursively
def sum_of_digits(n, accumulator):
    if n < 10:
        return accumulator + n
    accumulator += n % 10
    return sum_of_digits(n // 10, accumulator)


# Given base and n that are both 1 or more, compute recursively the value of base to the n power.
def power_n(base, power):
    if power == 1:
        return base
    return base * power_n(base, power - 1)


# Find the greatest common divisor of two numbers using recursion.
def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)


# We have a number of bunnies and each bunny has two big floppy ears. We want to compute the total number of ears
# across all the bunnies recursively
def count_bunny_ears(n):
    if n == 1:
        return 2
    if n % 2 == 0:
        ears = 3
    else:
        ears = 2
    return ears + count_bunny_ears(n - 1)


# The fibonacci sequence is a famous bit of mathematics, and it happens to have a recursive definition.
# The first two values in the sequence are 0 and 1 (essentially 2 base cases).
# Each subsequent value is the sum of the previous two values, so the whole sequence is:
# 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on.
# Define a recursive fibonacci(n) method that returns the nth fibonacci number,
# with n=0 representing the start of the sequence.
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


# O(n) solution:
def fibonacci_memo(n):
    if n not in fibonacci_dict:
        fibonacci_dict[n] = fibonacci_memo(n - 2) + fibonacci_memo(n - 1)
    return fibonacci_dict[n]


# Write a function that finds the largest element of an array using recursion.
def find_max(numbers, max_value, index):
    if index == len(numbers):
        return max_value
    if numbers[index] > max_value:
        max_value = numbers[index]
    return find_max(numbers, max_value, index + 1)


print(add(5))
print(sum_of_digits(15636, 0))
print(power_n(3, 17))
print(count_bunny_ears(5))
print(fibonacci(9))
print(fibonacci_memo(9))
print(find_max([5, 6542, 3452, 2782, 7, 854], float('-inf'), 0))
