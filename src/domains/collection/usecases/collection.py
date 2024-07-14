from django.db import transaction
from pydantic import BaseModel

from domains.collection.contracts.collectors_repo import ICollectorsRepo
from domains.collection.contracts.tasks_repo import ITasksRepo
from domains.collection.entities.collector import UserID
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
        with transaction.atomic():
            collector = self.get_collector_or_throw(request.user_id)
            self.assert_collector_is_not_frozen_or_throw(collector.id)

            task = self.tasks_repo.get_task(request.task_id)
            if task is None:
                raise TaskNotFound(task_id=request.task_id)


        # TODO finish this use case

    def assert_collector_is_not_frozen_or_throw(self, collector_id):
        status = self.collectors_repo.get_latest_status(
            collector_id=collector_id)
        if status.is_frozen_due():
            raise FrozenCollector(collector_id=collector_id)

    def get_collector_or_throw(self, user_id: UserID):
        collector = self.collectors_repo.get_collector_by_user_id(
            user_id=user_id)

        if collector is None:
            raise CollectorNotFound(user_id=user_id)

        return collector
