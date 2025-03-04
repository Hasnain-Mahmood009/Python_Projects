# Write a Python program that creates all possible strings using the letters 
# 'a', 'e', 'i', 'o', and 'I'. Ensure that each character is used only once.

import random
letters = ['a', 'e', 'i', 'o', 'I']
for i in range(0,100):
    random.shuffle(letters)
    result = ''.join(letters)
    print("Random string:", result)

    