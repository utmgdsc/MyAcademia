from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandParser
from reviews.models import UserReview
from courses.models import Course
import csv

# Created a command to add courses from csv file to database
class Command(BaseCommand):
    help = "Reset user reviews stored in database and set average rating of all courses back to 0"

    def handle(self, *args: Any, **options: Any) -> None:
        UserReview.objects.all().delete() # Delete all user reviews
        courses = Course.objects.all()
        for course in courses: # Reset average rating of all courses to 0
            course.avg_rating = 0 
            course.save()