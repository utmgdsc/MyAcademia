from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    program = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.user.username
    

# Creates a new user_profile when a new user is created
def create_profile(sender, instance, created , **kwargs):
    if created: 
        Profile.objects.create(user=instance) 

post_save.connect(create_profile, sender=User) # A signal to invoke create_profile function when a new user is created