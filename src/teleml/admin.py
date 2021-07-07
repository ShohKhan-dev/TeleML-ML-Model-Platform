from django.contrib import admin

# Register your models here.

from .models import Category, TeleModel, UserProfile


admin.site.register(Category)
admin.site.register(TeleModel)
admin.site.register(UserProfile)