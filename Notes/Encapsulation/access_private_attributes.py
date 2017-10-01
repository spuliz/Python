#Example 3
# Modify the class Person so it uses one variable to represent the full name, e.g.
# ‘John Smith’. How would you access the first name and the surname?

class Person:
    def __init__(self, fullname, age, name, surname):
        # we add __ after self to define a modifier to be private
        self.fullname = fullname
        self.age = age
        self.__name = name
        self.__surname = surname
    def __str__(self):
        return "Full name: {}, Age: {}".format(self.fullname, self.age)

p1 = Person("Saverio Pulizzi", "25", "Saverio", "Pulizzi")

print(p1)
print(p1._Person__name)
print(p1._Person__surname)

