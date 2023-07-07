from django.shortcuts import render
from rest_framework import viewsets, status
from .models import UserReview, OnlineReview, Professor
from .serializers import UserReviewSerializer, OnlineReviewSerializer, ProfessorSerializer
from requests import Response
from django.contrib.auth.models import User
from courses.models import Course
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

def createReview(self, request, *args, **kwargs):
    print("Hello")
    if request.METHOD == 'POST':
        # Extract the review data from request
        username = request.data['username']
        course_code = request.data['course_code']
        professor = request.data['professor']
        rating = request.data['rating']
        review = request.data['review']
        if not username or not course or not rating or not review:
            return Response({'Error, invalid arguments'}, status=status.HTTP_400_BAD_REQUEST)
        # Check if the user exists
        user = User.objects.filter(username=username)
        if not user:
            return Response({'Error, user does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        # Check if the course exists
        course = Course.objects.filter(course_code=course_code)
        if not course:
            return Response({'Error, course does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        professor = Professor.objects.filter(name=professor)
        if not professor: 
            UserReview.objects.create(user=user, course=course, rating=rating, review=review) # Don't add professor if it doesn't exist
        else:
            UserReview.objects.create(user=user, course=course, professor=professor, rating=rating, review=review) # Add professor since it exists
        # Update the average rating and number of reviews for the course
        course.updateRating(rating)
        return Response({'Success'}, status=status.HTTP_200_OK)
    else:
        return Response({'Error, invalid request'}, status=status.HTTP_400_BAD_REQUEST)