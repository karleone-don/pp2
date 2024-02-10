class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Coordinates of the point: ({self.x}, {self.y})")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, left):
        return round(((self.x - left.x) ** 2 + (self.y - left.y) ** 2) ** 0.5)

x1, y1 = map(int, input("Enter the coordinates of the first point: ").split())
x2, y2 = map(int, input("Enter the first coordinates of the 2nd points: ").split())

p1 = Points(x1, y1)
p2 = Points(x2, y2)

p1.show()
p2.move(2, -1)
p2.show()
distance = p1.dist(p2)

print("Distance between p1 and p2:", distance)
