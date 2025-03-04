# Write a Python program to convert all units of time into seconds.

def time_to_seconds(days, hours, minutes, seconds):
    total_seconds = (days * 86400) + (hours * 3600) + (minutes * 60) + seconds
    return total_seconds

# User input
days = int(input("Enter days: "))
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

# Convert to seconds
result = time_to_seconds(days, hours, minutes, seconds)
print("Total time in seconds: ", result)

