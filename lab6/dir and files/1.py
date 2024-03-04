import os

path = r'C:\Users\abzal\Desktop\kbtu'

for dirs, folders, files in os.walk(path):
    print(dirs)
    print(folders)
    print(files)

#directory = os.walk(path)
#print(next(directory))