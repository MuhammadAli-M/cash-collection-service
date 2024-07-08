from domains.collection.infra.models.task import Task

class TaskDao:
    def save_task(self, task: Task) -> Task:
        task.save()
        return task
