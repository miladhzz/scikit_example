from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import User


class StandarizeViewTestCase(APITestCase):
    url = reverse('standarize')

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpass')
        self.token = AccessToken.for_user(self.user)

    def test_standarize_view_with_valid_data(self):
        # valid request data
        data = {
            "sensor_1": [1.0, 2.0, 3.0],
            "sensor_2": [4.0, 5.0, 6.0],
            "sensor_3": [7.0, 8.0, 9.0]
        }

        # set the authentication header with the JWT token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('result', response.data)

    def test_standarize_view_with_invalid_data(self):
        # invalid request data
        data = {
            "sensor_1": [1.0, 2.0, "3.0"],
            "sensor_2": [4.0, 5.0],
            "sensor_3": [7.0, 8.0, 9.0]
        }

        # set the authentication header with the JWT token
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('errors', response.data)
