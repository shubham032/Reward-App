from django.apps import AppConfig


class AppManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_manager'

    def ready(self):
        import app_manager.signals
