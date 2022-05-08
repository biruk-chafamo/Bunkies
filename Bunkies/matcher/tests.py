import json

from django.urls import reverse
from django.test.client import RequestFactory
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .serializers import *
from .models import *


class RegistrationTestCase(APITestCase):

    def test_registration(self):
        url = '/users/'
        data = {
            'username': 'test_user', 'email': 'test@gamil.com',
            'first_name': 'test_first_name', 'last_name': 'test_last_name',
            'password': 'test_password', 'password2': 'test_password'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_registration_fail(self):
        url = '/users/'
        data = {
            'username': 'test_user', 'email': 'test@gamil.com',
            'first_name': 'test_first_name', 'last_name': 'test_last_name',
            'password': 'test_password', 'password2': 'test_incorrect_password'
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ConnectionTestCase(APITestCase):
    connection_list_url = reverse('connection-list')

    def setUp(self):
        self.users = {}
        self.user_urls = {}
        for idx in range(3):
            user = User.objects.create_user(
                username=f'test_user_{idx}', email=f'test_{idx}@gamil.com',
                first_name=f'test_first_name_{idx}', last_name=f'test_last_name_{idx}',
                password=f'test_password_{idx}'
            )
            self.users[idx] = user
            self.user_urls[idx] = Util.get_test_object_url('User', user)

        self.client.login(username='test_user_0', password='test_password_0')

    def tearDown(self):
        User.objects.all().delete()
        Connection.objects.all().delete()

    def test_create_connection_authenticated(self):
        data = {'receiver': self.user_urls[1], 'connection_type': 'Roommate'}
        response = self.client.post(self.connection_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_connection_unauthenticated(self):
        self.client.logout()
        data = {'receiver': self.user_urls[1], 'connection_type': 'Roommate'}
        response = self.client.post(self.connection_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_connection_to_self(self):
        data = {'receiver': self.user_urls[0], 'connection_type': 'Roommate'}
        response = self.client.post(self.connection_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_duplicate_existing_pending_connection(self):
        data = {'receiver': self.user_urls[1], 'connection_type': 'Roommate'}
        # print(data)
        response = self.client.post(self.connection_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # duplicate connection request
        response_2 = self.client.post(self.connection_list_url, data)

        err_msg = json.loads(response_2.content)['receiver'][0]
        self.assertEqual(err_msg, f'connection to {self.users[1].username} is already requested.')
        self.assertEqual(response_2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_duplicate_existing_accepted_connection(self):
        data = {'receiver': self.user_urls[1], 'connection_type': 'Roommate'}
        response = self.client.post(self.connection_list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # logging in user_1 to accept connection request from user_0
        self.client.login(username='test_user_1', password='test_password_1')
        response.data.update({'is_accepted': True, 'is_pending': False})
        connection_detail_url = response.data['url']
        self.client.put(connection_detail_url, response.data)  # accepting connection request

        # logging in user_0 to duplicate connection request
        self.client.login(username='test_user_0', password='test_password_0')
        response_2 = self.client.post(self.connection_list_url, data)

        err_msg = json.loads(response_2.content)['receiver'][0]
        self.assertEqual(err_msg, f'{self.users[1].username} is already your connection.')
        self.assertEqual(response_2.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_list_of_sent_connections(self):
    #     data = {'receiver': self.user_urls[1], 'connection_type': 'Roommate'}
    #     response = self.client.post(self.connection_list_url, data)


class Util:
    @staticmethod
    def get_test_object_url(model_name: str, instance):
        model_name = model_name.lower()
        return 'http://testserver' + reverse(f'{model_name}-detail', kwargs={'pk': instance.pk})
