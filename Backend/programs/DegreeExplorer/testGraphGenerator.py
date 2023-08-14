from django.test import TestCase
from courses.models import Course
from programs.DegreeExplorer.DegreeAPI import Degree
from programs.models import Program, Requirement
from programs.DegreeExplorer.Generator import Generator

"""
Test Case 1: Course Suggestion for a CS Minor Program 
             (No Previous Courses Taken)

Basic Background:
    - The degree program consists of several courses (referred to as X courses).
    - None of the courses in the degree program are used to fulfill requirements 
      in the user's program.

Test Case Scenario:
    In this test case, we aim to showcase the functionality of the graph generator 
    in suggesting courses for a user who has not yet taken any courses in their 
    CS Minor program. The graph generator recommends courses based on prerequisites 
    and course relationships.

Degree Program (CS Minor) Courses:
    - CSC108H5: No pre-reqs
    - MAT102H5: No pre-reqs
    - MAT135H5: No pre-reqs
    - MAT136H5: MAT135H5
    - CSC148H5: CSC108H5
    - CSC207H5: CSC148H5
    - CSC209H5: CSC207H5
    - CSC263H5: CSC207H5 and CSC236H5 and (STA246H5 or STA256H5)
    - CSC258H5: CSC148H5
    - CSC236H5: CSC148H5 and MAT102H5

User Inputs:
    - Program: CS Minor
    - Completed Degree Courses: None
    - Semester Length: 1 semester (Fall or Winter) and 2 semesters (Fall and Winter)

Expected Output:
Given that the user has not yet taken any courses, the graph generator should 
recommend the following courses for 1 semester length:
    1. CSC108H5
    2. MAT102H5
    3. MAT135H5
    
Given that the user has not yet taken any courses, the graph generator should
recommend the following courses for 2 semester length (or year long):
    1. CSC108H5
    2. MAT102H5
    3. MAT135H5
    4. MAT136H5
    5. CSC148H5

These are the only options available for the user, as they have not completed 
any courses that could influence the recommendations.

Note: The provided test case documentation assumes that the graph generator 
suggests courses based on prerequisites and course relationships, 
and the output is generated accordingly.
"""


class GraphGeneratorTest(TestCase):
    def setUp(self):
       # adding cs minor program courses to database
        Course.objects.create(course_code="CSC108H5", title="Intro to CS",
                                description="Introduction to computer science",
                                credit="0.5", distribution="Science",
                                pre_req="None", exclusions="")
        Course.objects.create(course_code="MAT102H5", title="Intro to Math",
                                description="Introduction to math",
                                credit="0.5", distribution="Science",
                                pre_req="None", exclusions="")
        Course.objects.create(course_code="MAT135H5", title="Calculus I",
                                description="Introduction to calculus",
                                credit="0.5", distribution="Science",
                                pre_req="None", exclusions="")
        Course.objects.create(course_code="MAT136H5", title="Calculus II",
                                description="Introduction to calculus",
                                credit="0.5", distribution="Science",
                                pre_req="MAT135H5", exclusions="")
        Course.objects.create(course_code="CSC148H5", title="Intro to CS II",
                                description="Introduction to computer science",
                                credit="0.5", distribution="Science",
                                pre_req="CSC108H5", exclusions="")
        Course.objects.create(course_code="CSC207H5", title="Software Design",
                                description="Introduction to software design",
                                credit="0.5", distribution="Science",
                                pre_req="CSC148H5", exclusions="")
        Course.objects.create(course_code="CSC209H5", title="Software Tools",
                                description="Introduction to software tools",
                                credit="0.5", distribution="Science",
                                pre_req="CSC207H5", exclusions="")
        Course.objects.create(course_code="CSC263H5", title="Data Structures",
                                description="Introduction to data structures",
                                credit="0.5", distribution="Science",
                                pre_req="CSC207H5 and CSC236H5 and (STA246H5 or STA256H5)", exclusions="")
        Course.objects.create(course_code="CSC258H5", title="Computer Organization",
                                description="Introduction to computer organization",
                                credit="0.5", distribution="Science",
                                pre_req="CSC148H5", exclusions="")
        Course.objects.create(course_code="CSC236H5", title="Discrete Math",
                                description="Introduction to discrete math",
                                credit="0.5", distribution="Science",
                                pre_req="CSC148H5 and MAT102H5", exclusions="")

    def testGraphGeneratorSem1(self):
        """
        This test is used to suggest courses for a user who has not yet taken
        any courses in their CS Minor program. The graph generator recommends
        courses for the first semester (Fall or Winter) of the user's program.
        """
        # adding cs minor courses
        program_courses = Course.objects.filter(course_code__in=["CSC108H5", "MAT102H5", "MAT135H5", "MAT136H5",
                                                                 "CSC148H5", "CSC207H5", "CSC209H5", "CSC263H5",
                                                                 "CSC258H5", "CSC236H5"])
        program_courses = list(program_courses)
        degree = Degree()

        # Generating courses for the first semester of the user's program
        generator = Generator(degree, 1, "FILLER")

        # Expected Output: CSC108H5, MAT102H5, MAT135H5
        retVal = generator.suggestProgramCourse(program_courses)
        # for course in retVal:
        #     print(course.course_code)
        self.assertIn(Course.objects.get(course_code="CSC108H5"), retVal)
        self.assertIn(Course.objects.get(course_code="MAT102H5"), retVal)
        self.assertIn(Course.objects.get(course_code="MAT135H5"), retVal)

    def testGraphGeneratorSem2(self):
        """
        This test is used to suggest courses for a user who has not yet taken
        any courses in their CS Minor program. The graph generator recommends
        courses for both of the semesters (Fall and Winter) of the user's
        program.
        """
        # adding cs minor courses
        program_courses = Course.objects.filter(course_code__in=["CSC108H5", "MAT102H5", "MAT135H5", "MAT136H5",
                                                                 "CSC148H5", "CSC207H5", "CSC209H5", "CSC263H5",
                                                                 "CSC258H5", "CSC236H5"])
        program_courses = list(program_courses)
        degree = Degree()

        # Generating courses for the first semester of the user's program
        generator = Generator(degree, 2, "FILLER")

        # Expected Output: CSC108H5, MAT102H5, MAT135H5
        retVal = generator.suggestProgramCourse(program_courses)

        self.assertIn(Course.objects.get(course_code="CSC108H5"), retVal)
        self.assertIn(Course.objects.get(course_code="MAT102H5"), retVal)
        self.assertIn(Course.objects.get(course_code="MAT135H5"), retVal)
        self.assertIn(Course.objects.get(course_code="MAT136H5"), retVal)
        self.assertIn(Course.objects.get(course_code="CSC148H5"), retVal)


"""
Test Case 2: Course Suggestion for a CS Minor Program 
             (Previous Courses Taken towards Program completion)

Basic Background:
    - The degree program consists of several courses (referred to as X courses).
    - Each course contributes towards the completion of the degree program 
      and 

Test Case Scenario:
    In this test case, we aim to showcase the functionality of the graph generator 
    in suggesting courses for a user who has not yet taken any courses in their 
    CS Minor program. The graph generator recommends courses based on prerequisites 
    and course relationships.

Degree Program (CS Minor) Courses:
    - CSC108H5: No pre-reqs
    - MAT102H5: No pre-reqs
    - MAT135H5: No pre-reqs
    - MAT136H5: MAT135H5
    - CSC148H5: CSC108H5
    - CSC207H5: CSC148H5
    - CSC209H5: CSC207H5
    - CSC263H5: CSC207H5 and CSC236H5 and (STA246H5 or STA256H5)
    - CSC258H5: CSC148H5
    - CSC236H5: CSC148H5 and MAT102H5

User Inputs:
    - Program: CS Minor
    - Completed Degree Courses: None
    - Semester Length: 1 semester (Fall or Winter) and 2 semesters (Fall and Winter)

Expected Output:
Given that the user has not yet taken any courses, the graph generator should 
recommend the following courses for 1 semester length:
    1. CSC108H5
    2. MAT102H5
    3. MAT135H5
    
Given that the user has not yet taken any courses, the graph generator should
recommend the following courses for 2 semester length:
    1. CSC108H5
    2. MAT102H5
    3. MAT135H5
    4. MAT136H5
    5. CSC148H5

These are the only options available for the user, as they have not completed 
any courses that could influence the recommendations.

Note: The provided test case documentation assumes that the graph generator 
suggests courses based on prerequisites and course relationships, 
and the output is generated accordingly.
"""

