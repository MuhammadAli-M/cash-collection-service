from django.db import models

from domains.collection.infra.models.collector import Collector
from domains.collection.infra.models.user import User


class Status(models.Model):
    collector = models.ForeignKey(Collector, models.CASCADE)
    due_at = models.DateTimeField()
    is_frozen = models.BooleanField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
