# Write a Python program to calculate the body mass index
height = float(input("Enter height : "))
weight = int(input("Enter weight : "))

bmi = weight / height ** 2
print(f"Your BMI is : {bmi:.2f}")
