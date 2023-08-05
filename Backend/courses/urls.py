from django.contrib import admin
from django.urls import path, include
from .views import CourseSearchView,GetProgramAreaView

urlpatterns = [
    path('courseSearch/', CourseSearchView.as_view(), name='courseSearch'), # custom endpoint for course search. 
    path('getProgramAreas/',GetProgramAreaView.as_view(), name='getProgramAreas'), # custom endpoint for getting program areas.
]