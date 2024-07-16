from typing import Optional

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from domains.collection.infra.models.collector import Collector


class CollectorDao:

    def save_collector(self, dbo: Collector) -> Collector:
        dbo.save()
        return dbo

    def get_collector(self, collector_id) -> Optional[Collector]:
        collector_id_filter = Q(id=collector_id)
        return self._get_single_collector(collector_id_filter)

    def get_collector_by_user_id(self, user_id):
        user_id_filter = Q(user_id=user_id)
        return self._get_single_collector(user_id_filter)

    def _get_single_collector(self, collector_id_filter):
        try:
            object = Collector.objects.get(collector_id_filter)
        except ObjectDoesNotExist:
            object = None
        return object
