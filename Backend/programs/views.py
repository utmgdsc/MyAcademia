from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProgramSerializer, RequirementSerializer
from .models import Program, Requirement
from courses.models import Course

# To view programs in the backend
class ProgramView(viewsets.ModelViewSet):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()

# To view requirements in the backend
class RequirementView(viewsets.ModelViewSet):
    serializer_class = RequirementSerializer
    queryset = Requirement.objects.all()


def getProgramRequirements(Program: Program):
    # Get the requirements for a program
    for req in Program.requirements.all():
        for course in req.courses.all():
            print(course.course_code)

