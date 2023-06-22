from django.contrib import admin
from .models import UserReview, OnlineReview, Professor
# Register your models here.
admin.site.register(UserReview)
admin.site.register(OnlineReview)
admin.site.register(Professor)