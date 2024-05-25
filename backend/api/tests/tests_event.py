from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Event, Location
import json


class EventTest(TestCase):
    fixtures = ['data.json']

    def setUp(self):
        self.password = '123'
        self.username = 'adminTest'
        self.user = User.objects.create_user(username=self.username, password=self.password, is_superuser=True, is_staff=True)
        self.client.login(username=self.username, password=self.password)

    def test_create_event(self):
        request = self.client.post('/api/event/', {
            "name": "Test Event",
            "description": "This is a test event",
            "lan": True,
            "location": 1,
            "date": "2030-05-21",
            "capacity": 100
        }).content.decode('utf-8')
        response = json.loads(request)

        self.assertEqual(response['name'], 'Test Event')
        self.assertEqual(response['description'], 'This is a test event')
        self.assertEqual(response['lan'], True)
        self.assertEqual(response['user'], self.username)
        self.assertEqual(response['location'], 1)
        self.assertEqual(response['date'], '2030-05-21')

    def test_update_event(self):
        event = Event.objects.create(name='Test Event', description='This is a test event', lan=False,
            location_id=1, date='2030-05-21', userId=self.user)

        request = self.client.put(f'/api/event/{event.id}/', {
            "id": event.id,
            "name": "Updated Event",
            "description": "This event has been updated",
            "lan": True,
            "location": 1,
            "date": "2030-05-21",
            "capacity": 100
        }, content_type="application/json").content.decode('utf-8')
        response = json.loads(request)

        self.assertEqual(response['name'], 'Updated Event')
        self.assertEqual(response['description'], 'This event has been updated')
        self.assertEqual(response['lan'], True)
        self.assertEqual(response['user'], self.username)
        self.assertEqual(response['location'], 1)
        self.assertEqual(response['date'], '2030-05-21')


class EventRegistrationTest(TestCase):
    fixtures = ['data.json']

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test_pass')
        self.location = Location.objects.get(pk=1)

        self.event = Event.objects.create(
            name='Test Event',
            description='Test Description',
            lan=True,
            location=self.location,
            date='2030-05-21',
            capacity=100,
            userId=self.user
        )

    def test_event_registration(self):
        self.client.login(username='test', password='test_pass')

        response = self.client.post('/api/eventRegistration/', {
            "event": self.event.id,
            "user": self.user.username
        }).content.decode('utf-8')
        registration = json.loads(response)

        self.assertEqual(registration['event'], self.event.id)
        self.assertEqual(registration['user'], self.user.username)

    def test_event_capacity(self):
        for i in range(5):
            user = User.objects.create_user(username=f'test{i}', password='testpass')
            self.client.login(username=f'test{i}', password='testpass')
            self.client.post('/api/eventRegistration/', {
                "event": self.event.id,
                "user": user.username
            })
            self.client.logout()

        self.assertEqual(self.event.current_capacity, 5)

