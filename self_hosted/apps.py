from django.apps import AppConfig


class SelfHostedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'self_hosted'
