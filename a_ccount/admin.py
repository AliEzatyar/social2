from django.contrib import admin
from django.contrib import admin

# Register your models here.
from a_ccount.models import Profile, Relation


@admin.register(Profile)
class ProfileAdminControl(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'image']
    # raw_id_fields = ['user'] seems like it is not needed!

@admin.register(Relation)
class relationAdmin(admin.ModelAdmin):
    list_display = ['From','To','created','id']
    list_filter = ['From']
