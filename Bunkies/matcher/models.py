from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.utils import timezone
import datetime

from rest_framework import serializers
# from guardian.shortcuts import assign_perm


class User(AbstractUser):
    connections = models.ManyToManyField("self", through='Connection', blank=True, related_name='connections')
    suggested_roommates = models.ManyToManyField(
        "self", through='Suggestion', blank=True, related_name='suggested_roommates'
    )
    preference = models.OneToOneField(to='Preference', null=True, on_delete=models.CASCADE)


class Preference(models.Model):
    city = models.CharField(max_length=100)
    # pass
    # # location = models.
    # # TODO set default preferences
    # # TODO: django-location-field


class Suggestion(models.Model):
    suggested_user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='suggested_user')
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    compatibility = models.FloatField()


class Connection(models.Model):
    receiver = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='friend')  # user.connections
    sender = models.ForeignKey(to=User, on_delete=models.CASCADE)  # connections.user
    date_joined = models.DateTimeField(default=timezone.now)
    is_pending = models.BooleanField(default=True)
    is_accepted = models.BooleanField(default=False)

    class ConnectionType(models.TextChoices):
        ROOMMATE = 'Roommate'
        FRIEND = 'Friend'

    connection_type = models.CharField(
        max_length=8,
        choices=ConnectionType.choices,
        default=ConnectionType.FRIEND,
    )

    class Meta:
        ordering = ['-date_joined']

    def save(self, *args, **kwargs):
        # if any change is made after the initial save, the connection is no longer pending because the only change
        # that can be made is to the is_accepted field
        if self.is_pending and self.is_accepted:
            self.is_pending = False
        super().save(*args, **kwargs)


