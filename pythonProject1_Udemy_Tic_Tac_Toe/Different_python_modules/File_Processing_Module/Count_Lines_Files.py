import os

#print(f.read())
#print(f.readline())
try:
    f = open("C:\\Users\\umesh\\PycharmProjects\\pythonProject1_Udemy_Tic_Tac_Toe\\Different_python_modules\\test.txt", "rt")
    line_cnt = 0
    ch_cnt = 0
    line = f.readline()
    while line != "":
        line_cnt += 1
        for ch in line:
            print(ch, end=' ')
            ch_cnt += 1
        line = f.readline()
    print("\n")
    print("The total no of characters: ", ch_cnt)
    print("The total number of line: ", line_cnt)
    f.close()
except IOError as e:
    print("The error message corresponding to error code: ", os.strerror(e))

# Another solution to read lines
