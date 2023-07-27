from django.test import TestCase
from Backend.courses.models import Course
from Backend.programs.DegreeExplorer.degreeAPI import Degree
# from programs.models import Program, Requirement

class DegreeExplorerTestCase(TestCase):

    def testBasic(self):
        degree = Degree()
        # degree.addCourse(Course)
        degree.removeCourse()
