from django.contrib.auth.models import User
from django.test import TestCase, Client


class UpdateUser(TestCase):
    def setUp(self):
        self.password = '123'
        self.admin = User.objects.create_superuser('admin', '', self.password)
        self.client = Client()

    def test_update_user(self):
        self.client.login(username=self.admin.username, password=self.admin.password)

        response = self.client.put('/api/users/1/', {
            "username": "admin",
            "password": "123",
            "email": "admin@mail.com",
            "is_superuser": True,
            "groups": []
        }, content_type="application/json",)
        self.assertEqual(response.status_code, 200)

