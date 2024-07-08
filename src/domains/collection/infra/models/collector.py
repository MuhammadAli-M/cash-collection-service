from django.db import models
from domains.collection.infra.models.user import User


class Collector(models.Model):
    amount = models.IntegerField(blank=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    is_frozen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
