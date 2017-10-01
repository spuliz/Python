from student import Student
import unittest

class TestStudent(unittest.TestCase):

    def testStudent(self):
        st = Student(1,'cici',13, 342)
        assert st.getName() == 'cici'
        assert st.getId() == 1
        assert st.getHours() == 13
        assert st.getQPoints() ==342

    def testGetName(self):
        st = Student(2,'james',15, 123)
        assert st.getName() == 'james'

    def testGetID(self):
        st = Student(3,'tst', 0,0 )
        assert st.getId() ==3

    def testAddGrade(self):
        st = Student(4, 'John', 12, 200)
        st.addGrade(10,10)
        assert st.getqpoints() == 300

    def testAddLetterGrade(self):
        st = Student(4, 'John', 12, 200)
        st.addGrade(10,10)
        assert st.addLetterGrade() == "A"


def suite():
    print ("Test for Student Results")
    suite = unittest.TestSuite()
    suite.addTest(TestStudent("testStudent"))
    suite.addTest(TestStudent("testGetName"))
    suite.addTest(TestStudent("testGetID"))
    suite.addTest(TestStudent("testAddGrade"))
    suite.addTest(TestStudent("testAddLetterGrade"))

    print ('\n')
    return suite

runnerS = unittest.TextTestRunner()
runnerS.run(suite())
