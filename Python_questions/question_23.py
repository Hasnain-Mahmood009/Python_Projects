#Write a phyton program to find the least common multiple (LCM) 
#of two positive integers.

number = 20
result = 0
for i in range(1,number+1):
    for j in range(1,number+1):
        m = i*j
        if(m == number):
            result = i*j
            break
print(result)