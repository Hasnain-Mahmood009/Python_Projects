s = "abdsddsb"
li = []
li.append(s[0])
for i in range(1,len(s)):
    if s[i] == li[i]:
        continue
    else:
        li.append(s[i])
print(li)