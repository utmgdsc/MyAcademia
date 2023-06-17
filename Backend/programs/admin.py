from django.contrib import admin

# Register your models here.

from .models import Program, Requirement
admin.site.register(Program)
admin.site.register(Requirement)