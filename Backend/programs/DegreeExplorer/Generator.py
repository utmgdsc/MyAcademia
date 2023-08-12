from typing import Dict, List

from courses.models import Course
from programs.models import Program, Requirement

from programs.DegreeExplorer.parser.ExclusionParser import \
    ExclusionParser

from .DegreeAPI import Degree
import re

utmCourseRegex = re.compile(r'^[A-Z]{3}[0-9]{3}[A-Z][0-9]$')

from .parser.PrereqParser import PrereqParser

import re

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

    def __init__(self, degree, semester_length, program):
        self.semester_length = semester_length
        self.program = "Program.objects.get(program_code=program)"
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
        humanities_courses = Course.objects.filter(
            distribution=Course.HUMANITIES)
        courses_to_remove = []
        for course in self.degree.user_courses:
            if course in humanities_courses:
                courses_to_remove.append(course)

        for course in courses_to_remove:
            humanities_courses = humanities_courses.exclude(
                course_code=course.course_code)

        # remove all the exclusions
        user_courses_str = self.degree.getCoursesString()
        for course in humanities_courses:
            exclusion = ExclusionParser(course.exclusions, user_courses_str)
            if not exclusion.checkCourseApproval():
                humanities_courses = humanities_courses.exclude(
                    course_code=course.course_code)

        # remove courses for which the user doesn't have pre-reqs
        for course in humanities_courses:
            parser_preq = PrereqParser(course.pre_req,
                                       self.degree.getCoursesString())
            if not parser_preq.evaluatePrereq():
                humanities_courses = humanities_courses.exclude(
                    course_code=course.course_code)

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
            parser_preq = PrereqParser(course.pre_req,
                                       self.degree.getCoursesString())
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
            parser_preq = PrereqParser(course.pre_req,
                                       self.degree.getCoursesString())
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
        courses = Course.objects.filter(
            course_code__regex=r'^[A-Z]{3}2[0-9]{2}H5$')
        user_courses_str = self.degree.getCoursesString()
        for course in courses:
            exclusion = ExclusionParser(course.exclusions, user_courses_str)
            if not exclusion.checkCourseApproval():
                courses = courses.exclude(course_code=course.course_code)

        for course in courses:
            parser_preq = PrereqParser(course.pre_req,
                                       self.degree.getCoursesString())
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
        courses = Course.objects.filter(
            course_code__regex=r'^[A-Z]{3}3[0-9]{2}H5$')
        user_courses_str = self.degree.getCoursesString()
        for course in courses:
            exclusion = ExclusionParser(course.exclusions, user_courses_str)
            if not exclusion.checkCourseApproval():
                courses = courses.exclude(course_code=course.course_code)

        for course in courses:
            parser_preq = PrereqParser(course.pre_req,
                                       self.degree.getCoursesString())
            if not parser_preq.evaluatePrereq():
                courses = courses.exclude(course_code=course.course_code)

        return courses

    def suggestProgramCourse(self, program_courses: List[Course]):
        program_courses = program_courses
        vertexDict = {}
        for course in program_courses:
            course_vertex = Vertex(course)
            vertexDict[course.course_code] = course_vertex
        graph = Graph(vertexDict, self.degree.user_courses)
        graph.build_graph()
        suggestion = graph.suggestCourses()
        return suggestion


class Vertex:
    course: Course
    level: int
    visited: bool

    def __init__(self, course: Course):
        self.level = 0
        self.visited = False
        self.course = course

    def visited(self):
        self.visited = True


class Graph:
    vertices: Dict[str, Vertex]
    adj_list: Dict[Vertex, List[Vertex]]
    vertex_by_level: Dict[int, List[Vertex]]

    def __init__(self, vertices, user_course):
        self.vertices = vertices
        self.adj_list = {}
        self.vertex_by_level = {}
        self.user_courses = user_course

    def add_edge(self, u: Vertex, v: Vertex) -> None:
        if u is None and v is not None:
            self.adj_list[v] = []
            if v.level not in self.vertex_by_level:
                self.vertex_by_level[v.level] = [v]
            else:
                self.vertex_by_level[v.level].append(v)
            return
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v is not None:
            if v not in self.adj_list[u]:
                self.adj_list[u].append(v)
            if v.level < u.level + 1:
                if v in self.vertex_by_level[v.level]:
                    self.vertex_by_level[v.level].remove(v)
                v.level = u.level + 1
            if v.level not in self.vertex_by_level:
                self.vertex_by_level[v.level] = [v]
            else:
                self.vertex_by_level[v.level].append(v)

    def build_graph(self) -> None:
        for vertex in self.vertices:
            if not (self.vertices[vertex].course.pre_req == "None" or "Grade 12" in self.vertices[vertex].course.pre_req):
                courses_in_pre_req = re.findall(utmCourseRegex, self.vertices[vertex].course.pre_req)
                for course_new in courses_in_pre_req:
                    try:
                        vertex2 = self.vertices[course_new]
                    except:
                        continue
                    self.add_edge(vertex2,self.vertices[vertex])
            else:
                self.add_edge(None, self.vertices[vertex])

    def suggestCourses(self) -> List[Vertex]:
        suggested_courses = []
        isLevelComplete = False
        for level in self.vertex_by_level:
            if isLevelComplete:
                break
            for vertex in self.vertex_by_level[level]:
                if vertex.visited:
                    for v in self.adj_list[vertex]:
                        if not v.visited:
                            suggested_courses.append(v)
                else:
                    isLevelComplete = True
                    suggested_courses.append(vertex)
        for val in suggested_courses:
            parser = PrereqParser(val.course.pre_req, self.user_courses)
            if not parser.evaluatePrereq():
                suggested_courses.remove(val)
        retValCourses = []
        for val in suggested_courses:
            retValCourses.append(val.course)
            # print(val.course.course_code)
        return retValCourses


