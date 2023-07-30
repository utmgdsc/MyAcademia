from Courses.course import Course
from programs.models import Program, Requirement

from Backend.programs.DegreeExplorer.parser.ExclusionParser import \
    ExclusionParser
from DegreeAPI import Degree
import re
"""
The purpose of this class is to generate a graph of the user's degree and
suggest courses that the user should take next to fulfill their degree
requirements.
"""


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

        # remove all the exclusions
        user_courses_str = self.degree.getCoursesString()
        for course in humanities_courses:
            exclusion = ExclusionParser(course.exclusions, user_courses_str)
            if not exclusion.checkCourseApproval():
                humanities_courses = humanities_courses.exclude(course_code=course.course_code)

        # remove courses for which the user doesn't have pre-reqs

        return humanities_courses

    def suggestSocialScienceElective(self):
        ssc_course = Course.objects.filter(distribution=Course.SOCIAL_SCIENCE)
        courses_to_remove = []
        for course in self.degree.user_courses:
            if course in ssc_course:
                courses_to_remove.append(course)
        for course in courses_to_remove:
            ssc_course = ssc_course.exclude(course_code=course.course_code)

        # remove all the exclusions
        user_courses_str = self.degree.getCoursesString()
        for course in ssc_course:
            exclusion = ExclusionParser(course.exclusions, user_courses_str)
            if not exclusion.checkCourseApproval():
                ssc_course = ssc_course.exclude(course_code=course.course_code)

        # remove courses for which the user doesn't have pre-reqs

        return ssc_course

    def suggestScienceElective(self):
        sci_course = Course.objects.filter(distribution=Course.SCIENCE)
        courses_to_remove = []
        for course in self.degree.user_courses:
            if course in sci_course:
                courses_to_remove.append(course)
        for course in courses_to_remove:
            sci_course = sci_course.exclude(course_code=course.course_code)

        # remove all the exclusions
        user_courses_str = self.degree.getCoursesString()
        for course in sci_course:
            exclusion = ExclusionParser(course.exclusions, user_courses_str)
            if not exclusion.checkCourseApproval():
                sci_course.exclude(course_code=course.course_code)

        # remove courses for which the user doesn't have pre-reqs
        return sci_course


    def suggest200L(self):
        courses = Course.objects.filter(course_code__regex=r'^[A-Z]{3}2[0-9]{2}$')

        # more to do
    def suggest300L(self):
        courses = Course.objects.filter(course_code__regex=r'^[A-Z]{3}3[0-9]{2}$')

        # more to do

    def getExclusionCourses(self):
        for course in degree.user_courses:
            pass


    def generate_graph(self):
        pass












