import os
import re

def space(text):
    pattern = r'([a-zA-Z])([A-Z])'

    result = re.sub(pattern, r'\1' + " " + r'\2', text)
    print(result, end ='')

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'new.txt')

with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        space(line)