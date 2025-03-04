# Write a Python program that accepts a sequence of comma-separated 
# numbers from the user and generates a list and a tuple of those numbers.

prompt = input("enter the value : ")
saperated = prompt.split(",")
tup = tuple(saperated)
print("List : ", saperated)
print("Tuple : ",tup)