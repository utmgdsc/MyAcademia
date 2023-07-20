from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandParser
from reviews.models import OnlineReview
from courses.models import Course
from reviews.sentimentAnalysisAPI import sentimentAnalysisAPI
import csv

# Created a command to add courses from csv file to database
class Command(BaseCommand):
    help = "Load online reviews from a csv file"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("folder", type=str, help="Path to folder") # Argument for the path to the csv file

        parser.add_argument("filename", type=str, help="Name of file")
    
    def handle(self, *args: Any, **options: Any) -> str :
        folder = options["folder"]
        filename = options["filename"]
        full_path = f'{folder}/{filename}.csv'

        with open(full_path, mode="w") as csv_file:
            csv_file.write("Course_code, Review, SAV\n")
            all_reviews = OnlineReview.objects.all()
            for review in all_reviews:
                without_commana = review.review.replace(",", "").replace("\n", "") # Incase the review has a comma in it or a newline
                csv_file.write(f'{review.course.course_code}, "{without_commana}", {review.sentiment_analysis_value}\n')
        