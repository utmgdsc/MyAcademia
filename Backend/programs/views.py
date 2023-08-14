from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import ProgramSerializer, RequirementSerializer
from .models import Program, Requirement
from courses.models import Course
from rest_framework.views import APIView
from rest_framework.response import Response

# To view programs in the backend
class ProgramView(viewsets.ModelViewSet):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()

# To view requirements in the backend
class RequirementView(viewsets.ModelViewSet):
    serializer_class = RequirementSerializer
    queryset = Requirement.objects.all()


# View to test the degree explorer
class TestDegreeExplorerView(APIView):
    def get(self, request):
        dict = {}
        test1 = "Hey"
        dict["test1"] = test1
        return Response(dict, status=status.HTTP_200_OK) 




