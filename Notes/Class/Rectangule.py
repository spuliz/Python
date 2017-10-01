class Rectangule:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def __str__(self):
        return "The base is: {}, The height is: {}".format(self.base, self.height)

    def calculate_perimeter(self):
        return (self.base + self.height)*2

    def area(self):
        return self.base * self.height

r1 = Rectangule(4, 8)
print(r1)

print(r1.calculate_perimeter())
print(r1.area())
