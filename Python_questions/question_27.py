# Write a Python program to get the current username.

import os
def username():
    return os.getlogin()

print(username())