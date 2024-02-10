class Shape:

    def area(self):
        return 0
class Square:
    def __init__(self, length):
        self.arg = length
        
    def area(self):
        return self.arg ** 2
    
length = float(input("Enter the length of square: "))
res = Square(length)

print("The area of the square is :", res.area())