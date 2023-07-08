from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import CourseSerializer
from .models import Course
from django.http import request, JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.core import serializers
# To view courses in the backend
class CourseView(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

# Create your views here.


# A class to handle the course search functionality
class CourseSearchView(APIView):
    permission_classes = [permissions.AllowAny] # Allow any user to access this endpoint
    http_method_names = ['post']

    # A post method to handle the request and return the courses
    def post(self, request):
        # Extract information from the request
        course_code = request.data.get('course_code')
        pre_req = request.data.get('pre_req')
        distribution = request.data.get('distribution')
        program_area = request.data.get('program_area')
        # Change to empty string if none is provided
        if pre_req == None:
            pre_req = ""
        if distribution == None:
            distribution = ""
        if program_area == None:
            program_area = ""

        # Filter courses based on the criteria provided. Return only course code and title
        courses = self.filterCourses(course_code, pre_req, distribution, program_area)
        data = courses.values('course_code', 'title')
        return Response(data, status=status.HTTP_200_OK)

    def filterCourses(self, course_code, pre_req, distribution, program_area):
        if course_code:
            if not course_code.endswith("H5"):
                course_code += "H5"  # Add H5 to the end of the course code if it is not already there
            return Course.objects.filter(course_code=course_code)
        # Filter courses based on the criteria provided. If empty string is provided for an attribute, don't filter
        courses = Course.objects.all()
        searched = False # Boolean that tells us whether we have narrowed the queryset or not
        if pre_req != "":
            courses = courses.filter(pre_req__icontains=pre_req)
            searched = True
        if distribution != "":
            courses = courses.filter(distribution=distribution)
            searched = True
        if program_area != "":
            courses = courses.filter(program_area=program_area)
            searched = True
        
        # If we have narrowed the queryset, return the courses. Else, return an empty queryset
        if searched:
            return courses
        else:
            return Course.objects.none() 




    
    