import os
import re

def lowcase(match):
    return match.group(1).lower() + '_' + match.group(2).lower()

def snake(text):
    pattern = r'([a-zA-Z])([A-Z])'
    result = re.sub(pattern, lowcase, text)
    print(result, end='')

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'new.txt')


with open(file_path, 'r', encoding='utf-8') as file:
    for line in file:
        snake(line)