from .models import Table, User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class TestApi(APITestCase):
    def setUp(self):
        Table.objects.create(name='test')
        Table.objects.create(name='test1')
        User.objects.create_user(name="test", surname="test", login='test_12', email="pos123t@mail.com",
                                 password="testtesteat")

    def test_Table(self):
        data = {"name": "test"}
        response = self.client.post("/tables/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_table(self):
        response = self.client.get('/tables/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user(self):
        data = {
            "name": "post",
            "surname": "post",
            "login": "post",
            "email": "post@mail.com",
            "password": "testtesttesttest",
            "phone": 700701011

        }
        response = self.client.post("/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)

    def test_token(self):
        response = self.client.get("/login/test_12/testtesteat")
        self.assertEqual(response.status_code,status.HTTP_200_OK)
