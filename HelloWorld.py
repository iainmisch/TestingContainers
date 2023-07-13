import os

# Print out hello world -- First Task
print("Hello World!")

# Print out the operating system -- Second Task
if os.name == 'posix':
    print("Operating System Name: Linux or MacOS")
elif os.name == 'nt':
    print("Operating System Name: Windows")
else:
    print("Operating System Name: Unknown")
