from django.db import models


# Create your models here.
# Model for a course. Refers to the course table in the database.
class Course(models.Model):
    course_code = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=200)
    credit = models.DecimalField(max_digits=3, decimal_places=1, default=0.5)
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
    avg_rating = models.FloatField(default=0.0)
    # Below are private fields which will be used by the degree explorer algorithm. These may be in a different format from the above fields which will be easier to 
    # parse for the algorithm. These fields are not meant to be accessed by the user. 
    pre_req_algo = models.TextField(default="") 
    exclusions_algo = models.TextField(default="")
    is_dummy = models.BooleanField(default=False) # Indicates whether the course is a dummy course. Dummy courses are used to represent a course that is not in the database but is required for program and degre evaluation.



    def __str__(self):
        if self.course_code is not None:
            return self.course_code
        return "Issues exist here"
    # Function to update the average rating and number of reviews for the course
    def updateRating(self, rating: int):
        rating = int(rating)
        currTotal = self.avg_rating * self.num_reviews
        self.num_reviews += 1
        self.avg_rating = (currTotal + rating) / self.num_reviews
        self.save()
