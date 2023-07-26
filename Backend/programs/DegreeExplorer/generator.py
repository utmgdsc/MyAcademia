from Courses.course import Course
from programs.models import Program, Requirement

class Generator:
    user_courses: List[Course]
    semester_length: int
    program: Program

    def __init__(self,user_courses,semester_length, program):
        self.user_courses = user_courses
        self.semester_length = semester_length
        self.program = Program.objects.get(program_code=program)


    def potential_courses(self, semester):
        potential_courses = []
        for course in Course.objects.all():



