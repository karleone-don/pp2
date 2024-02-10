class Shape:
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
length = float(input("Enter the length of Rectangle: "))
width = float(input("Enter the width of Rectangle: "))
res = Rectangle(length, width)

print("The area of the Rectangle is :", res.area())

