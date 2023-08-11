from courses.models import Course
from programs.models import Program, Requirement

from programs.DegreeExplorer.parser.ExclusionParser import \
    ExclusionParser


from .DegreeAPI import Degree
import re

from .parser.PrereqParser import PrereqParser

"""
The purpose of this class is to generate a list of courses that the user should
take next to fulfill their degree requirements. This takes into account various
requirements to either complete a program requirement or to fulfill a breadth
requirement.
"""
class Generator:
    semester_length: int
    program: Program
    degree: Degree

    def __init__(self, degree):
        # self.semester_length = semester_length
        # self.program = Program.objects.get(program_code=program)
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
            courses = self.suggestHumanitiesElective()
            courses.objects.filter(course_code__regex=r'^[A-Z]{3}2[0-9]{2}H5$')
            return courses
        elif "Humanities" in incomplete_requirements and "min300LR" in incomplete_requirements:
            courses = self.suggestHumanitiesElective()
            courses.objects.filter(course_code__regex=r'^[A-Z]{3}3[0-9]{2}H5$')
            return courses
        elif "Humanities" in incomplete_requirements:
            courses = self.suggestHumanitiesElective()
            return courses

        if "Social Science" in incomplete_requirements and "min200LR" in incomplete_requirements:
            courses = self.suggestSocialScienceElective()
            courses.objects.filter(course_code__regex=r'^[A-Z]{3}2[0-9]{2}H5$')
            return courses
        elif "Social Science" in incomplete_requirements and "min300LR" in incomplete_requirements:
            courses = self.suggestSocialScienceElective()
            courses.objects.filter(course_code__regex=r'^[A-Z]{3}3[0-9]{2}H5$')
            return courses
        elif "Social Science" in incomplete_requirements:
            courses = self.suggestSocialScienceElective()
            return courses

        if "Science" in incomplete_requirements and "min200LR" in incomplete_requirements:
            courses = self.suggestScienceElective()
            courses.objects.filter(course_code__regex=r'^[A-Z]{3}2[0-9]{2}H5$')
            return courses
        elif "Science" in incomplete_requirements and "min300LR" in incomplete_requirements:
            courses = self.suggestScienceElective()
            courses.objects.filter(course_code__regex=r'^[A-Z]{3}3[0-9]{2}H5$')
            return courses
        elif "Science" in incomplete_requirements:
            courses = self.suggestScienceElective()
            return courses

    def suggestHumanitiesElective(self):
        """
        This method will suggest a humanities elective to the user based on the
        user's degree requirements and the courses they have already taken.

        :return: Humanities elective course that the user should take next to
        fulfill their degree requirements
        """
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
        for course in humanities_courses:
            parser_preq = PrereqParser(course.pre_req, self.degree.getCoursesString())
            if not parser_preq.evaluatePrereq():
                humanities_courses = humanities_courses.exclude(course_code=course.course_code)

        return humanities_courses

    def suggestSocialScienceElective(self):
        """
        This method will suggest a social science elective to the user based on
        the user's degree requirements and the courses they have already taken.

        :return: Social science elective course that the user should take next
        to fulfill their degree requirements
        """
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
        for course in ssc_course:
            parser_preq = PrereqParser(course.pre_req, self.degree.getCoursesString())
            if not parser_preq.evaluatePrereq():
                ssc_course = ssc_course.exclude(course_code=course.course_code)

        return ssc_course

    def suggestScienceElective(self):
        """
        This method will suggest a science elective to the user based on the
        user's degree requirements and the courses they have already taken.

        :return: Science elective course that the user should take next to
        fulfill their degree requirements
        """
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
        for course in sci_course:
            parser_preq = PrereqParser(course.pre_req, self.degree.getCoursesString())
            if not parser_preq.evaluatePrereq():
                sci_course = sci_course.exclude(course_code=course.course_code)

        return sci_course

    def suggest200L(self):
        """
        This method will suggest a 200 level course to the user based on the
        user's degree requirements and the courses they have already taken.

        :return: 200 level course that the user should take next to fulfill
        their degree requirements
        """
        courses = Course.objects.filter(course_code__regex=r'^[A-Z]{3}2[0-9]{2}H5$')
        user_courses_str = self.degree.getCoursesString()
        for course in courses:
            exclusion = ExclusionParser(course.exclusions, user_courses_str)
            if not exclusion.checkCourseApproval():
                courses = courses.exclude(course_code=course.course_code)

        for course in courses:
            parser_preq = PrereqParser(course.pre_req, self.degree.getCoursesString())
            if not parser_preq.evaluatePrereq():
                courses = courses.exclude(course_code=course.course_code)

        return courses

    def suggest300L(self):
        """
        This method will suggest a 300 level course to the user based on the
        user's degree requirements and the courses they have already taken.

        :return: 300 level course that the user should take next to fulfill
        their degree requirements
        """
        courses = Course.objects.filter(course_code__regex=r'^[A-Z]{3}3[0-9]{2}H5$')
        user_courses_str = self.degree.getCoursesString()
        for course in courses:
            exclusion = ExclusionParser(course.exclusions, user_courses_str)
            if not exclusion.checkCourseApproval():
                courses = courses.exclude(course_code=course.course_code)

        for course in courses:
            parser_preq = PrereqParser(course.pre_req, self.degree.getCoursesString())
            if not parser_preq.evaluatePrereq():
                courses = courses.exclude(course_code=course.course_code)

        return courses
