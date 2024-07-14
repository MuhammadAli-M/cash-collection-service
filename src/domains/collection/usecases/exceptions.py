from dataclasses import dataclass

from domains.collection.entities.collector import UserID
from domains.collection.entities.task import CollectorID


@dataclass
class CollectorNotFound(AssertionError):
    user_id: UserID


@dataclass
class FrozenCollector(AssertionError):
    collector_id: CollectorID


@dataclass
class TaskNotFound(AssertionError):
    task_id: int
