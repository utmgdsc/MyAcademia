from django.test import TestCase
from .models import Course

# Create your tests here.

class CourseTestCase(TestCase):

    def setUp(self):
        Course.objects.create(course_code="CSC300H5", title="Intro to Computer Programming", credit=0.5, recommended_prep="None", 
                              distribution="Science", pre_req="CSC108", exclusions="None",)
        Course.objects.create(course_code="CSC400H5", title="Second Intro to Computer Programming", credit=0.5, recommended_prep="None", 
                              distribution="Science", pre_req="Grade 12 advanced Functions", exclusions="None",)
        Course.objects.create(course_code="CSC367H5", title="Third Intro to Computer Programming", credit=0.5, recommended_prep="None", 
                              distribution="Social Science", pre_req="CSC232", exclusions="None", program_area="Computer Science")
        Course.objects.create(course_code="CSC260H5", title="Third Intro to Computer Programming", credit=0.5, recommended_prep="None", 
                              distribution="Special Science", pre_req="CSC363 and CSC108 and CSC232", exclusions="None",program_area="Special Program Area")
        Course.objects.create(course_code="GGR148H5", title="Fourth Intro to Computer Programming", credit=1.0, recommended_prep="None", 
                              distribution="Humanities", pre_req="GGR167", exclusions="None",)
        Course.objects.create(course_code="GGR352H5", title="FifthIntro to Computer Programming", credit=0.5, recommended_prep="None", 
                              distribution="Social Science", pre_req="None", exclusions="None",program_area="Geographical Sciences")
        Course.objects.create(course_code="ENV300H5", title="Sixth Intro to Computer Programming", credit=1.0, recommended_prep="None", 
                              distribution="Humanities", pre_req="CSC363 and GGR167", exclusions="None",)
        Course.objects.create(course_code="KIN450H5", title="Seventh Intro to Computer Programming", credit=0.5, recommended_prep="None", 
                              distribution="Science", pre_req="CSC258", exclusions="None",)
        Course.objects.create(course_code="LKW250H5", title="Eigth Intro to Computer Programming", credit=1.0, recommended_prep="None", 
                              distribution="Social Science", pre_req="CSC232", exclusions="None",)
        Course.objects.create(course_code="CSC358H5", title="Ninth Intro to Computer Programming", credit=0.5, recommended_prep="None", 
                              distribution="Science", pre_req="CSC493", exclusions="None", program_area="Computer Science")

    def test_course_creation(self):
        print("\nTesting Course Model")
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

    def test_course_filters(self):
        print("\nTesting course filters")

        print("Testing get by program code")
        course = Course.objects.get(course_code="CSC300H5")
        self.assertEqual(course.course_code, "CSC300H5")
        print("Program Code OK")

        print("Testing course title")
        courses = Course.objects.filter(title="Intro to Computer Programming")
        self.assertEqual(len(courses), 1)
        for course in courses:
            self.assertEqual(course.title, "Intro to Computer Programming")
        print("Course Title OK")

        print("Testing distribution")
        courses = Course.objects.filter(distribution = "Science")
        self.assertEqual(len(courses), 4)
        for course in courses:
            self.assertEqual(course.distribution, "Science")
        print("Distribution OK")

        print("Testing credit")
        courses = Course.objects.filter(credit = 0.5)
        self.assertEqual(len(courses), 7)
        for course in courses:
            self.assertEqual(course.credit, 0.5)
        print("Credit OK")

        print("Testing pre_req")
        courses = Course.objects.filter(pre_req__icontains="CSC363")
        self.assertEqual(len(courses), 2)
        print("Pre_req OK")

        print("Testing program_area")
        courses = Course.objects.filter(program_area__icontains="Computer Science")
        self.assertEqual(len(courses), 2)
        print("Program Area OK")


    def test_course_regex(self):
        print("\nTesting course code regex")
        courses = Course.objects.filter(course_code__regex=r'^[A-Z]{3}(3\d{2}|4\d{2})(H5|Y5)$')
        self.assertEqual(len(courses), 7) # 
        for course in courses:
            print(course.course_code)

    def test_Course_Search_Endpoint(self):
        url = "http://127.0.0.1:8000/api/courseSearch/"
        print("\nTesting course search endpoint")

        print("Testing with empty request")
        data = {}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 0)
        print("Empty request OK")

        print("Testing with complete course Code")
        data = {"course_code": "CSC300H5"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['course_code'], "CSC300H5")
        print("Complete course code OK")

        print("Testing with partial course code")
        data = {"course_code": "CSC367"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['course_code'], "CSC367H5")
        print("Partial course code OK")

        print("Testing with pre_req")
        data = {"pre_req": "CSC363"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

        print("Testing with distribution")
        data = {"distribution": "Science"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)

        print("Testing with program_area")
        data = {"program_area": "Computer Science"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

        print("Testing with multiple filters")
        data = {"pre_req": "CSC232", "distribution": "Special Science", "program_area": "Special Program Area"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['course_code'], "CSC260H5")




    