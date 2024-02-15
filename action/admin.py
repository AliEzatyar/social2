from django.contrib import admin

# Register your models here.
from action.models import Action
#

@admin.register(Action)
class actionAdmin(admin.ModelAdmin):
    list_display = ['user', 'verb', 'target_model_object', 'created','target_ct']
    list_filter = ['created']
    search_fields = ['verb']