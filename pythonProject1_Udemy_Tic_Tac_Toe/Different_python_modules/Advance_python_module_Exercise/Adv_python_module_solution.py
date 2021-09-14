import os
import re
# print(os.getcwd())
# import shutil
# out_put_filename = "C:\\Users\\umesh\\PycharmProjects\\pythonProject1_Udemy_Tic_Tac_Toe\\Different_python_modules\\Advance_python_module_Exercise\\unzip_me_for_instructions.zip"
# shutil.unpack_archive(out_put_filename, 'instruction_file', 'zip')


def find_phone_number(file_path):
    with open(file_path, 'r') as demo_file:
        contents = demo_file.read()
    pattern = r'\d{3}-\d{3}-\d{4}'
    match = re.search(pattern, contents)
    if match is None:
        return ''
    else:
        print(match.group())


for folders, sub_folders, files in os.walk("C:\\Users\\umesh\\PycharmProjects\\pythonProject1_Udemy_Tic_Tac_Toe\\Different_python_modules\\Advance_python_module_Exercise\\instruction_file\\extracted_content"):
    #print("We are looking at folder:", folders)
    #print('\n')
    #for sub_folder in sub_folders:
        #print("The Sub folder:", sub_folder)
    #print('\n')
    for file in files:
        #print("The file: ", file)
        path = folders + '\\' + file
        #print("Path: ", path)
        find_phone_number(path)
    print('\n')




#find_phone_number("C:\\Users\\umesh\\PycharmProjects\\pythonProject1_Udemy_Tic_Tac_Toe\\Different_python_modules\\Advance_python_module_Exercise\\instruction_file\\extracted_content\\Instructions.txt")





