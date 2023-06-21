from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CourseSerializer
from .models import Course

# To view courses in the backend
class CourseView(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

# Create your views here.

