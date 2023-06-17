from django.db import models

# Create your models here.

class Requirement(models.Model):
    requirement_id = models.AutoField(primary_key=True)
    requirement = models.TextField(max_length=2500)
    def __str__(self):
        return self.requirement
    program_id = models.ForeignKey('Program', on_delete=models.CASCADE) 

class Program(models.Model):
    program_id = models.AutoField(primary_key=True)
    program_name = models.CharField(max_length=100)
    SPECIALIST = "SPE"
    MAJOR = "MAJ"
    MINOR = "MIN"
    program_type = models.CharField(max_length=100, choices=[(SPECIALIST, "Specialist"), (MAJOR, "Major"), (MINOR, "Minor")]) # 3 choices for program type