from django.contrib.auth import get_user_model
from django.test import TestCase
from ninja_extra import status
from ninja_jwt.tokens import AccessToken

from tasks.enums import TaskStatus
from tasks.models import Task

User = get_user_model()


class TaskTest(TestCase):
    base_url = '/api/tasks/'

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='user_1',
            password='123456789'
        )

        cls.task = Task.objects.create(
            title='task_1',
            description='description_1',
            user=cls.user,
        )

        cls.access_token = AccessToken.for_user(cls.user)
        cls.headers = {'Authorization': f'Bearer {cls.access_token}'}

        cls.task_data = {
            'title': 'task_2',
            'description': 'description_2',
        }

        cls.task_update_data = {
            'title': 'task_2',
            'description': 'description_2',
            'status': TaskStatus.active,
        }

    async def test_list_tasks(self):
        response = await self.async_client.get(self.base_url, headers=self.headers)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task_count = await Task.objects.acount()
        self.assertEqual(len(response.json()), task_count)

    async def test_get_task(self):
        response = await self.async_client.get(f'{self.base_url}{self.task.id}', headers=self.headers)
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data.get('id'), self.task.id)
        self.assertEqual(response_data.get('title'), self.task.title)

    async def test_create_task(self):
        response = await self.async_client.post(
            self.base_url,
            data=self.task_data,
            content_type='application/json',
            headers=self.headers,
        )
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task_count = await Task.objects.acount()
        self.assertEqual(2, task_count)
        self.assertEqual(response_data.get('title'), self.task_data.get('title'))
        self.assertEqual(response_data.get('status'), TaskStatus.created)
        self.assertEqual(response_data.get('user'), self.user.id)

    async def test_update_task(self):
        response = await self.async_client.put(
            f'{self.base_url}{self.task.id}',
            data=self.task_update_data,
            content_type='application/json',
            headers=self.headers,
        )
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data.get('id'), self.task.id)
        self.assertEqual(response_data.get('status'), self.task_update_data.get('status'))
