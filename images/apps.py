from django.apps import AppConfig
from django.core.signals import setting_changed
from .signalls import receiverr
class ImageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'images'

    def ready(self):
        print("sssssssssssssssssssssssss")

        setting_changed.connect(receiverr,weak=False)
