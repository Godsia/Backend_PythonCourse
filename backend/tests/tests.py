from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Item

class ItemAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')

    def test_create_item(self):
        response = self.client.post('/api/items/', {'name': 'Test Item', 'description': 'Test Description'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)