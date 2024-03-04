import os

file1 = r'C:\Users\abzal\Desktop\gitkbtupy\lab6\dir and files\alphabet\A.txt'
file2 = r'C:\Users\abzal\Desktop\gitkbtupy\lab6\dir and files\alphabet\Y.txt'

with open(file1, 'r') as f:
    file = f.read()

with open(file2, 'w') as f:
    f.write(file)