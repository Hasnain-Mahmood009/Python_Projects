#Write a phyton program to create a histogram from a given list of integers.

li = [3,6,3]

for x in range(0, len(li)):
    value = li[x]
    for i in range(0,value):
        print("*",end=" ")
    print(end="\n")