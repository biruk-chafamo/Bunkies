from django.db.models.signals import post_save, pre_save, m2m_changed
from django.dispatch import receiver
from django.conf import settings

from guardian.shortcuts import assign_perm

from .models import *


@receiver(signal=post_save, sender=Connection)
def assign_connection_perm(sender, instance, created, **kwargs):
    connection = instance
    if created:
        assign_perm('matcher.change_connection', connection.receiver)
        assign_perm('change_connection', connection.receiver, connection)


