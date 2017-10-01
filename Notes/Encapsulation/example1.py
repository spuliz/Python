# Example 1

# Encapsulation is used to make our code more user friendly


class Person:
    def __init__(self, name, age, address):
        # we add __ after self to define a modifier to be private
        self.__name = name
        self.age = age
        self.address = address
    # public method to get access the data stored in the variable
    def get_name(self):
        return self.__name

p1 = Person('Martin', 20, "Best Street")

# the get method will give you the opportunity to access to the data store in name even if that its private
print(p1.get_name())
# We can also access the private variable by calling the name of the class
print(p1._Person__name)
# print(p1.__name)
# print(p1.name)



