class Student:
    def __init__(self, name, ID, marks):
        self.name = name
        self.ID = ID
        self.marks = marks
    def __str__(self):
        return "Name: {}, Student ID: {}, Student Marks: {}".format(self.name, self.ID, self.marks)

    def average(self):
        sum = 0
        for element in self.marks:
            sum = sum + element
        return "The average is: {}".format(sum/len(self.marks))




S1 = Student("Save", 12345, [7,8,6,7,8,9,5,7,8,9] )

print(S1)

print(S1.average())



