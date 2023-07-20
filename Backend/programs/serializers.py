from rest_framework import serializers
from .models import Program, Requirement

# Serailzer for the Program model
class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = ('program_code', 'program_title', 'requirements')
    
# Serializer for the Requirement model
class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ('requirement_id', 'requirement_type', 'requirement_description', 'count', 'courses')
