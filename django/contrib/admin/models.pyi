from django.db import models
from typing import Any

class LogEntryManager(models.Manager):

    def log_action(self, user_id:int, content_type_id:int, object_id:int,
                         object_repr:str, action_flag:str, change_message:str) -> None:
        pass

class LogEntry(models.Model):
    objects = LogEntryManager()

ADDITION:str
CHANGE:str
DELETION:str
