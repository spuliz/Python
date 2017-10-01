class Animal:
    def __init__(self, name):
        self.name = name



class Cat(Animal):
    def make_sound(self):
        print(self.name,'Says: miao')


class Dog(Animal):
    def make_sound(self):
        print('wof')


c = Cat('Fluffy')
c.make_sound()
