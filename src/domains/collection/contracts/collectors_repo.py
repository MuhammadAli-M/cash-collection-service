from abc import ABC, abstractmethod
from typing import Optional

from domains.collection.entities.status import Status
from domains.collection.entities.task import CollectorID


class ICollectorsRepo(ABC):

    @abstractmethod
    def get_latest_status(
        self, collector_id: CollectorID, is_frozen: bool, is_active: bool
    ) -> Optional[Status]:
        raise NotImplemented()
