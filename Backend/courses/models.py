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
    distribution = models.CharField(max_length=max(len(SCIENCE), len(HUMANITIES), len(SOCIAL_SCIENCE), len(NONE)),
                                    choices=
                                    [(SCIENCE, "SCI"),
                                     (HUMANITIES, "HUM"),
                                     (SOCIAL_SCIENCE, "SSC"),
                                     (NONE, "N/A")])  # Choices for distribution requirements
    pre_req = models.TextField(default="")
    exclusions = models.TextField(default="")
    description = models.TextField()
    program_area = models.CharField(max_length=200, default="")
    # Store the number of reviews and the average rating for the course. This is based on the reviews provided by the users and updated whenever a new review is added
    num_reviews = models.IntegerField(default=0)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)

    def __str__(self):
        return self.course_code
    
    # Function to update the average rating and number of reviews for the course
    def updateRating(self, rating: int):
        currTotal = self.avg_rating * self.num_reviews
        self.num_reviews += 1
        self.avg_rating = (currTotal + rating) / self.num_reviews
        self.save()
