from typing import List

from domains.collection.contracts.tasks_repo import ITasksRepo
from domains.collection.entities.task import Task, CollectorID
from domains.collection.infra.models.task import Task as TaskDbo
from domains.collection.infra.repos.tasks_dao import TasksDao


class TasksRepo(ITasksRepo):
    def __init__(self, dao=TasksDao()):
        self.dao = dao

    def save_task(self, domain: Task) -> Task:
        dbo = self.to_dbo(domain)
        return self.dao.save_task(dbo)

    def get_tasks(self, collector_id: CollectorID, is_collected: bool) -> List[Task]:
        return self.dao.get_tasks(collector_id, is_collected)

    def to_domain(self, dbo: TaskDbo) -> Task:
        """
        Convert to domain entity
        """
        return Task(
            id=dbo.id,
            collector_id=dbo.collector.id,
            is_collected=dbo.is_collected,
            created_at=dbo.created_at,
            updated_at=dbo.updated_at,
        )

    def to_dbo(self, domain: Task) -> TaskDbo:
        """
        Convert to dbo(database object)
        """
        return TaskDbo(
            collector_id=domain.collector_id,
            is_collected=domain.is_collected,
            created_at=domain.created_at,
            updated_at=domain.updated_at,
        )
