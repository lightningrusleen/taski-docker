"""Конфигурация приложения API."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Конфигурация для приложения 'api'."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
