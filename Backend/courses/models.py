from django.db import models
# Create your models here.
# Model for a course. Refers to the course table in the database.
class Course(models.Model):
    course_code = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=200)
    credit = models.DecimalField(max_digits=3, decimal_places=1)
    recommended_prep = models.TextField(default="")
    SCIENCE = "Science"
    HUMANITIES = "Humanities"
    SOCIAL_SCIENCE = "Social Science"
    NONE = "None"
    distrubution = models.CharField(max_length= max(len(SCIENCE), len(HUMANITIES), len(SOCIAL_SCIENCE), len(NONE)),choices=
                                    [(SCIENCE, "SCI"), 
                                     (HUMANITIES, "HUM"), 
                                     (SOCIAL_SCIENCE, "SSC"),
                                     (NONE, "N/A")]) # Choices for distribution requirements
    pre_req = models.TextField(default="")
    exclusions = models.TextField(default="")
    description = models.TextField()
    def __str__(self):
        return self.course_code



    