from django.apps import AppConfig


class CustomersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'customers'
    label = 'customers'

    def ready(self):
        from . import receivers

        from .injector import override
        override()
