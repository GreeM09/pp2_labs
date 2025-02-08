class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"Coordinates of point are ({self.x}, {self.y})")

    def move(self, x, y):
        self.x += x
        self.y += y

    def dist(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5

point = Point(int(input("Enter x coordinate: ")), int(input("Enter y coordinate: ")))
point.show()

point.move(int(input("Enter x to move: ")), int(input("Enter y to move: ")))
print(f"New coordinates after moving are: ({point.x}, {point.y})")

point2 = Point(int(input("Enter x coordinate: ")), int(input("Enter y coordinate: ")))

distance = point.dist(point2)
print(f"Distance between two points is {distance}")
