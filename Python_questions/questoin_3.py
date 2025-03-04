# Write a Python program that accepts a filename from 
# the user and prints the extension of the file.
filename = input("Enter file name : ")
exe = filename.split(".")
exetension = exe[-1]
if(len(exe) > 1):
    print("Extention Name : ", exetension)
else:
    print("Plese check your name..")
print("File Name : ", filename)