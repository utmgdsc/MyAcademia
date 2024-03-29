from rest_framework import serializers
from .models import Course

# Serializer class for the Course model which will allow it to be converted to json to store in the database
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('course_code', 'title', 'credit', 'recommended_prep', 
                  'distribution', 'pre_req', 'exclusions', 'description', 'program_area', 'avg_rating', 'num_reviews')