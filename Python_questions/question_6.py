# Write a Python program that accepts an integer (n) and 
# computes the value of n+nn+nnn.

n = int(input("Enter a number : "))
result = n + int(str(n) * 2) + int(str(n) * 3)
print(result)




