from abc import ABC, abstractmethod
from typing import Optional

from domains.collection.entities.collector import Collector
from domains.collection.entities.status import Status
from domains.collection.entities.task import CollectorID


class ICollectorsRepo(ABC):

    @abstractmethod
    def get_collector(self, collector_id: int) -> Optional[Collector]:
        raise NotImplemented()

    @abstractmethod
    def get_collector_by_user_id(self, user_id: int) -> Optional[Collector]:
        raise NotImplemented()

    @abstractmethod
    def get_latest_status(self, collector_id: CollectorID) -> Optional[Status]:
        raise NotImplemented()
