# Write a Python function that takes a sequence of numbers and 
# determines whether all the numbers are different from each other.

li = [2,3,4,5,3,5,4,3,8]

for i in range(0, len(li)):
    for j in range(i+1, len(li)):
        if li[i] == li[j]:
            print("Index : ",j, end= "   ")
            print("value : ",li[j])