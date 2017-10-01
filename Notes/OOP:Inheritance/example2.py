#Generate a superclass polygon and then add the subclasses triangle and rectagle

class Polygon:
    def __init__(self, sides):
        self.sides = sides
        self.size = [int(input("Please enter the size of the sides: ")) for i in range(sides)]

    def __str__(self):
        return "The sides of your Polygon are: {}; The size of your sides are: {}".format(self.sides, self.size)

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

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
        Polygon.__init__(self, 2)

    def area(self):
        a, b = self.size
        area = a * b
        print('The area of the rectangle is:', round(area, 2))



t = Triangle()
t.area()
print(t)

r = Rectangle()
r.area()

p = Polygon(4)
print(p)
