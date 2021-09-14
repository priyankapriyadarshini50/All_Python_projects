import os
for folder, sub_folders, files in os.walk("/Test_Top_Level"):
    print("we are looking at the folder: ", folder)
    print("\n")
    print("THE SUB FOLDERS ARE: ")
    for sub_folder in sub_folders:
        print("\t Sub folders: ", sub_folder)
    print('\n')
    print("THE FILES ARE: ")
    for file in files:
        print("\t Files: ", file)
