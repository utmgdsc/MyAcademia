from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandParser
from reviews.models import OnlineReview
from courses.models import Course
import csv

# Created a command to add courses from csv file to database
class Command(BaseCommand):
    help = "Load online reviews from a csv file"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("csv_file", type=str, help="Path to csv file") # Argument for the path to the csv file
    
    def handle(self, *args: Any, **options: Any) -> str :
        OnlineReview.objects.all().delete() # Delete all the reviews in the database. Just for testing
        csv_file = options["csv_file"]
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                course = Course.objects.get(course_code=row['course_code'].strip()) # Get the course object from the database
                if course is None: # If course does not exist, skip
                    continue
                for i in range(1,11): # 10 reviews
                    if row[str(i)] == '': # Indicates end of reviews so break
                        break
                    OnlineReview.objects.create(course=course, review=row[f'{i}']) # Create a new review object and store in database