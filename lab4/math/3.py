import math
num = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))

#S = (n * a^2) / 4tg(pi/n)
S = (num * l ** 2) / (4 * math.tan(math.pi/num))
print("The area of the polygon is:", round(S, 5))