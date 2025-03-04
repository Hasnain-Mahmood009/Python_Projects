# Write a Python program that removes and prints every third number from a 
# list of numbers until the list is empty.

def remove_third_number(lst):
    index = 2
    
    while lst:
        print(lst.pop(index)) 
        if len(lst) < 3:
            break 
        index = (index + 2) % len(lst)
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
remove_third_number(numbers)
