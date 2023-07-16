"""
The class keeps track of the prerequisites of each course that is
offered at UTM. It also keeps track of the courses that the user has
taken and evaluates if the user is eligible to take a course.
"""

import re

utmCourseCode = r"[A-Z]{3}\d{3}[HY]5"


class PrereqParser:
    def __init__(self, prereq, user_courses):
        self.prereq = prereq
        self.user_courses = user_courses

    def evaluatePrereq(self):
        pass

    def check_for_none_requirement(self):
        """
        This method checks if the course has no requirement

        :return: True if the course has no requirement, False otherwise
        """
        if "None" in self.prereq or self.prereq.strip() == "":
            return True
        return False

    def check_for_garde12_req(self):
        """
        This method checks if the course has a grade 12 requirement

        :return: True if the course has a grade 12 requirement, False otherwise
        """
        if "grade 12".upper() in self.prereq.upper():
            return True
        else:
            return False

    def check_for_no_course_code_req(self):
        """
        This method checks if the no course code is present in the prerequisite.

        :return: True if no course code is present in the prerequisite, False otherwise
        """
        if self.check_for_none_requirement():
            return False
        matches = re.findall(utmCourseCode, self.prereq,
                             flags=re.IGNORECASE)
        if len(matches) == 0:
            return True
        return False

    def check_for_credits_in_prereq(self):
        """
        This method checks if the course has the word credit in the prerequisite

        :return: True if the course prerequisites has the word credit it, False otherwise
        """
        if "credit" in self.prereq.lower():
            return True
        return False

    def check_for_credits(self):
        if self.check_for_credits_in_prereq() and not self.check_for_course_code():
            if not self.check_for_none_requirement() and not self.check_for_garde12_req():
                extracted_details = self.extract_details()
                # todo: check of some more details
                return extracted_details

    def extract_details(self):
        credits = -1
        course_code = -1
        level = -1

        # Extract number of credits
        if "credits" in self.prereq:
            credits_start = self.prereq.find(" credits")
            if credits_start != -1:
                credits_str = self.prereq[:credits_start]
                try:
                    credits = float(credits_str)
                except ValueError:
                    pass
        elif "credit" in self.prereq:
            credits_start = self.prereq.find(" credit")
            if credits_start != -1:
                credits_str = self.prereq[:credits_start]
                try:
                    credits = float(credits_str)
                except ValueError:
                    pass

        # Extract course code
        course_code_start = self.prereq.find(" in ")
        if course_code_start != -1:
            pattern = r"[A-Z]{3}"
            match = re.findall(pattern, self.prereq)
            course_code = match[0]

        # Extract level
        if "level" in self.prereq:
            if "100" in self.prereq:
                level = 100
            elif "200" in self.prereq:
                level = 200
            elif "300" in self.prereq:
                level = 300
            elif "400" in self.prereq:
                level = 400

        return [credits, course_code, level]

    def check_for_course_code(self):
        """
        This method checks if the course has a course code in the prerequisite

        :return: True if the course has a course code in the prerequisite, False otherwise
        """
        match = re.findall(utmCourseCode, self.prereq,
                           flags=re.IGNORECASE)
        if len(match) == 0:
            return False
        return True

    def check_for_structured_prereq(self):
        """
        This method checks if the course has structured prerequisites

        :return: True if the course has structured prerequisites, False otherwise
        """
        if "and" in self.prereq and "or" in self.prereq:
            list = self.prereq.split("and")
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
        elif "and" in self.prereq:
            result = self.prereq.split("and")
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

        elif "or" in self.prereq:
            result = self.prereq.split("or")
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
            match = re.findall(utmCourseCode, self.prereq,
                               flags=re.IGNORECASE)
            if len(match) == 0:
                return False
            else:
                self.prereq = self.prereq.replace(match[0], "")
                for i in self.prereq:
                    if i.isalpha():
                        return False
            return True

# f = open("/Users/guninkakar/Desktop/GDSC/myAcademia/MyAcademia/parser/pre_req_out/creditsUpdated.txt", "r")
#
# while True:
#     line = f.readline()
#     if not line:
#         break
#     line = line.strip().split(":")
#     prereq = line[1]
#     course_code = line[0]
#     parser = PrereqParser(prereq, [])
#     result = parser.check_for_credits()
#     print(prereq,":",result)
