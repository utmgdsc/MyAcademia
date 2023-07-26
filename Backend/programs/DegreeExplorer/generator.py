from Courses.course import Course
from programs.models import Program, Requirement
from degreeAPI import Degree


class Generator:
    semester_length: int
    program: Program
    degree: Degree

    def __init__(self, semester_length, program, degree):
        self.semester_length = semester_length
        self.program = Program.objects.get(program_code=program)
        self.degree = degree

    def potential_courses(self, semester):
        pass

    def generate_graph(self):
        pass












