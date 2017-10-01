class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "Abscissa: {}, Ordinate: {}".format(self.x, self.y)
    def translate(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

p1 = Point(1,1)
print(p1)

#let's translate it!!

p1.translate(3, -3)
print("The translated point is: ", p1)

