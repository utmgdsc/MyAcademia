from rest_framework import serializers
from .models import UserReview, OnlineReview, Professor

#Serailizer for the UserReview model
class UserReviewSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField() # Serializer method field to get the username and return Anonymous if username is None
    Professor = serializers.SerializerMethodField() # Serializer method field to get the professor name and return No Professor if professor is None
    class Meta:
        model = UserReview
        fields = ('review_id', 'review', 'course', 'rating', 'username', 'Professor')
    
    def get_username(self, obj):
        if obj.username is None:
            return 'Anonymous'
        return obj.username.username
    def get_Professor(self, obj):
        if obj.Professor is None:
            return 'No Professor'
        return obj.Professor.professor_name

# Serializer for the OnlineReview model
class OnlineReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineReview
        fields = ('review_id', 'review', 'course', 'sentiment_analysis_value')

# Serializer for the Professor model
class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('professor_name', 'department', 'prof_id', 'previous_courses')
