from Courses.course import Course
from programs.models import Program, Requirement
from degreeAPI import Degree


class Generator:
    semester_length: int
    program: Program
    degree: Degree

    def __init__(self, semester_length, program, degree):
        self.semester_length = semester_length
        self.program = Program.objects.get(program_code=program)
        self.degree = degree


    def suggestDegreeCourse(self):
        """
        This method will suggest a course to the user based on the user's degree
        requirements and the courses they have already taken.

        :return: a course that the user should take next to fulfill their
        degree requirements
        """
        incomplete_requirements = self.degree.evaluate_requirements()

        #
        if "Humanities" in incomplete_requirements and "min200LR" in incomplete_requirements:
            pass
        elif "Humanities" in incomplete_requirements and "min300LR" in incomplete_requirements:
            pass
        elif "Humanities" in incomplete_requirements:
            pass

    def suggestHumanitiesElective(self):
        humanities_courses = Course.objects.filter(distribution=Course.HUMANITIES)
        courses_to_remove = []
        for course in self.degree.user_courses:
            if course in humanities_courses:
                courses_to_remove.append(course)

        for course in courses_to_remove:
            humanities_courses = humanities_courses.exclude(course_code=course.course_code)

        return humanities_courses


    def suggestSocialScienceElective(self):
        ssc_course = Course.objects.filter(distribution=Course.SOCIAL_SCIENCE)
        courses_to_remove = []
        for course in self.degree.user_courses:
            if course in ssc_course:
                courses_to_remove.append(course)
        for course in courses_to_remove:
            ssc_course = ssc_course.exclude(course_code=course.course_code)
        return ssc_course

    def suggestScienceElective(self):
        sci_course = Course.objects.filter(distribution=Course.SCIENCE)
        courses_to_remove = []
        for course in self.degree.user_courses:
            if course in sci_course:
                courses_to_remove.append(course)
        for course in courses_to_remove:
            sci_course = sci_course.exclude(course_code=course.course_code)
        return sci_course


    def generate_graph(self):
        pass












