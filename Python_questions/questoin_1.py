# Write a Python program that accepts the user's first and last name 
# and prints them in reverse order with a space between them.

print("Question (1)......")
first_name = input("enter your first name : ")
last_name = input("enter your last name  : ")

print(first_name[::-1],end=" ")
print(last_name[::-1])