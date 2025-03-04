#Write a phyton program to print all even numbers from a given list of
#in the same order and stop printing any after 237 in the sequence.

numbers = [234,123,4322,543,234,654,3,4,7,334,237,34,237]

for i in range(0, len(numbers)):
    li = numbers[i]
    if(li != 237):
        if(li%2 == 0):
            print(li)
    else:
        break