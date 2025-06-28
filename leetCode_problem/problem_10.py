l1 = [1,2,3,3,2,4,2,1,4]

l2 = []
l2.append(l1[0])
for i in range(1,len(l1)):
    f = l1[i]
    for j in range(len(l2)):
        if f not in l2:
            l2.append(f)
print(l2)