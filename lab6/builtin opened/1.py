ds = input()
number_list = ds.split()
numbers = [int(num) for num in number_list]
#print(eval('*'.join(str(item) for item in numbers)))
b = 1
for i in numbers:
    b *= i
print(b)