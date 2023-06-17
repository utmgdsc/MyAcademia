from django.contrib import admin

# Register your models here.

# Register the courses model in the admin page
from .models import Course

admin.site.register(Course)