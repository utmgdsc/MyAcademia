"""
URL configuration for Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from courses.views import CourseView, CourseSearchView
from programs.views import ProgramView, RequirementView
from reviews.views import UserReviewView, OnlineReviewView, ProfessorView, CreateReviewView, FindProfessorsView
from accounts.views import ProfileView, CustomUserViewSet

# A router object created so that the views can be registered and accessed from the backend
router = routers.DefaultRouter()
router.register(r'courses', CourseView, 'course')
router.register(r'programs', ProgramView, 'program')
router.register(r'requirements', RequirementView, 'requirement')
router.register(r'userreviews', UserReviewView, 'userreview')
router.register(r'onlinereviews', OnlineReviewView, 'onlinereview')
router.register(r'professors', ProfessorView, 'professor')
router.register(r'profiles', ProfileView, 'profile')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # Register the router object. So now, specific objects can be accessed via api/name_of_object
    # /api/name_of_object
    path(r'auth/', include('djoser.urls')), # This is backend endpoints for authentication provided by djoser
    path(r'auth/', include('djoser.urls.jwt')), # Javascript Web Token authentication provided by djoser
    path('auth/users', CustomUserViewSet.as_view({'post': 'create'}), name='user_create'), # custom endpoint for creating a new user
    path('api/createUserReview/', CreateReviewView.as_view(), name='createUserReview'), # custom endpoint for creating a new user review
    path('api/courseSearch/', CourseSearchView.as_view(), name='courseSearch'), # custom endpoint for course search Returns a JSONResponse which can be parsed by the frontend
    path('api/findProfessor/', FindProfessorsView.as_view(), name='findProfessor') # custom endpoint for filtering professors. Returns a JSONResponse which can be parsed by the frontend
]
