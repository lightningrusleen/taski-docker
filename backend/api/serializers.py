"""Файл сериализаторов."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Task.

    Используется для преобразования данных модели Task в формат JSON
    и обратно.
    """

    class Meta:
        """Класс Meta для определения мета-информации о сериализаторе."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
