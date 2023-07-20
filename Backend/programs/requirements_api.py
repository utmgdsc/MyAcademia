from courses.models import Course
import re
from typing import List
from regex_constants import *
from parser import PrereqParser,prereq_filter
"""
Designing the API for Degree-Explorer
"""


class Requirementalgo:
    courses_reqd: list[Course]
    description: str
    isCompleted: bool
    req_type: str
    courses_taken: list[Course]
    count: int
    applied_course: list[Course]

    def __init__(self, coursesReqd, description, courses_taken,req_type):
        self.courses_reqd = coursesReqd
        self.description = description
        self.isCompleted = False
        self.req_type = req_type
        self.courses_taken = courses_taken
        self.applied_course=[]
        #self.count = count

    def addCourse(self, course: Course):
        self.courses_reqd.append(course)

    def removeCourse(self, course: Course):
        self.courses_taken.remove(course)

    def addAppliedCourses(self, course: Course):
        """
          This function is used to add the courses that are applied by the user
        """
        if course.code in self.courses_reqd:
            self.applied_course.append(course)
        #pre_req=Course.objects.filter(course_code=course.course_code).values_list('pre_req',flat=True)






    def evaluate_req(self):
        pass

    def curr_credits(self):
        curr_credits = 0
        for course in self.courses_taken:
            curr_credits += course.credit
        return curr_credits

    def getcourses_reqd(self):
        return self.courses_reqd


class MiscBasedProgramRequirement(Requirementalgo):
    def __init__(self, coursesReqd, description, courses_applied, req_type):
        super().__init__(coursesReqd, description, courses_applied, req_type)

    def evaluate_req(self):
        # need to encounter multiple cases of req_type
        if self.req_type == "COURSES/NUM/LIST":
            # Just check for courses, no count attribute
            for course in self.courses_taken:
                if course not in self.courses_reqd:
                    self.isCompleted = False
                    return
            self.isCompleted = True
        elif self.req_type == "PROHIBITED_POST" or self.req_type == "MAXIMUM" or self.req_type == "UNVERIFIABLE":
            # no info about this
            pass





class CreditBasedRequirement(Requirementalgo):
    credits_reqd: float

    def __init__(self, coursesReqd, description, courses_applied, credits_reqd,req_type):
        super().__init__(coursesReqd, description, courses_applied,req_type)
        self.credits_reqd = credits_reqd

    def evaluate_req(self):
        curr_credits = self.curr_credits()
        counter_chk = 0
        if self.req_type == 'COURSES/FCES/MIN' or self.req_type == 'COURSES/FCES/GROUPMIN':
            # Atleast x.0 credits condition
            if curr_credits >= self.credits_reqd:
                for course in self.courses_taken:
                    if course in self.courses_reqd:
                        counter_chk += course.credit
                if counter_chk >= self.credits_reqd:
                    self.isCompleted = True
                    return
            self.isCompleted = False
        elif self.req_type == 'COURSES/FCES/GROUPMAX':
            # Atmost x.0 credits condition
            if curr_credits >= self.credits_reqd:
                for course in self.courses_taken:
                    if course in self.courses_reqd:
                        counter_chk += course.credit
                if counter_chk == self.credits_reqd:
                    self.isCompleted = True
                    return
            self.isCompleted = False


class CourseBasedRequirement(Requirementalgo):
    num_courses_reqd: int

    def __init__(self, coursesReqd, description, courses_applied, req_type, num_courses_reqd):
        super().__init__(coursesReqd, description, courses_applied)
        self.req_type = req_type
        self.num_courses_reqd = num_courses_reqd

    def evaluate_req(self):
        counter_chk = 0
        num_courses = len(self.courses_taken)
        if num_courses >= self.num_courses_reqd:
            for req_type in self.req_type:
                if req_type == 'COURSES/NUM/MIN':
                    for course in self.courses_taken:
                        if course in self.courses_reqd:
                            counter_chk += 1
                            if counter_chk == self.num_courses_reqd:
                                self.isCompleted = True
                                return

            self.isCompleted = False


class CategoriesBasedRequirement(Requirementalgo):
    num_categories_reqd: int / float
    pre_req_list: list[Requirementalgo]
    categories: list[str]

    def __init__(self, coursesReqd, description, courses_applied, req_type, pre_req_list,categories):
        super().__init__(coursesReqd, description, courses_applied)
        self.req_type = req_type
        self.num_categories_reqd = num_categories_reqd
        self.pre_req_list = pre_req_list
        self.categories = categories

    def evaluate_req(self):
        #Have a list of all courses ready

        courses=Course.objects.all()
        if self.req_type=="CATEGORIES/FCES/MIN":
            #Atleast x.0 credits condition
            if self.courses_reqd:
                self.req_type="COURSES/FCES/MIN"
                CreditBasedRequirement.evaluate_req(self)
                return

            elif self.categories:
                for category in self.categories:
                    pass
            pass
