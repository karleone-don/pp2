string = input()

low = 0
hight = 0
for i in string:
    if 96 < ord(i) and ord(i) < 123:
        low += 1
    if 64 < ord(i) and ord(i) < 90:
        hight += 1

print("num of lower case letters:", low)
print("num of upper case letters:", hight)

#a = 97, z = 122
#A = 65, Z = 90