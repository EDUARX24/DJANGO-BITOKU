from django.apps import AppConfig


class BitokuappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bitokuApp'
    verbose_name = 'Bitoku App'

    def ready(self):
        import bitokuApp.signals
