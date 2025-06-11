def linear_search(n):
    list1 = [2,3,9,8,1,4,5,3]

    for i in range(len(list1)):
        li = list1[i]
        if n == li:
            return i
        
print(linear_search(4))