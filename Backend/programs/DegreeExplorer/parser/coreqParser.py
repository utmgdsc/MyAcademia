"""
The purpose of this parser to parse the corequisites for each course that
is offered at UTM. Some courses have certain corequisites, which are courses
that must be taken to take the course.
"""

import re

utmCourseCode = r"[A-Z]{3}\d{3}[HY]5"


class CoreqParser:
    def __init__(self, coreq, user_courses):
        self.coreq = coreq
        self.user_courses = user_courses


    """
    This function evaluates the co-requisites for a course. It checks if the
    user has taken the co-requisites for the course. If the user has taken the
    co-requisites, then the user is eligible to take the course.
    
    :return: True if the user is eligible to take the course, False otherwise
    """
    def evaluate_coreq(self):
        pass

    def check_none_requirements (self):
        if "None" in self.coreq:
            return True
        return False

    def check_for_structured_prereq(self):
        if "and" in self.coreq and "or" in self.coreq:
            list = self.coreq.split("and")
            for item in list:
                if "or" in item:
                    new_list = item.split("or")
                    list.extend(new_list)
                    list.remove(item)
            for item in list:
                match = re.findall(utmCourseCode, item,
                                   flags=re.IGNORECASE)
                if len(match) == 0:
                    return False
                else:
                    item = item.replace(match[0], "")
                    for i in item:
                        if i.isalpha():
                            return False

            return True
        elif "and" in self.coreq:
            result = self.coreq.split("and")
            for item in result:
                match = re.findall(utmCourseCode, item,
                                   flags=re.IGNORECASE)
                if len(match) == 0:
                    return False
                else:
                    item = item.replace(match[0], "")
                    for i in item:
                        if i.isalpha():
                            return False
            return True

        elif "or" in self.coreq:
            result = self.coreq.split("or")
            for item in result:
                match = re.findall(utmCourseCode, item,
                                   flags=re.IGNORECASE)
                if len(match) == 0:
                    return False
                else:
                    item = item.replace(match[0], "")
                    for i in item:
                        if i.isalpha():
                            return False
            return True
        else:
            match = re.findall(utmCourseCode, self.coreq,
                               flags=re.IGNORECASE)
            if len(match) == 0:
                return False
            else:
                self.coreq = self.coreq.replace(match[0], "")
                for i in self.coreq:
                    if i.isalpha():
                        return False
            return True
