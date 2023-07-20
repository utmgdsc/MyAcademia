from django.db import models
from courses.models import Course
# Create your models here.

# Requirement model
class Requirement(models.Model):
    requirement_id = models.AutoField(primary_key=True)
    requirement_type = models.CharField(max_length=100, default="None")
    requirement_description = models.CharField(max_length=100, blank=True)
    count = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    courses = models.ManyToManyField(Course, blank=True)
    categories = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'Requirement-{self.requirement_id}'

# Program model
class Program(models.Model):
    program_code = models.CharField(max_length=10, primary_key=True, default="00000")
    program_title = models.CharField(max_length=100)
    requirements = models.ManyToManyField(Requirement, blank=True)
    
    def __str__(self):
        return self.program_code + " " + self.program_title
    