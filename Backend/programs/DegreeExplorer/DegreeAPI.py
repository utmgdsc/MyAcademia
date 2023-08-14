from typing import List

from courses.models import Course

"""
This class keeps track of essential information about the user's degree and
will be used to assist the user in planning their degree.
"""


class Degree:
    minCR: bool
    min200LR: bool
    min300LR: bool
    humRequirement: bool
    sscRequirement: bool
    sciRequirement: bool
    user_courses: List[Course]
    credits: float
    minCRCourses: List[Course]
    min200LRCourses: List[Course]
    min300LRCourses: List[Course]
    humRequirementCourses: List[Course]
    sscRequirementCourses: List[Course]
    sciRequirementCourses: List[Course]

    def __init__(self):
        self.minNumCR = False
        self.minNumCRCourses = []
        self.min200LR = False
        self.min200LRCourses = []
        self.min300LR = False
        self.min300LRCourses = []
        self.humRequirement = False
        self.humRequirementCourses = []
        self.sscRequirement = False
        self.sscRequirementCourses = []
        self.sciRequirement = False
        self.sciRequirementCourses = []
        self.user_courses = []
        self.credits = 0

    def addCourse(self, course) -> None:
        self.user_courses.append(course) # adds course to user's list of courses

        # adds course to the appropriate list of courses as per the requirements
        self.credits += course.credit
        self.minNumCRCourses.append(course)
        if course.course_code[3] == "2":
            self.min200LRCourses.append(course)
            self.min300LRCourses.append(course)
        if course.course_code[3] == "3":
            self.min300LRCourses.append(course)

        if course.distribution == "Humanities":
            self.humRequirementCourses.append(course)
        if course.distribution == "Social Science":
            self.sscRequirementCourses.append(course)
        if course.distribution == "Science":
            self.sciRequirementCourses.append(course)
        self.evaluate_requirements()

    def removeCourse(self, course) -> None:
        """
        This function removes a course from the user's list of courses.
        """
        self.user_courses.remove(course)
        self.credits -= course.credit
        self.minNumCRCourses.remove(course)
        if course.course_code[3] == "2":
            self.min200LRCourses.remove(course)
            self.min300LRCourses.remove(course)
        if course.course_code[3] == "3":
            self.min300LRCourses.remove(course)

        if course.distribution == "Humanities":
            self.humRequirementCourses.remove(course)
        if course.distribution == "Social Science":
            self.sscRequirementCourses.remove(course)
        if course.distribution == "Science":
            self.sciRequirementCourses.remove(course)

        self.evaluate_requirements()

    def evaluate_requirements(self):

        if self.credits >= 20:
            self.minCR = True
        if self.countCredits(self.min200LRCourses) >= 13.0:
            self.min200LR = True
        if self.countCredits(self.min300LRCourses) >= 1.0:
            self.min300LR = True
        if self.countCredits(self.humRequirementCourses) >= 1.0:
            self.humRequirement = True
        if self.countCredits(self.sscRequirementCourses) >= 1.0:
            self.sscRequirement = True
        if self.countCredits(self.sciRequirementCourses) >= 1.0:
            self.sciRequirement = True

    def getIncompleteRequirements(self):
        """
        This function returns a list of requirements that are not met by the
        user's courses.

        :return: List of requirements that are not met by the user's courses.
        """
        incompleteRequirements = []
        if not self.minCR:
            incompleteRequirements.append("minCR")
        if not self.min200LR:
            incompleteRequirements.append("min200LR")
        if not self.min300LR:
            incompleteRequirements.append("min300LR")
        if not self.humRequirement:
            incompleteRequirements.append("humRequirement")
        if not self.sscRequirement:
            incompleteRequirements.append("sscRequirement")
        if not self.sciRequirement:
            incompleteRequirements.append("sciRequirement")
        return incompleteRequirements

    def getCoursesString(self) -> List[str]:
        """
        This function returns a string of the user's courses.

        :return: List of String consisting of all the courses.
        """
        courses = []
        for c in self.user_courses:
            courses.append(c.course_code)
        return courses

    def countCredits(self, courses) -> float:
        count = 0
        for c in courses:
            count += c.credit
        return count


class BBADegree(Degree):
    def __init__(self):
        super().__init__()


class HBscDegree(Degree):
    def __init__(self):
        super().__init__()


class BcomDegree(Degree):
    def __init__(self):
        super().__init__()


class HBADegree(Degree):
    def __init__(self):
        super().__init__()
