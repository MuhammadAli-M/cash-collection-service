from django.db import transaction
from pydantic import BaseModel

from domains.collection.contracts.collectors_repo import ICollectorsRepo
from domains.collection.contracts.tasks_repo import ITasksRepo
from domains.collection.entities.collector import UserID
from domains.collection.entities.status import Status
from domains.collection.infra.repos.tasks_repo import TasksRepo
from domains.collection.usecases.exceptions import CollectorNotFound, \
    FrozenCollector, TaskNotFound


class CollectionRequest(BaseModel):
    user_id: int
    task_id: int


class Collection:

    def __init__(self, collectors_repo: ICollectorsRepo,
                 tasks_repo: ITasksRepo = TasksRepo()):
        self.collectors_repo = collectors_repo
        self.tasks_repo = tasks_repo

    def execute(self, request: CollectionRequest):
        with (transaction.atomic()):
            collector = self.get_collector_or_throw(request.user_id)

            status = self.collectors_repo.get_latest_status(collector.id)
            self.assert_not_frozen_status_or_throw(collector, status)

            task = self.get_task_or_throw(request)

            task.set_collected()
            collector.increment_amount(task.amount_due)

            if self.should_freeze_collector(collector, status):
                new_status = Status.make_future_freeze_status(collector.id)
                self.collectors_repo.save_status(new_status)
            self.collectors_repo.save_collector(collector)
            self.tasks_repo.save_task(task)

        # TODO Assign the next task

    def get_collector_or_throw(self, user_id: UserID):
        collector = self.collectors_repo.get_collector_by_user_id(
            user_id=user_id)

        if collector is None:
            raise CollectorNotFound(user_id=user_id)

        return collector

    @staticmethod
    def assert_not_frozen_status_or_throw(collector, status):
        if status.is_frozen_due():
            raise FrozenCollector(collector_id=collector.id)

    def get_task_or_throw(self, request):
        task = self.tasks_repo.get_task(request.task_id)
        if task is None:
            raise TaskNotFound(task_id=request.task_id)
        return task

    @staticmethod
    def should_freeze_collector(collector, status):
        return collector.does_amount_above_freeze_limit() and status.is_freeze_safe()
