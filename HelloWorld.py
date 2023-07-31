import datetime


# Print out hello world -- First Task
print("Hello World!")

# Find the UTC time of the OS
current_time = datetime.datetime.now()

# Set the timezone to EST
est_offset = datetime.timedelta(hours=4)

est_time = current_time - est_offset # UTC - EST_offset by 4 hours

print("Current time in EST: {}".format(est_time))
print()
print("Formatting of time: YYYY-MM-DD HH:MM:SS:MS")


# # Print out the operating system -- Second Task
# if os.name == 'posix':
#     print("Operating System Name: Linux or MacOS")
# elif os.name == 'nt':
#     print("Operating System Name: Windows")
# else:
#     print("Operating System Name: Unknown")
