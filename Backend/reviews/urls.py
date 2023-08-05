from django.contrib import admin
from django.urls import path, include
from .views import CreateReviewView, FindProfessorsView, GetOnlineReviewsView, GetUserReviewsView, AllProfessorsView

urlpatterns = [
    path('createUserReview/', CreateReviewView.as_view(), name='createUserReview'), # custom endpoint for creating a new user review
    path('findProfessor/', FindProfessorsView.as_view(), name='findProfessor'), # custom endpoint for filtering professors. 
    path('getOnlineReviews/', GetOnlineReviewsView.as_view(), name='getOnlineReviews'), # custom endpoint for getting online reviews.
    path('getUserReviews/', GetUserReviewsView.as_view(), name='getUserReviews'), # custom endpoint for getting user reviews.
    path('allProfessors/' , AllProfessorsView.as_view(), name='allProfessors') # custom endpoint for getting all professors.
]