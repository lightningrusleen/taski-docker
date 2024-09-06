"""Файл вьюсетов."""

from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Task
from .serializers import TaskSerializer


class TaskView(viewsets.ModelViewSet):
    """
    ViewSet для работы с задачами (Task).

    Предоставляет методы для создания, обновления, удаления и получения задач.
    """

    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def destroy(self, *args, **kwargs):
        """
        Удаляет задачу и возвращает данные удаленной задачи.

        с HTTP-статусом 200 (OK).

        Метод вызывает сериализатор для получения данных удаленной задачи и
        возвращает их в ответе.
        """
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)
