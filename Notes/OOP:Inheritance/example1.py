# Inheritance is a base class dependent of the mother class.
# For example creating student and staff as a subclass of staff
# In brackets you put the name of the superclass

#superclass
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name(self):
        return self.name


#subclassess
class Student(Person):
    def __init__(self, name, age, ID, course):
        # person. we use it to call the superclass within the subclass
        Person.__init__(self, name, age)
        self.ID = ID
        self.course = course

class Staff(Person):
    def __init__(self, name, age, staff_office):
        Person.__init__(self, name, age)
        self.staff_office = staff_office


student1 = Student('Paul', 15, 123456789, 'Python')
staff1 = Staff('John', 34, 'B2')


print(student1.get_name())
print(staff1.get_name())
