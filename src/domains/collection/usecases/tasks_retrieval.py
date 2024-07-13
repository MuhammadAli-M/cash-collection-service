from typing import List

from pydantic import BaseModel

from domains.collection.contracts.tasks_repo import ITasksRepo
from domains.collection.entities.task import Task
from domains.collection.infra.repos.tasks_repo import TasksRepo


class TasksRetrievalRequest(BaseModel):
    user_id: int


class TasksRetrievalResponse(BaseModel):
    tasks: List[Task]


class TasksRetrieval:

    def __init__(self, repo: ITasksRepo = TasksRepo()):
        self.repo = repo

    def execute(self, request: TasksRetrievalRequest) -> TasksRetrievalResponse:
        tasks = self.repo.get_tasks(user_id=request.user_id, is_collected=True)
        return TasksRetrievalResponse(tasks=tasks)
