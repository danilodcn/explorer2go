from django.apps import AppConfig


class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clube_saber.apps.product'
    verbose_name = 'Produto'
    verbose_name_plural = 'Produtos'
