from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProgramSerializer
from .models import Program, Requirement

# To view programs in the backend
class ProgramView(viewsets.ModelViewSet):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()

# To view requirements in the backend
class RequirementView(viewsets.ModelViewSet):
    serializer_class = ProgramSerializer
    queryset = Requirement.objects.all()



# Create your views here.
