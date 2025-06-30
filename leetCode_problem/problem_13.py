s = "abhjklf"
ss = "jkl"
step = len(ss)
for i in range(0,len(s),step):
    chunk = s[i:i+step]
    if chunk == ss:
        print(i)
        break
    # print(chunk)