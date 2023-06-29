from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandParser
from courses.models import Course
import csv

# Created a command to add courses from csv file to database
class Command(BaseCommand):
    help = "Load courses from csv file"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("csv_file", type=str, help="Path to csv file") # Argument for the path to the csv file
    
    def handle(self, *args: Any, **options: Any) -> str :
        # Course.objects.all().delete() # Delete all courses in database. This is for testing purposes
        csv_file = options["csv_file"]
        with open(csv_file, mode='r') as csv_file:
            reader = csv.DictReader(csv_file) # Gets it as a dictionary and uses the first row as the keys
            for row in reader:
                if(row['course_code'] == '' or Course.objects.filter(course_code=row['course_code']).exists()): # If empty or course already exists
                    continue
                # Create and save course object
                Course.objects.create(course_code=row['course_code'], title=row['title'], credit=row['credit'], recommended_prep=row['recommended_prep'], distrubution=row['distribution'], 
                                      pre_req=row['pre_req'], exclusions=row['exclusions'], description=row['description'], program_area=row['program_area'])