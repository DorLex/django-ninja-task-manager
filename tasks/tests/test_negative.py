from django.contrib.auth import get_user_model
from django.test import TestCase
from ninja_extra import status
from ninja_jwt.tokens import AccessToken

from tasks.models import Task

User = get_user_model()


class TaskNegativeTest(TestCase):
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

        cls.task_incorrect_update_data = {
            'title': 'task_2',
            'description': 'description_2',
            'status': 'incorrect_status',
        }

    async def test_unauthorized_list_tasks(self):
        response = await self.async_client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    async def test_unauthorized_get_task(self):
        response = await self.async_client.get(f'{self.base_url}1')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    async def test_unauthorized_create_task(self):
        response = await self.async_client.post(
            self.base_url,
            data={},
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    async def test_unauthorized_update_task(self):
        response = await self.async_client.put(
            f'{self.base_url}1',
            data={},
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    async def test_incorrect_status_update_task(self):
        response = await self.async_client.put(
            f'{self.base_url}{self.task.id}',
            data=self.task_incorrect_update_data,
            content_type='application/json',
            headers=self.headers,
        )
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)

    async def test_unauthorized_delete_task(self):
        response = await self.async_client.delete(f'{self.base_url}1')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
