"""Модели для приложения API."""

from django.db import models


class Task(models.Model):
    """
    Модель задачи (Taski).

    Содержит заголовок, описание и флаг завершения задачи.
    """

    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        """Возвращает строковое представление задачи (title)."""
        return self.title
