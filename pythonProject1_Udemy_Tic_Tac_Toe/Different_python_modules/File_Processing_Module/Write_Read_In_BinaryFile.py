from os import strerror
import errno

data = bytearray(10)

for i in range(len(data)):
    data[i] = ord("a") + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Your code that reads bytes from the stream should go here.
data1 = bytearray(8)
try:
    bf = open("file.bin", "rb")
    bf.readinto(data1)
    bf.close()

    for b in data1:
        print(chr(b), end=" ")
except IOError as ie:
    print(ie.errno)
    print("I/O error message: ", strerror(ie.errno))

