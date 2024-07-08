from django.db import models

from domains.collection.infra.models.collector import Collector
from domains.collection.infra.models.customer import Customer


class Task(models.Model):
    amount_due = models.IntegerField()
    amount_due_at = models.DateTimeField()
    customer = models.ForeignKey(Customer, models.RESTRICT)
    collector = models.ForeignKey(Collector, models.PROTECT, null=True)
    is_collected = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


