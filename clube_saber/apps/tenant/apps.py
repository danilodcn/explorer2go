from django.apps import AppConfig


class TenantConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clube_saber.apps.tenant'