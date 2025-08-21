num_minutes = int(input("Enter the number of minutes: "))

hours = num_minutes // 60
minutes = num_minutes % 60

hours_label = "hour" if hours == 1 else "hours"
minutes_label = "minute" if minutes == 1 else "minutes"
print(f"The time is: {hours} {hours_label} and {minutes} {minutes_label}.")