from django.test import TestCase
from ninja_extra import status


class TaskNegativeTest(TestCase):
    base_url = '/api/tasks/'

    async def test_list_tasks(self):
        response = await self.async_client.get(self.base_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    async def test_get_task(self):
        response = await self.async_client.get(f'{self.base_url}1')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    async def test_create_task(self):
        response = await self.async_client.post(
            self.base_url,
            data={},
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    async def test_update_task(self):
        response = await self.async_client.put(
            f'{self.base_url}1',
            data={},
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    async def test_delete_task(self):
        response = await self.async_client.delete(f'{self.base_url}1')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
