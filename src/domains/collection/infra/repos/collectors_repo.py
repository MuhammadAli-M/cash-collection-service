from typing import Optional

from domains.collection.contracts.collectors_repo import ICollectorsRepo
from domains.collection.contracts.tasks_repo import ITasksRepo
from domains.collection.entities.status import Status
from domains.collection.entities.task import CollectorID
from domains.collection.infra.repos.converters.status import StatusConverter
from domains.collection.infra.repos.status_dao import StatusDao


class CollectorsRepo(ICollectorsRepo):
    def __init__(self, status_dao=StatusDao(), status_converter=StatusConverter()):
        self.status_dao = status_dao
        self.status_converter = status_converter

    def get_latest_status(
        self, collector_id: CollectorID, is_frozen: bool, is_active: bool
    ) -> Optional[Status]:
        status_dbo = self.status_dao.get_latest(
            collector_id=collector_id, is_frozen=is_frozen, is_active=is_active
        )
        return self.status_converter.to_domain(status_dbo)
