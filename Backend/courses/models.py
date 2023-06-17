from django.db import models
# Create your models here.
# Model for a course. Refers to the course table in the database.
class Course(models.Model):
    course_code = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    credits = models.DecimalField(max_digits=3, decimal_places=1)
    recommended_prep = models.JSONField(default=list)
    SCIENCE = "SCI"
    HUMANITIES = "HUM"
    SOCIAL_SCIENCE = "SSC"
    distrubution = models.CharField(max_length=3, choices=
                                    [(SCIENCE, "Science"), 
                                     (HUMANITIES, "Humanities"), 
                                     (SOCIAL_SCIENCE, "Social Science")]) # Choices for distribution requirements
# Store list of course codes. we store them as a JSONField, which is a list of strings.
    prerequisites = models.JSONField( default=list)
    exclusions = models.JSONField(default=list)

    def __str__(self):
        return self.course_code



    