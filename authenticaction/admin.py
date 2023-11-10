from django.contrib import admin

# Register your models here.
from authenticaction.models import CustomUser

admin.site.register(CustomUser)