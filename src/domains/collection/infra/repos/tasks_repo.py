from typing import List, Optional

from domains.collection.contracts.tasks_repo import ITasksRepo
from domains.collection.entities.task import Task
from domains.collection.infra.models.task import Task as TaskDbo
from domains.collection.infra.repos.tasks_dao import TasksDao


class TasksRepo(ITasksRepo):
    def __init__(self, dao=TasksDao()):
        self.dao = dao

    def save_task(self, domain: Task) -> Task:
        dbo = self.to_dbo(domain)
        return self.dao.save_task(dbo)

    def get_tasks(self, user_id: int, is_collected: bool) -> List[Task]:
        dbos = self.dao.get_tasks(user_id, is_collected)
        return [self.to_domain(dbo) for dbo in dbos]

    def get_task(self, id: int) -> Optional[Task]:
        dbo = self.dao.get_task(id=id)
        return self.to_domain(dbo)

    def to_domain(self, dbo: TaskDbo) -> Optional[Task]:
        """
        Convert to domain entity
        """

        if dbo is None:
            return None

        return Task(
            id=dbo.id,
            amount_due=dbo.amount_due,
            amount_due_at=dbo.amount_due_at,
            customer_id=dbo.customer_id,
            collector_id=dbo.collector_id,
            is_collected=dbo.is_collected,
            created_at=dbo.created_at,
            updated_at=dbo.updated_at,
        )

    def to_dbo(self, domain: Task) -> TaskDbo:
        """
        Convert to dbo(database object)
        """
        return TaskDbo(
            amount_due=domain.amount_due,
            amount_due_at=domain.amount_due_at,
            customer_id=domain.customer_id,
            collector_id=domain.collector_id,
            is_collected=domain.is_collected,
            created_at=domain.created_at,
            updated_at=domain.updated_at,
        )
