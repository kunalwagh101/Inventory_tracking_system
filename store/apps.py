"""
    Module name :- apps
"""

from django.apps import AppConfig


class StoreConfig(AppConfig):
    """
    App config file.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "store"
