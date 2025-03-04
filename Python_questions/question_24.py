#Write a phyton program to sum two given integers. However, if the sum 
#is between 15 and 20 it will return 20.

n1 = 112
n2 = 65

sum = n1+n2
for i in range(0,sum+20,5):
    if(i > sum):
        print(i)
        break
    else:
        i += 1
