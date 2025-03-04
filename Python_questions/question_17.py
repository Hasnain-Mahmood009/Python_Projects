#Write a phyton program to test whether a passed letter is a vowel or not.

n = input("Enter the letter : ")
result = ""
vowel = ["a","e","i","o","u"]
for x in range(0, len(vowel)):
        if(len(n) > 1):
            result = "invalid input try again..."
        else:
            if(n == vowel[x]):
                result = "This letter is vowel..."
                break
            else:
                result = "This is not vowel..."
print(result)