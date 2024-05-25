from django.contrib.auth.models import User
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=50, null=False)
    zip = models.CharField(max_length=10, null=False)

    @property
    def rating(self):
        ratings = LocationRating.objects.filter(location_id=self.pk)

        count = len(ratings)
        if count == 0:
            return "0"

        rating_sum = 0
        for rating in ratings:
            rating_sum += rating.rating

        avg = round(rating_sum / count, 1)
        return str(avg)

    def __str__(self):
        return self.name


class LocationComment(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=False, related_name="locationComments")
    comment = models.CharField(max_length=200, null=False)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    @property
    def user(self):
        return self.userId.username

    def __str__(self):
        return self.user + " " + self.location.name + " id:" + str(self.pk)


class LocationRating(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=False)
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=0, null=False)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    @property
    def user(self):
        return self.userId.username

    def __str__(self):
        return self.user + " " + self.location.name


class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    lan = models.BooleanField(default=False)
    location = models.ForeignKey(Location, on_delete=models.SET("Location not found"))
    date = models.DateField()
    capacity = models.IntegerField(default=0)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    @property
    def current_capacity(self):
        return len(EventRegistration.objects.filter(event_id=self.pk))

    @property
    def user(self):
        return self.userId.username

    def __str__(self):
        return self.name


class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=False)
    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

    @property
    def user(self):
        return self.userId.username

    def __str__(self):
        return self.event.name + " " + self.user
