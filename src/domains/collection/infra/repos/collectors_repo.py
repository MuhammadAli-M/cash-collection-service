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

    def save_collector(self, collector: Collector) -> Collector:
        dbo = self.to_dbo(collector)
        saved_dbo = self.dao.save_collector(dbo)
        return self.to_domain(saved_dbo)

    def get_collector(self, collector_id: int) -> Optional[Collector]:
        dbo = self.dao.get_collector(collector_id=collector_id)
        return self.to_domain(dbo)

    def get_collector_by_user_id(self, user_id: int) -> Optional[Collector]:
        dbo = self.dao.get_collector_by_user_id(user_id=user_id)
        return self.to_domain(dbo)

    def save_status(self, status: Status) -> Status:
        dbo = self.status_converter.to_dbo(status)
        saved_dbo = self.status_dao.save_status(dbo)
        return self.status_converter.to_domain(saved_dbo)


    def get_latest_status(self, collector_id: CollectorID) -> Optional[Status]:
        status_dbo = self.status_dao.get_latest(collector_id=collector_id)
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

    def to_dbo(self, domain: Collector) -> CollectorDbo:
        """
        Convert to dbo entity
        """

        dbo = CollectorDbo(
            amount=domain.amount,
            user_id=domain.user_id,
        )

        if domain.id is not None:
            dbo.id = domain.id
            dbo.created_at = domain.created_at
            dbo.updated_at = domain.updated_at

        return dbo
