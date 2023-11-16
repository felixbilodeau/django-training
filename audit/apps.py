from django.apps import AppConfig


class AuditConfig(AppConfig):
    name = 'audit'
    label = 'audit'

    def ready(self):
        from . import receivers
