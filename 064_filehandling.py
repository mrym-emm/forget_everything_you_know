# python file handling
# relative = folder/test.txt
# absolute = C:/users/mm/desktop/test.txt or double slash

import os

file_path = "C:\\Users\\Maryam M\\Desktop\\gems\\klassikal"
file_path = "text.txt"

if os.path.exists(file_path):
    print(f"The location is '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file")

    # check if something is a folder/directory
    elif os.path.isdir(file_path):
        print("This is a directory/folder")

else:
    print("That location doesnt exist")