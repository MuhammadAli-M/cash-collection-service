from typing import Optional

from django.core.exceptions import ObjectDoesNotExist

from domains.collection.infra.models.collector import Collector


class CollectorDao:
    def get_collector(self, collector_id) -> Optional[Collector]:
        try:
            object = Collector.objects.get(id=collector_id)
        except ObjectDoesNotExist:
            object = None
        return object
