import math


class Polygon:
    def __init__(self, sides, color, x, y):
        self.sides = sides
        self.size = [int(input("Please enter the size of the sides: ")) for i in range(sides)]
        self.color = color
        self.x = x
        self.y = y

    def __str__(self):
        return "The sides of your Polygon are: {}; The size of your sides are: {}".format(self.sides, self.size)

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy



class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3, 'orange', 0, 0)

    def area(self):
        a, b, c = self.size
        # semiperimeter
        s = (a + b + c)/2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is:', round(area, 2))

    def __str__(self):
        return "The sides of your Triangle are: {}; The size of your sides are: {}".format(self.sides, self.size)



class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2, 'yellow', 0, 0)

    def area(self):
        a, b = self.size
        area = a * b
        print('The area of the rectangle is:', round(area, 2))





class Circle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 1, 'green', 0, 0)

    def area(self):
        r = self.size[0]
        area = math.pi * r ** 2
        print('The area of the circle is:', round(area, 2))



class Square(Polygon):
    def __init__(self):
        Polygon.__init__(self,1, 'red', 0, 0)

    def area(self):
        l = self.size[0]
        area = l ** 2
        print('The area of the square is:', round(area, 2))



c = Circle()
c.area()

s = Square()
s.area()


