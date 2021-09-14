import os
# create an array with byte elements
data = bytearray(10)
print(ord("a"))
# Enter elements to the byte array
for i in range(len(data)):
    data[i] = ord("a") + i
print(data)

try:
    # Create a binary file with write mode wb
    f = open("/Different_python_modules/File_Processing_Module\\test_byte.bin", "wb")
    f.write(data)
    f.close()
except IOError as e:
    print("The error message with the code is: ", os.strerror(e))

try:
    # read the binary information from the binary file file
    f = open("/Different_python_modules/File_Processing_Module\\test_byte.bin", "rb")
    # assign the content of the binary file to an binary object
    f_binary_content = bytearray(f.read()) # f.read() reads all the contents of the binary file

    for b in f_binary_content:
        print(hex(b))
    f.close()
except IOError as e:
    print("The error message: ", os.strerror(e))
