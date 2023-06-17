from django.contrib import admin
from .models import UserReviews, OnlineReviews, Professor
# Register your models here.
admin.site.register(UserReviews)
admin.site.register(OnlineReviews)
admin.site.register(Professor)