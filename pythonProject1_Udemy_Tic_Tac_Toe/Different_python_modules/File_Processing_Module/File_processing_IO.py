from os import strerror
#stream = open("C:\\Users\\umesh\\PycharmProjects\\pythonProject1_Udemy_Tic_Tac_Toe\\Different_python_modules\\test.txt", "w")
#poem = "Beautiful is better than ugly.\n" \
#      "Explicit is better than implicit.\n" \
#       "Simple is better than complex." \
#       "Complex is better than complicated."\
#        "Flat is better than nested." \
#       "Sparse is better than dense." \
#       "Readability counts."
#stream.write(poem)
#stream.close()
# count the number of characters in the file
try:
    stream = open("C:\\Users\\umesh\\PycharmProjects\\pythonProject1_Udemy_Tic_Tac_Toe\\Different_python_modules\\test.txt", "r")
    ch = stream.read(1)
    count = 0
    while ch != "":
        print(ch)
        count += 1
        ch = stream.read(1)
    print("The total no of characters :", count)
    stream.close()
except IOError as e:
    print("IOError occurred: ", strerror(e.errno))




