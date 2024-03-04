import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'count.txt')
row = 0

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        row += 1
print(row)