from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from images.models import Image


@admin.register(Image)
class image_admin_panel(ModelAdmin):
    list_display = ['user', 'title', 'created', 'image']
    list_filter = ['created']
