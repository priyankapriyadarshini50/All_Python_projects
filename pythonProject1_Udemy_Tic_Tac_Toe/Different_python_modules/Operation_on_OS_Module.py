#import platform
#print(platform.uname())
import os
import errno
# create directory
try:
    os.mkdir("Using_OS_Module")  # current working directory
except IOError as ie:
    print("I/O error message: ", os.strerror(ie.errno))
    print("File already exists.")
#os.mkdir("../my_second_working_dire")
#print(os.getcwd())


# find ALL THE FILES SND FOLDERS IN THE PATH DIRECTORY
#print(os.listdir("C:\\Users\\umesh\\PycharmProjects\\pythonProject1_Udemy_Tic_Tac_Toe\\Different_python_modules\\File_Processing_Module"))

# CREATE MY_FIRST_DIRECTORY AND INSIDE IT A SUB DIRECTORY IN THE CURRENT WORKING DIRECTORY
#os.makedirs("my_first_directory\\my_second_dire")
#print(os.getcwd())

# CREATE ANOTHER SUB-FOLDER INSIDE MY_FIRST_DIRECTORY
#os.mkdir("C:\\Users\\umesh\PycharmProjects\pythonProject1_Udemy_Tic_Tac_Toe\Different_python_modules\my_first_directory\my_second_dire")

# DELETE BOTH THE FOLDER AND SUB FOLDER
#os.removedirs("C:\\Users\\umesh\PycharmProjects\pythonProject1_Udemy_Tic_Tac_Toe\Different_python_modules\my_first_directory\my_second_dire")
print(os.listdir())
# MOVE TO MY_FIRST_DIRECTORY
#os.chdir("C:\\Users\\umesh\PycharmProjects\pythonProject1_Udemy_Tic_Tac_Toe\Different_python_modules\my_first_directory")
#print(os.listdir())
#print(os.getcwd())

# MOVE TO MY_TEST_DIRECTORY
#os.chdir("C:\\Users\\umesh\PycharmProjects\pythonProject1_Udemy_Tic_Tac_Toe\Different_python_modules\my_test_directory")
#print(os.listdir())
#print(os.getcwd())
#os.rmdir("C:\\Users\\umesh\PycharmProjects\pythonProject1_Udemy_Tic_Tac_Toe\Different_python_modules\my_test_directory")
print(os.name)
