from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandParser
from reviews.models import Professor
import csv

# Created a command to add courses from csv file to database
class Command(BaseCommand):
    help = "Load online reviews from a csv file"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument("csv_file", type=str, help="Path to csv file") # Argument for the path to the csv file
    
    def handle(self, *args: Any, **options: Any) -> None:
        #Professor.objects.all().delete() # Delete all existing professors only for testing purposes
        csv_file = options["csv_file"]
        with open(csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    professor = Professor.objects.get(professor_name=row["professor"], department=row["department"])
                except Professor.DoesNotExist:
                    Professor.objects.create(professor_name=row["professor"], department=row["department"])