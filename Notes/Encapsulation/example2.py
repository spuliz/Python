# Example 2
class Person:
    def __init__(self, name, age):
        # we add __ after self to define a modifier to be private
        self.name = name
        self.age = age
    # public method to get access the data stored in the variable
    # def get_name(self):
    #     return self.name
    # def get_age(self):
    #     return self.age

people = []

# populate the list
for i in range(2):
    n = input("Please enter the name: ")
    age = input("Please enter the age: ")
    p = Person(n, age);
    people.append(p)

# iterate over the list
for p in people:
    print(p.name)
    print(p.age)

