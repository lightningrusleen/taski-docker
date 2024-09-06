"""
Модуль тестов для API задач.

Содержит тесты для проверки доступности списка задач и создания задач.
"""

from http import HTTPStatus

from django.test import Client, TestCase

from . import models


class TaskiAPITestCase(TestCase):
    """
    Тестовый класс для проверки API задач.

    Содержит тесты для методов API, списка задач и создание новой задачи.
    """

    def setUp(self):
        """
        Настраивает тестовый клиент для использования в тестах.

        Создает экземпляр клиента  для отправки запросов в тестах.
        """
        self.guest_client = Client()

    def test_list_exists(self):
        """
        Проверяет доступность списка задач через API.

        Отправляет GET-запрос что статус ответа равен 200 (OK).
        """
        response = self.guest_client.get('/api/tasks/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_task_creation(self):
        """
        Проверяет создание задачи через API.

        Отправляет POST-запрос что статус ответа равен 201 (Created).
        Также проверяет, что задача была успешно добавлена в базу данных.
        """
        data = {'title': 'Test', 'description': 'Test'}
        response = self.guest_client.post('/api/tasks/', data=data)
        self.assertEqual(response.status_code, HTTPStatus.CREATED)
        self.assertTrue(models.Task.objects.filter(title='Test').exists())
