from django.db import models
from courses.models import Course
from django.contrib.auth.models import User
# Create your models here.

#Model for Professor
class Professor(models.Model):
    professor_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100) # Update to include a list of departments
    prof_id = models.AutoField(primary_key=True) # Autofield which automatically creates a unique id for the professor
    
    def __str__(self):
        return self.professor_name
# Superclass for Reviews model
class AbstractReview(models.Model):
    review_id = models.AutoField(primary_key=True) # Autofield which automatically creates a unique id
    review = models.TextField(max_length=2500) # Text field for the review
    course = models.ForeignKey(Course, on_delete=models.CASCADE) # Foreign key to the course model. on_delete = models.CASCADE since if the course is deleted, the review is deleted
    def __str__(self):
        return self.course.course_code + "-" + str(self.review_id)
    
    class Meta:
        abstract = True

#UserReviews model which inherits from AbstractReview
class UserReview(AbstractReview):
    rating = models.DecimalField(max_digits=2, decimal_places=1) 
    userName = models.ForeignKey(User, blank=True, on_delete=models.RESTRICT) # Foreign key to the user model. on_delete = models.RESTRICT since if the user is deleted, the review is not deleted
    Professor = models.ForeignKey(Professor, blank=True, on_delete=models.RESTRICT) # Foreign key to the professor model. on_delete = models.RESTRICT since if the professor is deleted, the review is not deleted

#OnlineReviews model which inherits from AbstractReview
class OnlineReview(AbstractReview):
    sentiment_analysis_value = models.DecimalField(max_digits=10, decimal_places=10, default=0.0) # Sentiment analysis value for the review

