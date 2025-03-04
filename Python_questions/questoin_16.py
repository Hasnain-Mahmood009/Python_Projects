# Write a Python program to get n (non-negative integer) copies of the first 2 
# characters of a given string. Return n copies of the whole string if the length 
# is less than 2.

def repeat_string(string, repeat):
    if len(string) < 2:
        return string * repeat
    else:
        return string[:2] * repeat

print(repeat_string("Hasnain", 2)) 