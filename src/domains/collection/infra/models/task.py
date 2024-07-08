from django.db import models
from domains.collection.infra.models.collector import Collector


class Task(models.Model):
    collector = models.ForeignKey(Collector, models.PROTECT, null=True)
    is_collected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
