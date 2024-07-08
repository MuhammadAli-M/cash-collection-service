from typing import List

from domains.collection.infra.models.task import Task


class TaskDao:
    def save_task(self, task: Task) -> Task:
        task.save()
        return task

    def get_tasks(self, collector_id: int, is_collected: bool) -> List[Task]:
        return Task.objects.filter(collector_id=collector_id,
                                   is_collected=is_collected)
