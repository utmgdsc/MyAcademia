from typing import List
from Backend.courses.models import Course


class Degree:
    minCR: bool
    min200LR: bool
    min300LR: bool
    humRequirement: bool
    sscRequirement: bool
    sciRequirement: bool
    user_courses: List[Course]

    def __init__(self):
        self.minNumCR = False
        self.min200LR = False
        self.min300LR = False
        self.humRequirement = False
        self.sscRequirement = False
        self.sciRequirement = False
        self.user_courses = []

    def addCourse(self, course):
        self.user_courses.append(course)

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
