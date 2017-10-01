# class Person:
#     name = 'John'
#     age = 20
#
# p1 = Person() # this is called constructor and has the same name of the class and you can also add a paramiter to it.
#
# p2 = Person()
#
# p2.name = 'Mary'
# p2.age = 18
#
# print(p1.name)
# print(p1.age)
# print(p2.name)
# print(p2.age)



# how to create people without all the time define a new constructor for a new person and using parameters
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def __str__(self): #this method is used to print the full object attributes in a readable way
        return "Name: {}, Age: {}, Address: {}".format(self.name, self.age, self.address) #the .format method fills the curly brackets.
    #you can add all the methods you want inside the class
    #the following method will change the address
    def change_address(self, new_address):
        self.address = new_address
    def age_diff(self, subtracting):
        return "The result of the substraction is: {}" .format(self.age - subtracting)

p = Person('Name', 'Age', 'Address')

p1 = Person('Martin', 20, "Best Street")
p1.change_address('New') #here we are changing the address of the person
p2 = Person('Mara', 25, "Worst Street")
p2.change_address('New')
p3 = Person('Save', 25, "Sheriff Street")
p3.change_address('New')


print(p1)
print(p2)
print(p3)

#here we are printing the difference between ages
print(p1.age_diff(p2.age))

#the attributes of each person can be modified (e.g. p1.name = "New Name")

#print(p.name, p.age, p.address)
#print(p1.name, p1.age, p1.address)
#print(p2.name, p2.age, p2.address)
#print(p3.name, p3.age, p3.address)   #you can also print all the attributes at one time insteade of call each time,
# the method __str__ will give you the stirng representation of the object.

