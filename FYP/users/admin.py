from django.contrib import admin
from .models import Profile


admin.site.site_header = "RideSafely Admin Panel"
admin.site.register(Profile)
