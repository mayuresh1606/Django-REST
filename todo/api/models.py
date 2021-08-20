from django.db import models


class Task(models.Model):
    task = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)
