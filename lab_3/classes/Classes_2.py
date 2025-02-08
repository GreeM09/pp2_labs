class Shape():
    def __init__(self, sides):
        self.sides = sides
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, side_length):
        super().__init__(4)
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

class Triangle(Shape):
    def __init__(self, length, width):
        super().__init__(3)
        self.length = length
        self.width = width

    def area(self):
        return (self.length * self.width)/2

square = Square(int(input("Enter side length of square: ")))
print(square.area())
triangle = Triangle(int(input("Enter length of triangle: ")), int(input("Enter width of triangle: ")))
print(triangle.area())
