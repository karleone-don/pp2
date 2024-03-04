import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'write.txt')

array = [1, 2, 3, 4 , 5]

with open(file_path, 'w', encoding='utf-8') as file:
    for item in array:
        file.write("%s\n" % item)