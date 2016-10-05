total_time = int(input("Enter a number of seconds between 0 and 86400: "))

hours = int(total_time / 3600.0)

minutes = int((total_time - (hours * 3600.0)) / 60.0)

seconds = int(((total_time) - (hours * 3600) - (minutes * 60)))

print("The time is %d hours, %d minutes, and %d seconds." % (hours, minutes, seconds))