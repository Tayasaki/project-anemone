import json

from django.contrib.auth.models import User
from django.test import TestCase


class LocationSearch(TestCase):
    fixtures = ['data.json']

    def test_name_search(self):
        request = self.client.get("/api/location/", {"name": "Bern"}).content.decode('utf-8')
        request = json.loads(request)

        self.assertEqual(request[0].get("name"), "Bern")

    def test_zip_search(self):
        request = self.client.get("/api/location/", {"zip": "3000"}).content.decode('utf-8')
        request = json.loads(request)

        self.assertEqual(request[0].get("name"), "Bern")

    def test_contains_search(self):
        request = self.client.get("/api/location/", {"zip": "3"}).content.decode('utf-8')
        request = json.loads(request)

        self.assertEqual(len(request), 4)


class LocationComments(TestCase):
    fixtures = ['data.json']

    def test_post(self):
        password = '123'
        username = 'adminTest'
        self.user = User.objects.create_user(username=username, password=password, is_superuser=True, is_staff=True)
        self.client.login(username=username, password=password)

        request = self.client.post('/api/locationComment/', {
            "comment": "Test",
            "location": 1
        }).content.decode('utf-8')
        request = json.loads(request)

        self.assertEqual(request['comment'], 'Test')

    def test_put(self):
        self.test_post()

        request = self.client.put('/api/locationComment/1/', {
            "id": 1,
            "comment": "Test2",
            "location": 1
        },
            content_type="application/json"
        ).content.decode('utf-8')
        request = json.loads(request)

        self.assertEqual(request['comment'], 'Test2')

    def test_delete(self):
        self.test_post()

        request = self.client.delete('/api/locationComment/1/')

        self.assertEqual(request.status_code, 204)


class LocationRating(TestCase):
    fixtures = ['data.json']

    def test_post(self):
        password = '123'
        username = 'adminTest'
        self.user = User.objects.create_user(username=username, password=password, is_superuser=True, is_staff=True)
        self.client.login(username=username, password=password)

        request = self.client.post('/api/locationRating/', {
            "rating": '5.0',
            "location": 1
        }).content.decode('utf-8')
        request = json.loads(request)

        self.assertEqual(request['rating'], '5.0')

    def test_put(self):
        self.test_post()

        request = self.client.put('/api/locationRating/1/', {
            "id": 1,
            "rating": '1.0',
            "location": 1
        },
            content_type="application/json"
        ).content.decode('utf-8')
        request = json.loads(request)

        self.assertEqual(request['rating'], '1.0')
