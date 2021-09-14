import os
print(os.getcwd())
#f = open('C:\\Users\\umesh\\PycharmProjects\\pythonProject1_Udemy_Tic_Tac_Toe\\Different_python_modules\\practice.txt', 'w')
#f.write('This is a test string')
#f.close()
# returns a list of files in the current directory
print(os.listdir())
# lets see the files and folders under Udemy tic_tac_Toe directory
print(os.listdir('C:\\Users\\umesh\\PycharmProjects\\pythonProject1_Udemy_Tic_Tac_Toe'))

# move the file from one folder to another
#import shutil
#shutil.move('practice.txt', 'C:\\Users\\umesh\\PycharmProjects\\pythonProject1_Udemy_Tic_Tac_Toe')
# After executing this we can see the practice file is under tic tac toe folder
# delete the practice file from tic tac toe
import send2trash
send2trash.send2trash('C:\\Users\\umesh\\PycharmProjects\\pythonProject1_Udemy_Tic_Tac_Toe\\practice.txt')


