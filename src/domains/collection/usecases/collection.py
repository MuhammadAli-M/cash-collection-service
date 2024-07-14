from pydantic import BaseModel

from domains.collection.contracts.collectors_repo import ICollectorsRepo
from domains.collection.contracts.tasks_repo import ITasksRepo
from domains.collection.infra.repos.tasks_repo import TasksRepo
from domains.collection.usecases.exceptions import CollectorNotFound


class CollectionRequest(BaseModel):
    user_id: int
    task_id: int


class Collection:

    def __init__(self, collectors_repo: ICollectorsRepo,
                 tasks_repo: ITasksRepo = TasksRepo()):
        self.collectors_repo = collectors_repo
        self.tasks_repo = tasks_repo

    def execute(self, request: CollectionRequest):
        collector = self.collectors_repo.get_collector_by_user_id(
            user_id=request.user_id)

        self.assertExistingCollector(collector, request)
        # TODO assert collector is not frozen
        # TODO assert existing

        # TODO finish this use case

    def assertExistingCollector(self, collector, request):
        if collector is None:
            raise CollectorNotFound(user_id=request.user_id)
