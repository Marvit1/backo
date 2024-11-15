from django.apps import AppConfig

class MainConfig(AppConfig):
    name = 'main'
    verbose_name = 'Հոդվածններ'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        # Import the signals module to ensure the signal handlers are registered
        import main.signals
