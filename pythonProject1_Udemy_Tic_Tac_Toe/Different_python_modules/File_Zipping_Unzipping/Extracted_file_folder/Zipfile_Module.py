# f1 = open('file_One.txt', 'w+')
# f1.write('This is File One text file.')
# f1.close()
# Create a file and write to it
# f2 = open('file_Two.txt', 'w+')
# f2.write('This is file Two text file.')
# f2.close()

import zipfile
import os
# create a folder (comp_file) and zip it
# send text file one by one into the zip folder
comp_file = zipfile.ZipFile('comp_file.zip', 'w')
# comp_file.write('file_One.txt',compress_type= zipfile.ZIP_DEFLATED)
# comp_file.write('file_two.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

import os
print(os.getcwd())

# Extract the zip files from the comp_file.zip folder
#zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
#zip_obj.extractall('C:\\Users\\umesh\\PycharmProjects\\pythonProject1_Udemy_Tic_Tac_Toe\\Different_python_modules\\File_Zipping_Unzipping\\Extracted_content')
# create a file 3 in Folder to be zipped
#f3 = open('C:\\Users\\umesh\\PycharmProjects\\pythonProject1_Udemy_Tic_Tac_Toe\\Different_python_modules\\File_Zipping_Unzipping\\Folder_to_be_zipped\\file_three.txt', 'w+')
#f3.write("This is file three.")
#f3.close()
#f4 = open('C:\\Users\\umesh\\PycharmProjects\\pythonProject1_Udemy_Tic_Tac_Toe\\Different_python_modules\\File_Zipping_Unzipping\\Folder_to_be_zipped\\file_four.txt', 'w+')
#f4.write("This is file four.")
#f4.close()

#ZIP THE FOLDER WHICH CONTANS FILE 3 AND 4 USING SHUTIL
import shutil
archived_file_name = 'file_contain_3 _4'
keep_file_path = 'C:\\Users\\umesh\\PycharmProjects\\pythonProject1_Udemy_Tic_Tac_Toe\\Different_python_modules\\File_Zipping_Unzipping'
shutil.make_archive(archived_file_name, 'zip', keep_file_path)

# EXTRACT FILE 3 AND 4 FROM FILE CONTAINING FOLDER
shutil.unpack_archive("file_contain_3 _4.zip",'Extracted_file_folder', 'zip')
