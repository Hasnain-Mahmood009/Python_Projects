# Write a Python program that accepts an integer (n) and 
# computes the value of n+nn+nnn.
print("Question 1........")
n = int(input("Enter a number : "))
result = n + int(str(n) * 2) + int(str(n) * 3)
print(result)





# Write a Python program to print the documents (syntax, description etc.) 
# of Python built-in function(s).
print("Question 2........")
import os
help(os)
