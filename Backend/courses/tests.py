from django.test import TestCase
from .models import Course

# Create your tests here.

class CourseTestCase(TestCase):

    def test_course_creation(self):
        print("Testing Course Model")
        # Test that a course can be created and saved to the database
        Course.objects.create(course_code="testCourse", title="Intro to Computer Programming", credit=1.0, recommended_prep="None", distribution="None", pre_req="None", exclusions="None", 
                              description="An introduction to computer programming.", program_area="Computer Science")
        course1 = Course.objects.get(course_code="testCourse")
        self.assertEqual(course1.course_code, "testCourse")
        self.assertEqual(course1.title, "Intro to Computer Programming")
        self.assertEqual(course1.credit, 1.0)
        self.assertEqual(course1.recommended_prep, "None")
        self.assertEqual(course1.distribution, "None")
        self.assertEqual(course1.pre_req, "None")
        self.assertEqual(course1.exclusions, "None")
        self.assertEqual(course1.description, "An introduction to computer programming.")
        self.assertEqual(course1.program_area, "Computer Science")
        Course.objects.get(course_code="testCourse").delete() # Delete the course after testing




    