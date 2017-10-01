class Student:

    def __init__(self, id, name, hours, qpoints):
        self.id = id
        self.name = name
        self.hours = float(hours)
        self.qpoints = float(qpoints)

    def getId(self):
        return self.id;

    def getName(self):
        return self.name

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qpoints

    def gpa(self):
        return self.qpoints / self.hours

    def addGrade(self, gradePoint, credits):
        self.qpoints += credits * gradePoint
        self.hours += credits


    def addLetterGrade(self,letterGrade,credits):

        if letterGrade == "A":
            gradePoint = 4
        elif letterGrade == "B":
            gradePoint = 3
        elif letterGrade == "C":
            gradePoint = 2
        elif letterGrade == "D":
            gradePoint = 1
        else:
            gradePoint = 0
        self.qpoints += credits * gradePoint
        self.hours += credits
