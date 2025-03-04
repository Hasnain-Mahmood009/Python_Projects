# Write a  Python program to calculate the number of days 
# between two dates.

day_1 = int(input("First day : "))
day_2 = int(input("Second day : "))
month_1 = int(input("First Month : "))
month_2 = int(input("second Month : "))
month = 30
result = day_1 - day_2-1
month_1_result = month * month_1
month_2_result = month * month_2
print("Total Days : ",abs(month_1_result - month_2_result + result))
