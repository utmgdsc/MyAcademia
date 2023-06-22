from rest_framework import serializers
from .models import UserReview, OnlineReview, Professor

#Serailizer for the UserReview model
class UserReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserReview
        fields = ('review_id', 'review', 'course', 'rating', 'userName', 'Professor')

# Serializer for the OnlineReview model
class OnlineReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineReview
        fields = ('review_id', 'review', 'course', 'senitment_analysis_value')

# Serializer for the Professor model
class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ('professor_name', 'department', 'prof_id')
