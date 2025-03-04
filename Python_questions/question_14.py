# Write a Python program that returns a string that is n (non-negative integer) 
# copies of a given string.

while (True):
    s = input("Enter the word : ")
    n = int(input("Enter number : "))
    result = (s * n)
    if(n < 0):
        print("Invalid input. Please enter a non-negative integer.")
    else:
        print(result)
        break