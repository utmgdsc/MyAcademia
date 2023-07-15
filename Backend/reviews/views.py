from django.shortcuts import render
from rest_framework import viewsets, status
from .models import UserReview, OnlineReview, Professor
from .serializers import UserReviewSerializer, OnlineReviewSerializer, ProfessorSerializer
from django.contrib.auth.models import User
from courses.models import Course
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
# To view User Reviews in the backend
class UserReviewView(viewsets.ModelViewSet):
    serializer_class = UserReviewSerializer
    queryset = UserReview.objects.all()

# To view Online Reviews in the backend
class OnlineReviewView(viewsets.ModelViewSet):
    serializer_class = OnlineReviewSerializer
    queryset = OnlineReview.objects.all()

# To view Professors in the backend
class ProfessorView(viewsets.ModelViewSet):
    serializer_class = ProfessorSerializer
    queryset = Professor.objects.all()

# Create your views here.

# Class that handles the creation of a new user review
class CreateReviewView(APIView):
    permission_classes = [permissions.IsAuthenticated] # Only authenticated users can access this endpoint
    #permission_classes = [permissions.AllowAny] # Allow any user to access this endpoint. Only for testing
    http_method_names = ['post']
    # A post method to handle the request and create a new user review
    def post(self, request, *args, **kwargs):
            # Extract the review data from request
        username = request.data['username']
        course_code = request.data['course_code']
        professor_name = request.data['professor_name']
        department = request.data['department']
        rating = request.data['rating']
        review = request.data['review']
        if not username or not course_code or not rating or not review or not professor_name or not department:
            return Response({'Error, invalid arguments'}, status=status.HTTP_400_BAD_REQUEST)
        # Check if the user exists and add if not AnonymousUser
        userReview = UserReview()
        user = User.objects.get(username=username)
        if not user and username != 'AnonymousUser':
            return Response({'Error, user does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        if username != 'AnonymousUser':
            userReview.userName = user
        # Check if the course exists
        course = Course.objects.get(course_code=course_code)
        if not course:
            return Response({'Error, course does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        userReview.course = course
        # Check if the professor exists
        professor = Professor.objects.filter(professor_name=professor_name).filter(department=department)
        if len(professor) != 0:
            userReview.Professor = professor[0] # We may need to change this later. Currently it uniquely identifies a professor based on name and department.
            userReview.Professor.add_course(course)  
        if len(professor) == 0 and professor_name != 'NoProfessor':
            return Response({'Error, professor does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        # Add rating and review. Store the review in the database
        userReview.rating = rating
        userReview.review = review
        userReview.save()
        # Update the average rating and number of reviews for the course
        course.updateRating(rating)
        return Response({'Success'}, status=status.HTTP_201_CREATED)

# Class that handles the finding of a professor for a course
class FindProfessorsView(APIView):
    permission_classes = [permissions.AllowAny] 
    http_method_names = ['get']
    # A get method to handle the request and find a professor for a course. 
    def get(self, request, *args, **kwargs):
        course_code = request.GET.get('course_code')
        if not course_code:
            return Response({'Error, invalid arguments'}, status=status.HTTP_400_BAD_REQUEST)
        # Check if the course exists
        try:
            course = Course.objects.get(course_code=course_code)
        except Course.DoesNotExist:
            return Response({'Error, course does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        # Get the professor for the course
        professors_names = Professor.objects.filter(previous_courses__in=[course]).values_list('professor_name', flat=True)
        return Response(professors_names, status=status.HTTP_200_OK)


# Get online reviews for a course
class GetOnlineReviewsView(APIView):
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']
    # A get method to return the online reviews for a course
    def get(self, request, *args, **kwargs):
        course_code = request.GET.get('course_code')
        if not course_code:
            return Response({'Error, invalid arguments'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            course = Course.objects.get(course_code=course_code)
        except Course.DoesNotExist:
            return Response({'Error, course does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        online_reviews = OnlineReview.objects.filter(course=course)
        serializer = OnlineReviewSerializer(online_reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Get user reviews for a course
class GetUserReviewsView(APIView):
    permission_classes = [permissions.AllowAny]
    http_method_names = ['get']
    # A get method to return the user reviews for a course
    def get(self, request, *args, **kwargs):
        course_code = request.GET.get('course_code')
        if not course_code:
            return Response({'Error, invalid arguments'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            course = Course.objects.get(course_code=course_code)
        except Course.DoesNotExist:
            return Response({'Error, course does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        user_reviews = UserReview.objects.filter(course=course)
        serializer = UserReviewSerializer(user_reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
