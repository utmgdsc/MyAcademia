from courses.models import Course
import re
from typing import List
from regex_constants import *
from parser import PrereqParser, prereq_filter

"""
Designing the API for Degree-Explorer
"""


class Requirementalgo:
    courses_reqd: list[Course]
    description: str
    isCompleted: bool
    req_type: str
    user_courses: list[Course]  # User Courses
    count: int
    applied_course: list[Course]

    def __init__(self, coursesReqd, description, courses_taken, req_type):
        self.courses_reqd = coursesReqd
        self.description = description
        self.isCompleted = False
        self.req_type = req_type
        self.user_courses = courses_taken
        self.applied_course = []
        # self.count = count

    def addCourse(self, course: Course):
        self.courses_reqd.append(course)

    def removeCourse(self, course: Course):
        self.user_courses.remove(course)

    def addAppliedCourses(self, course: Course):
        """
          This function is used to add the courses that are applied by the user
        """
        self.applied_course.append(course)
        # pre_req=Course.objects.filter(course_code=course.course_code).values_list('pre_req',flat=True)

    def evaluate_req(self):
        pass

    def getcourses_reqd(self):
        return self.courses_reqd


def curr_credits(user_courses: list[Course]):
    """
    This function is used to calculate the current credits of the user
    """
    curr_credits = 0
    for course in user_courses:
        curr_credits += course.credit
    return curr_credits


class MiscBasedProgramRequirement(Requirementalgo):
    def __init__(self, coursesReqd, description, courses_applied, req_type):
        super().__init__(coursesReqd, description, courses_applied, req_type)

    def evaluate_req(self):
        # need to encounter multiple cases of req_type
        if self.req_type == "COURSES/NUM/LIST":
            # Just check for courses, no count attribute
            for course in self.user_courses:
                if course not in self.courses_reqd:
                    self.isCompleted = False
                    return
                elif course in self.courses_reqd:
                    self.addAppliedCourses(course)

            self.isCompleted = True
        elif self.req_type == "PROHIBITED_POST" or self.req_type == "MAXIMUM" or self.req_type == "UNVERIFIABLE":
            # no info about this
            pass


class CreditBasedRequirement(Requirementalgo):
    credits_reqd: float

    def __init__(self, coursesReqd, description, courses_taken, credits_reqd, req_type):
        super().__init__(coursesReqd, description, courses_taken, req_type)
        self.credits_reqd = credits_reqd

    def evaluate_req(self):
        curr_credits = curr_credits(self.user_courses)
        counter_chk = 0
        if self.req_type == 'COURSES/FCES/MIN' or self.req_type == 'COURSES/FCES/GROUPMIN':
            # Atleast x.0 credits condition
            if curr_credits >= self.credits_reqd:
                for course in self.user_courses:
                    if course in self.courses_reqd:
                        self.addAppliedCourses(course)
                        counter_chk += course.credit
                if counter_chk >= self.credits_reqd:
                    self.isCompleted = True
                    return
            self.isCompleted = False
            self.applied_course = []
        elif self.req_type == 'COURSES/FCES/GROUPMAX':
            # Atmost x.0 credits condition
            if curr_credits >= self.credits_reqd:
                for course in self.user_courses:
                    if course in self.courses_reqd:
                        self.addAppliedCourses(course)
                        counter_chk += course.credit
                if counter_chk == self.credits_reqd:
                    self.isCompleted = True
                    return
            self.isCompleted = False
            self.applied_course = []


class CourseBasedRequirement(Requirementalgo):
    num_courses_reqd: int

    def __init__(self, coursesReqd, description, courses_taken, req_type, num_courses_reqd):
        super().__init__(coursesReqd, description, courses_taken, req)
        self.req_type = req_type
        self.num_courses_reqd = num_courses_reqd

    def evaluate_req(self):
        counter_chk = 0
        num_courses = len(self.user_courses)
        if num_courses >= self.num_courses_reqd:
            for req_type in self.req_type:
                if req_type == 'COURSES/NUM/MIN':
                    for course in self.user_courses:
                        if course in self.courses_reqd:
                            self.addAppliedCourses(course)
                            counter_chk += 1
                            if counter_chk == self.num_courses_reqd:
                                self.isCompleted = True
                                return

            self.isCompleted = False


def evaluate_regex(number):
    # Cases for number:
    if number == '1':
        pattern = '[1-4]\d{2}'
        return pattern
    elif number == '2':
        pattern = '[2-4]\d{2}'
        return pattern
    elif number == '3':
        pattern = '[3-4]\d{2}'
        return pattern
    elif number == '4':
        pattern = '[4]\d{2}'
        return pattern


class CategoriesBasedRequirement(Requirementalgo):
    num_categories_reqd: int / float
    pre_req_list: list[Requirementalgo]
    categories: list[str]

    def __init__(self, coursesReqd, description, courses_taken, req_type, recurs_req, categories):
        super().__init__(coursesReqd, description, courses_taken, req)
        self.req_type = req_type
        self.num_categories_reqd = num_categories_reqd  # Count key in the json
        self.recurs_req = recurs_req
        self.categories = categories

    def evaluate_req(self):
        # Have a list of all courses ready for filtering

        courses = Course.objects.all()
        if self.req_type == "COURSES_CATEGORIES/FCES/MIN" or self.req_type == "CATEGORIES/FCES/MIN" or \
                self.req_type == "CATEGORIES/FCES/GROUPMIN":
            # Atleast x.0 credits condition
            if self.courses_reqd:
                self.req_type = "COURSES/FCES/MIN"
                CreditBasedRequirement.evaluate_req(self)
                if self.isCompleted:
                    return

            elif self.categories:
                for category in self.categories:
                    if re.match(category, courseCodeRe):
                        # Ex- CSC-300+ So filter courses with course code starting with CSC300 and greater
                        pattern = category.replace('-', "")
                        pattern = pattern.replace("+", "")
                        # Now pattern is CSC300 but I want all courses from 300+ uptill end
                        courses = courses.filter(course_code__startswith=pattern)
                        # Now this is just a creditbased req for courses
                        self.courses_reqd = [course for course in courses]
                        self.req_type = "COURSES/FCES/MIN"
                        CreditBasedRequirement.evaluate_req(self)
                        if self.isCompleted:
                            return
                    if re.match(category, programTitleRe):
                        pass
                    if re.match(category, courseTypeRe):
                        # Ex-LIN-COURSES
                        pattern = category.split('-')[0]
                        courses = courses.filter(course_code__startswith=pattern)
                        self.courses_reqd = [course for course in courses]
                        self.req_type = "COURSES/FCES/MIN"
                        CreditBasedRequirement.evaluate_req(self)
                        if self.isCompleted:
                            return
                    if re.match(category, courseCodePlusRe):
                        # Ex- CSC-300+ So filter courses with course code starting with CSC300 and greater
                        pattern_preffix = category.split('-')[0]
                        pattern_numb = category.split('-')[1][0]
                        reg_eval = evaluate_regex(pattern_numb)
                        final_pattern = fr'{pattern_preffix}({reg_eval})$'
                        # Now pattern is CSC300 but I want all courses from 300+ uptill end
                        courses = courses.filter(course_code__regex=final_pattern)
                        # Now this is just a creditbased req for courses
                        self.courses_reqd = [course for course in courses]
                        self.req_type = "COURSES/FCES/MIN"
                        CreditBasedRequirement.evaluate_req(self)
                        if self.isCompleted:
                            return
                    if re.match(category, numberRe) or re.match(category, numberPlusRe):
                        # Recurs-reqs present
                        if re.match(category, numberPlusRe):
                            pattern_digit = category[0]
                            reg_exp= evaluate_regex(pattern_digit)
                            reg_pattern = fr'{reg_exp}'
                            if self.recurs_req:
                                for requirement in self.recurs_req:
                                    courses_filter = requirement.courses_reqd
                                    final_courses = []
                                    for course in courses_filter:
                                        if re.match(reg_pattern, course.course_code):
                                            final_courses.append(course)
                                    self.courses_reqd = final_courses
                                    self.req_type = "COURSES/FCES/MIN"
                                    CreditBasedRequirement.evaluate_req(self)
                                    if self.isCompleted:
                                        return
                        else:
                            pattern_digit = category[0]
                            reg_pattern=fr'{pattern_digit}\d{2}'
                            if self.recurs_req:
                                for requirement in self.recurs_req:
                                    #Filter courses from each requirement and then adding only apt courses
                                    courses_filter = requirement.courses_reqd
                                    final_courses = []
                                    for course in courses_filter:
                                        if re.match(reg_pattern, course.course_code):
                                            final_courses.append(course)
                                    self.courses_reqd = final_courses
                                    self.req_type = "COURSES/FCES/MIN"
                                    CreditBasedRequirement.evaluate_req(self)
                                    if self.isCompleted:
                                        return
            self.isCompleted = False
            self.applied_course = []
        elif self.req_type == "COURSES_CATEGORIES/NUM/GROUPMIN" or  self.req_type == "COURSES_CATEGORIES/NUM/MIN":
            # Atleast x.0 credits condition
            if self.courses_reqd:
                self.req_type = "COURSES/NUM/MIN"
                CourseBasedRequirement.evaluate_req(self)
                if self.isCompleted:
                    return

            elif self.categories:
                for category in self.categories:
                    if re.match(category, courseCodeRe):
                        # Ex- CSC-300+ So filter courses with course code starting with CSC300 and greater
                        pattern = category.replace('-', "")
                        pattern = pattern.replace("+", "")
                        # Now pattern is CSC300 but I want all courses from 300+ uptill end
                        courses = courses.filter(course_code__startswith=pattern)
                        # Now this is just a creditbased req for courses
                        self.courses_reqd = [course for course in courses]
                        self.req_type = "COURSES/NUM/MIN"
                        CourseBasedRequirement.evaluate_req(self)
                        if self.isCompleted:
                            return
                    if re.match(category, programTitleRe):
                        pass
                    if re.match(category, courseTypeRe):
                        # Ex-LIN-COURSES
                        pattern = category.split('-')[0]
                        courses = courses.filter(course_code__startswith=pattern)
                        self.courses_reqd = [course for course in courses]
                        self.req_type = "COURSES/NUM/MIN"
                        CourseBasedRequirement.evaluate_req(self)
                        if self.isCompleted:
                            return
                    if re.match(category, courseCodePlusRe):
                        # Ex- CSC-300+ So filter courses with course code starting with CSC300 and greater
                        pattern_preffix = category.split('-')[0]
                        pattern_numb = category.split('-')[1][0]
                        reg_eval = evaluate_regex(pattern_numb)
                        final_pattern = fr'{pattern_preffix}({reg_eval})$'
                        # Now pattern is CSC300 but I want all courses from 300+ uptill end
                        courses = courses.filter(course_code__regex=final_pattern)
                        # Now this is just a creditbased req for courses
                        self.courses_reqd = [course for course in courses]
                        self.req_type = "COURSES/NUM/MIN"
                        CourseBasedRequirement.evaluate_req(self)
                        if self.isCompleted:
                            return
                    if re.match(category, numberRe) or re.match(category, numberPlusRe):
                        # Recurs-reqs present
                        if re.match(category, numberPlusRe):
                            pattern_digit = category[0]
                            reg_exp= evaluate_regex(pattern_digit)
                            reg_pattern = fr'{reg_exp}'
                            if self.recurs_req:
                                for requirement in self.recurs_req:
                                    courses_filter =requirement.courses_reqd
                                    final_courses = []
                                    for course in courses_filter:
                                        if re.match(reg_pattern, course.course_code):
                                            final_courses.append(course)
                                    self.courses_reqd = final_courses
                                    self.req_type = "COURSES/NUM/MIN"
                                    CourseBasedRequirement.evaluate_req(self)
                                    if self.isCompleted:
                                        return
                        else:
                            pattern_digit = category[0]
                            reg_pattern=fr'{pattern_digit}\d{2}'
                            if self.recurs_req:
                                for requirement in self.recurs_req:
                                    #Filter courses from each requirement and then adding only apt courses
                                    courses_filter = requirement.courses_reqd
                                    final_courses = []
                                    for course in courses_filter:
                                        if re.match(reg_pattern, course.course_code):
                                            final_courses.append(course)
                                    self.courses_reqd = final_courses
                                    self.req_type = "COURSES/NUM/MIN"
                                    CourseBasedRequirement.evaluate_req(self)
                                    if self.isCompleted:
                                        return
            self.isCompleted = False
            self.applied_course = []
        elif self.req_type=='CATEGORIES/FCES/GROUPMAX' or self.req_type=='CATEGORIES/FCES/MAX':
            # Atmost x.0 credits condition
            if self.courses_reqd:
                self.req_type = "COURSES/FCES/GROUPMAX"
                CreditBasedRequirement.evaluate_req(self)
                if self.isCompleted:
                    return

            elif self.categories:
                for category in self.categories:
                    if re.match(category, courseCodeRe):
                        # Ex- CSC-300+ So filter courses with course code starting with CSC300 and greater
                        pattern = category.replace('-', "")
                        pattern = pattern.replace("+", "")
                        # Now pattern is CSC300 but I want all courses from 300+ uptill end
                        courses = courses.filter(course_code__startswith=pattern)
                        # Now this is just a creditbased req for courses
                        self.courses_reqd = [course for course in courses]
                        self.req_type = "COURSES/FCES/GROUPMAX"
                        CreditBasedRequirement.evaluate_req(self)
                        if self.isCompleted:
                            return
                    if re.match(category, programTitleRe):
                        pass
                    if re.match(category, courseTypeRe):
                        # Ex-LIN-COURSES
                        pattern = category.split('-')[0]
                        courses = courses.filter(course_code__startswith=pattern)
                        self.courses_reqd = [course for course in courses]
                        self.req_type = "COURSES/FCES/GROUPMAX"
                        CreditBasedRequirement.evaluate_req(self)
                        if self.isCompleted:
                            return
                    if re.match(category, courseCodePlusRe):
                        # Ex- CSC-300+ So filter courses with course code starting with CSC300 and greater
                        pattern_preffix = category.split('-')[0]
                        pattern_numb = category.split('-')[1][0]
                        reg_eval = evaluate_regex(pattern_numb)
                        final_pattern = fr'{pattern_preffix}({reg_eval})$'
                        # Now pattern is CSC300 but I want all courses from 300+ uptill end
                        courses = courses.filter(course_code__regex=final_pattern)
                        # Now this is just a creditbased req for courses
                        self.courses_reqd = [course for course in courses]
                        self.req_type = "COURSES/FCES/GROUPMAX"
                        CreditBasedRequirement.evaluate_req(self)
                        if self.isCompleted:
                            return
                    if re.match(category, numberRe) or re.match(category, numberPlusRe):
                        # Recurs-reqs present
                        if re.match(category, numberPlusRe):
                            pattern_digit = category[0]
                            reg_exp= evaluate_regex(pattern_digit)
                            reg_pattern = fr'{reg_exp}'
                            if self.recurs_req:
                                for requirement in self.recurs:
                                    courses_filter =requirement.courses_reqd
                                    final_courses = []
                                    for course in courses_filter:
                                        if re.match(reg_pattern, course.course_code):
                                            final_courses.append(course)
                                    self.courses_reqd = final_courses
                                    self.req_type = "COURSES/FCES/GROUPMAX"
                                    CreditBasedRequirement.evaluate_req(self)
                                    if self.isCompleted:
                                        return
                        else:
                            pattern_digit = category[0]
                            reg_pattern=fr'{pattern_digit}\d{2}'
                            if self.recurs_req:
                                for requirement in self.recurs_req:
                                    #Filter courses from each requirement and then adding only apt courses
                                    courses_filter = requirement.courses_reqd
                                    final_courses = []
                                    for course in courses_filter:
                                        if re.match(reg_pattern, course.course_code):
                                            final_courses.append(course)
                                    self.courses_reqd = final_courses
                                    self.req_type = "COURSES/FCES/GROUPMAX"
                                    CreditBasedRequirement.evaluate_req(self)
                                    if self.isCompleted:
                                        return
            self.isCompleted = False
            self.applied_course = []







