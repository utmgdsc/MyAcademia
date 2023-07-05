from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import CourseSerializer
from .models import Course
from django.http import request, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# To view courses in the backend
class CourseView(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

# Create your views here.

# Extracts information from the request and returns course objects which match the criteria
def courseSearch(request : request):
    if request.METHOD == 'POST':
        course_code = request.data['course_code']
        pre_req = request.data['pre_req']
        distribution = request.data['distribution']
        program_area = request.data['program_area']
        courses = filterCourses(course_code, pre_req, distribution, program_area)
        return JsonResponse(courses, safe=False, status = status.HTTP_200_OK) # Return the courses as a JSON object which can be parsed by the frontend and displayed
    return Response("Invalid request", status=status.HTTP_400_BAD_REQUEST)

def filterCourses(course_code: str, pre_req: str, distribution:str, program_area: str) -> Course.objects:
    if course_code != None or course_code != "": # Course code provided so return course with the course code
        return Course.objects.filter(course_code = course_code)
    # Filter courses based on the criteria provided. Program area is not implemented yet
    return Course.objects.all().filter(pre_req__icontains = pre_req).filter(distribution = distribution)
#.filter(program_area = program_area)
    
    