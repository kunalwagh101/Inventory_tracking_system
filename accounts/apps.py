"""
    Module name :- apps
"""

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    App configuration.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"
