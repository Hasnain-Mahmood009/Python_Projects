# Write a Python program to calculate the sum of three given 
# numbers. If the values are equal, return three times their sum.
def sum_fun(x, y, z):
    sum = x + y + z
    if x == y == z:
        sum = sum * 3
    return sum
print(sum_fun(1, 2, 3))
print(sum_fun(3, 3, 3))