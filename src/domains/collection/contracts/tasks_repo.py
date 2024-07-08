from abc import ABC, abstractmethod
from typing import List

from domains.collection.entities.task import Task, CollectorID


class ITasksRepo(ABC):

    @abstractmethod
    def save_task(self, domain: Task) -> Task:
        raise NotImplemented()

    @abstractmethod
    def get_tasks(self, collector_id: CollectorID, is_collected: bool) -> List[
        Task]:
        raise NotImplemented()
