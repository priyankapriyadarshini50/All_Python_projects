import os
try:
    s = open("C:\\Users\\umesh\\PycharmProjects\\pythonProject1_Udemy_Tic_Tac_Toe\\Different_python_modules\\test.txt", "r")
    print(type(s))
    lines = s.readlines()
    print(lines)
    print(type(lines))
    print(len(lines))
    for line in lines:
        print(line)
    s.close()
except IOError as e:
    print("The error message corresponding to the error code: ", os.strerror(e))
#print(s.readlines(20))
#print(s.readlines(20))
#print(s.readlines(20))

