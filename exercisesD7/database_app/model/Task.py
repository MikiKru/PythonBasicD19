class Task:
    def __init__(self,
                 name,
                 description,
                 status,
                 date_stop,
                 user_id,
                 task_id = 0,
                 date_start = ""
                 ):
        self.name = name
        self.description = description
        self.status = status
        self.date_stop = date_stop
        self.date_start = date_start
        self.user_id = user_id
        self.task_id = task_id
    def __str__(self):
        return "| %2d | %20s | %20s | %20s | %20s | %20s | %2d |"% \
               (self.task_id, self.name, self.description, self.status,
              self.date_start, self.date_stop, self.user_id)