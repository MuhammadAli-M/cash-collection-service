from typing import List

from domains.collection.infra.models.task import Task


class TasksDao:
    def save_task(self, task: Task) -> Task:
        task.save()
        return task

    def get_tasks(self, user_id: int, is_collected: bool) -> List[Task]:
        qs = Task.objects.filter(collector__user_id=user_id,
                                 is_collected=is_collected)
        return list(qs)
