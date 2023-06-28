from rest_framework import serializers
from .models import Profile
from djoser.serializers import UserCreateSerializer

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['program', 'user']

# This is a custom serializer for creating a new user. It is used in the djoser endpoint. Have modified it so that
# email, first_name and last_name are required fields
class CustomUserCreateSerializer(UserCreateSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    class Meta(UserCreateSerializer.Meta):
        fields = ['email', 'username', 'password', 'first_name', 'last_name']