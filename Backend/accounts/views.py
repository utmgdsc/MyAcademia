from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import ProfileSerializer, CustomUserCreateSerializer
from .models import Profile
from djoser.views import UserViewSet 
from rest_framework.response import Response
# Create your views here.

class ProfileView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

# This is a custom view for creating a new user. This will tell djoser to use the custom serializer
class CustomUserViewSet(UserViewSet):
    serializer_class = CustomUserCreateSerializer

    # We can modify this so that a User is required to provide a program as well. 
    def create(self, request, *args, **kwargs):
        email = request.data['email']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        if not email or not first_name or not last_name: # If email, first_name or last_name is not provided, return an error
            return Response({'error': 'Email, first_name and last_name are required fields'}, status=status.HTTP_400_BAD_REQUEST)
        # Capitalize the first letter of the first and last name
        first_name = first_name.capitalize()
        last_name = last_name.capitalize()
        # Pass data onto serializer and validate it
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer) # Create a new user

        # Return valid response saying user successfully created
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def me(self, request, *args, **kwargs):
        # Modify this to return the user's information such as email, first_name, last_name, etc.
        user = request.user
        dict = {}
        dict['username'] = user.username
        dict['email'] = user.email
        dict['first_name'] = user.first_name
        dict['last_name'] = user.last_name
        return Response(dict, status=status.HTTP_200_OK)
    