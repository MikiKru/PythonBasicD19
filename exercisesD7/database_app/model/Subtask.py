class Subtask:
    def __init__(self, detail_description, deadline, status, task_id, subtask_id = 0):
        self.detail_description = detail_description
        self.deadline = deadline
        self.status = status
        self.task_id = task_id
        self.subtask_id = subtask_id
    def __str__(self):
        return "| %2d | %20s | %20s | %20s | %2d |" % \
               (self.subtask_id, self.detail_description, self.deadline, self.status, self.task_id)