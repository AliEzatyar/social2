from django.apps import AppConfig


class a_ccountConfig(AppConfig):
    name = 'a_ccount'
    default_auto_field = 'django.db.models.BigAutoField'
    def ready(self):
        import a_ccount.signals # import signal modul