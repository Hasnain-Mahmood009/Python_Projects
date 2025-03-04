#Write a phyton program that checks whether a specified value is 
#contained within a goup of values.

li = [1,2,3,4,5,3,4,5,47,8]
n = 4
result = ""
for x in range(0,len(li)):
    if(li[x] == n):
        result = "present in list....."
        break
    else:
        result = "not present in the list......"
print(result)