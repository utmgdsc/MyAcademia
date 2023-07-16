from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandParser
from programs.models import Program, Requirement
from courses.models import Course
import csv
import json

class Command(BaseCommand):
    help = "Load programs from csv and json file. python manage.py load_programs <csv_file> <json_file>"

    def add_arguments(self, parser: CommandParser) -> None:
       parser.add_argument('json_file', type=str, help='Path to json file') # Argument for the path to the json file
    
    def handle(self, *args: Any, **options: Any) -> str :
        Requirement.objects.all().delete()
        Program.objects.all().delete()
        json_file = options['json_file']
        with open(json_file, mode='r') as json_file:
            data = json.load(json_file)
            for program in data:
                program_data = data[program] # Extract program data
                # Create and save program object
                new_program = Program.objects.create(program_code=program)
                new_program.program_title = program_data['title']
                assessments = program_data['detailAssessments']
                for requirement in assessments:
                        # Create and save requirement object
                        new_requirement = Requirement.objects.create()
                        new_requirement.requirement_type = assessments.get(requirement, {}).get('type', '')
                        new_requirement.requirement_description = assessments.get(requirement, {}).get('description', '')
                        new_requirement.count = assessments.get(requirement, {}).get('count', 0)
                        new_requirement.categories = assessments.get(requirement, {}).get('categories', '')
                        Command.extractCourses(self, assessments.get(requirement, {}).get('courses', []), new_requirement)
                        new_requirement.save()
                        new_program.requirements.add(new_requirement)
                new_program.save()

    def extractCourses(self, courses:list, new_requirement: Requirement):
        for course_code in courses:
            try:
                course_code = course_code.strip()
                course = Course.objects.get(course_code=course_code)
                new_requirement.courses.add(course)
            except Course.DoesNotExist:
                print(course_code)
                course = Course.objects.create(course_code=course_code, is_dummy=True)
                new_requirement.courses.add(course)