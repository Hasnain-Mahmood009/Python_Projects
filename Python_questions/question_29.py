# Write a Python program to sum the first n positive integers.

n = int(input("Enter a number: "))
sum = 0

for i in range(1, n+1):
    sum += i

print("The sum is:", sum)
