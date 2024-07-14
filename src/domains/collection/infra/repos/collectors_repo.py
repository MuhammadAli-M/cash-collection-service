from typing import Optional

from domains.collection.contracts.collectors_repo import ICollectorsRepo
from domains.collection.entities.collector import Collector
from domains.collection.entities.status import Status
from domains.collection.entities.task import CollectorID
from domains.collection.infra.models.collector import Collector as CollectorDbo
from domains.collection.infra.repos.collector_dao import CollectorDao
from domains.collection.infra.repos.converters.status import StatusConverter
from domains.collection.infra.repos.status_dao import StatusDao


class CollectorsRepo(ICollectorsRepo):
    def __init__(self, dao=CollectorDao(),
                 status_dao=StatusDao(),
                 status_converter=StatusConverter()):
        self.dao = dao
        self.status_dao = status_dao
        self.status_converter = status_converter

    def get_collector(self, collector_id: int) -> Optional[Collector]:
        dbo = self.dao.get_collector(collector_id=collector_id)
        return self.to_domain(dbo)

    def get_latest_status(
        self, collector_id: CollectorID, is_frozen: bool, is_active: bool
    ) -> Optional[Status]:
        status_dbo = self.status_dao.get_latest(
            collector_id=collector_id, is_frozen=is_frozen, is_active=is_active
        )
        return self.status_converter.to_domain(status_dbo)

    def to_domain(self, dbo: CollectorDbo) -> Optional[Collector]:
        """
        Convert to domain entity
        """

        if dbo is None:
            return None

        return Collector(
            id=dbo.id,
            amount=dbo.amount,
            user_id=dbo.user_id,
            created_at=dbo.created_at,
            updated_at=dbo.updated_at,
        )
