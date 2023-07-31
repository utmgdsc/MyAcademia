from django.test import TestCase
from courses.models import Course
from programs.DegreeExplorer.DegreeAPI import Degree
# from programs.models import Program, Requirement


class DegreeExplorerTestCase(TestCase):
    def setUp(self):
        Course.objects.create(course_code="CSC108H5", title="Intro to CS", description="Intro to CS",
                              pre_req="None", exclusions="None", distribution="None",
                              program_area="None", credit=0.5)
        Course.objects.create(course_code="PUN212Y5", title="Intro to Punjabi", description="Intro to Punjabi",
                                pre_req="None", exclusions="None", distribution="None",
                                program_area="None", credit=1.0)
        Course.objects.create(course_code="LIN204H5", title="Intro to Linguistics", description="Intro to Linguistics",
                                pre_req="None", exclusions="None", distribution="None",
                                program_area="None", credit=0.5)
        Course.objects.create(course_code="CSC148H5", title="Intro to CS II", description="Intro to CS II",
                                pre_req="None", exclusions="None", distribution="None",
                                program_area="None", credit=0.5)
        Course.objects.create(course_code="CSC207H5", title="Software Design", description="Software Design",
                                pre_req="None", exclusions="None", distribution="None",
                                program_area="None", credit=0.5)

    #    GGR111
        Course.objects.create(course_code="GGR111H5", title="Intro to Human Geography", description="Intro to Human Geography",
                                pre_req="None", exclusions="None", distribution="None",
                                program_area="None", credit=0.5)
    #     ECO101
        Course.objects.create(course_code="ECO101H5", title="Intro to Microeconomics", description="Intro to Microeconomics",
                                pre_req="None", exclusions="None", distribution="None",
                                program_area="None", credit=0.5)



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
        print()
        degree.evaluate_requirements()
        self.assertTrue(degree.sscRequirement)
