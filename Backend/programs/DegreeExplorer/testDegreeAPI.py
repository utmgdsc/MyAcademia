from django.test import TestCase
from courses.models import Course
from programs.DegreeExplorer.degreeAPI import Degree
# from programs.models import Program, Requirement


class DegreeExplorerTestCase(TestCase):

    def testCreditCalculation(self):
        degree = Degree()
        degree.addCourse(Course.objects.get(course_code="CSC108H5"))
        self.assertEqual(degree.credits, 0.5)

        degree.addCourse(Course.objects.get(course_code="PUN212Y5"))
        self.assertEqual(degree.credits, 1.5)

    def testCourseRemoval(self):
        degree = Degree()
        degree.addCourse(Course.objects.get(course_code="CSC108H5"))
        degree.addCourse(Course.objects.get(course_code="PUN212Y5"))
        degree.removeCourse(Course.objects.get(course_code="CSC108H5"))
        self.assertEqual(degree.credits, 1.0)

    def testHumApproval(self):
        degree = Degree()
        degree.addCourse(Course.objects.get(course_code="LIN204H5"))
        degree.addCourse(Course.objects.get(course_code="PUN212Y5"))
        degree.evaluate_requirements()
        self.assertTrue(degree.humRequirement)

    def testSciApproval(self):
        degree = Degree()
        degree.addCourse(Course.objects.get(course_code="CSC108H5"))
        degree.addCourse(Course.objects.get(course_code="CSC148H5"))
        degree.evaluate_requirements()
        self.assertTrue(degree.sciRequirement)

    def testSocSciApproval(self):
        degree = Degree()
        degree.addCourse(Course.objects.get(course_code="GGR111H5"))
        degree.addCourse(Course.objects.get(course_code="ECO101H5"))
        degree.evaluate_requirements()
        self.assertTrue(degree.socsciRequirement)
