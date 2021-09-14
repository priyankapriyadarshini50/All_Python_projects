import errno
from os import strerror

# Create and Open a file
# f = open("Exception_handling.txt", "wt")
# f.write("This file has created to check IOException.")
# f.close()

# Lets try to create an exception by writing on the file with read mode
try:
    f = open("Exception_handling.txt", "rt")
    f.write("This is the second line \\n")
    f.close()
except IOError as e:
    print(e.errno)
    # print(errno.errorcode)
    print(errno.EPERM)
    print("The error message: ", strerror(errno.EPERM))

# TO GET ALL THE ERROR MESSAGE FOR 1 TO 20 ERROR CODE
for error_code in range(1, 21):
    print(f"The error message corresponding to error code {error_code}: ", strerror(error_code))

