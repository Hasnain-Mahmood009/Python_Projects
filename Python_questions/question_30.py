# Write a Python program to convert height (in feet and inches) to centimeters.
def converter(centimeters):
    inches = centimeters / 2.54
    return inches

centimeters = int(input("Centimeters: "))
print(converter(centimeters))
