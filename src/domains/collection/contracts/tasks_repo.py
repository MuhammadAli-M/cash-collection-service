from abc import ABC, abstractmethod

from domains.collection.entities.task import Task


class ITasksRepo(ABC):

    @abstractmethod
    def save_task(self, domain: Task) -> Task:
        raise NotImplemented()
