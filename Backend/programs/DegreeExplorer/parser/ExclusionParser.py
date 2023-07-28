"""
The purpose of this file is to parse the exclusions for each exclusion that
is offered at UTM.
Each exclusion has certain exclusions, which are courses that cannot be taken
with the exclusion in question.

"""
import csv
import re

utmCourseCode = r"[A-Z]{3}\d{3}[HY]5"
utsgCourseCode = r"[A-Z]{3}\d{3}[HY]1"
utscCourseCode = r"[A-Z]{3}\d{2}[A-D]\d{1}[HY]3"
acrossCampus = r"([A-Z]{3}\d{3}[HY]5|[A-Z]{3}\d{3}[HY]1|[A-Z]{3}[A-D]\d{2}[HY]3)"


class ExclusionParser:

    def __init__(self, exclusion, user_courses):
        self.exclusion = exclusion
        self.user_courses = user_courses

    def checkCourseApproval(self):
        if self.noneSyntax():
            return True
        elif self.check_for_structured_prereqs():
            match = re.findall(utmCourseCode, self.exclusion,
                               flags=re.IGNORECASE)
            match += re.findall(utsgCourseCode, self.exclusion,
                                flags=re.IGNORECASE)
            match += re.findall(utscCourseCode, self.exclusion,
                                flags=re.IGNORECASE)
            tempExclusion = self.exclusion[::]
            if len(match) > 0:
                for course in match:
                    if course in self.user_courses:
                        tempExclusion = tempExclusion.replace(course, "True")
                    else:
                        tempExclusion = tempExclusion.replace(course, "False")
            return not eval(tempExclusion)

    def noneSyntax(self):
        if "None" in self.exclusion:
            return True
        return False


    def isValidCouseCode(self, courseCode):
        utmMatches = re.findall(utmCourseCode, courseCode, flags=re.IGNORECASE)
        utsgMatches = re.findall(utsgCourseCode, courseCode, flags=re.IGNORECASE)
        utscMatches = re.findall(utscCourseCode, courseCode, flags=re.IGNORECASE)

        if len(utmMatches) == 0 and len(utsgMatches) == 0 and len(utscMatches) == 0:
            return False
        return True

    def ifCourseExists(self, courseCode):
        if courseCode in self.user_courses:
            return True
        return False

    def check_for_structured_prereqs(self):
        if "and" in self.exclusion and "or" in self.exclusion: #TODO: FIX NEEDED HERE
            list = self.exclusion.split("and")
            for item in list:
                if "or" in item:
                    new_list = item.split("or")
                    list.extend(new_list)
                    list.remove(item)
            for item in list:
                # item = item.strip()
                match = re.findall(acrossCampus, item,
                                   flags=re.IGNORECASE)
                if len(match) == 0:
                    return False
                else:
                    item = item.replace(match[0], "")
                    for i in item:
                        if i.isalpha():
                            return False

            return True
        elif "and" in self.exclusion:
            result = self.exclusion.split("and")
            for item in result:
                # item = item.strip()
                match = re.findall(acrossCampus, item,
                                   flags=re.IGNORECASE)
                if len(match) == 0:
                    return False
                else:
                    item = item.replace(match[0], "")
                    for i in item:
                        if i.isalpha():
                            return False
            return True

        elif "or" in self.exclusion:
            result = self.exclusion.split("or")
            for item in result:
                match = re.findall(acrossCampus, item,
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
            match = re.findall(acrossCampus, self.exclusion,
                               flags=re.IGNORECASE)
            if len(match) == 0:
                return False
            else:
                temp = self.exclusion[::]
                temp = temp.replace(match[0], "")
                for i in temp:
                    if i.isalpha():
                        return False
            return True


def check_all_exclusion():
    f = open("/Users/guninkakar/Desktop/GDSC/myAcademia/MyAcademia/Backend/programs/DegreeExplorer/parser/updatedExclusion.txt", "r")

    while True:
        line = f.readline()
        if not line:
            break
        else:
            line_exclusion = line.split(":")
            exclusion = ExclusionParser(line_exclusion[1], [])

            if not exclusion.noneSyntax():
                if not exclusion.check_for_structured_prereqs():
                    print(f"{line}")
    f.close()

check_all_exclusion()
