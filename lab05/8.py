import os
import re

def newline(text):
    pattern = r'([А-Я])'
    print(re.sub(pattern, r'\n\1', text))

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "my.txt")

with open(file_path, "r", encoding="utf-8") as file:
    for line in file:
        newline(line)