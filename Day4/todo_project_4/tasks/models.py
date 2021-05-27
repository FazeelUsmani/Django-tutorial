from functools import total_ordering
from django.db import models
from django.db.models.fields import DateTimeField
from django.utils.translation import TranslatorCommentWarning
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

# Create an rich API for us for free

class Task(models.Model):   # class => table
    content = models.TextField()    # field => column in the table
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(
        default=timezone.now()
    )
    completed_at = models.DateTimeField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)   # got additional table because of many-to-many relation

    class TaskStatus(models.TextChoices): # enumeration
        COMPLETED = "CO", "Completed"
        PENDING = "PE", "Pending"
        DROPPED = "DR", "Dropped"

    status = models.CharField(
        choices = TaskStatus.choices,
        default = TaskStatus.PENDING,
        max_length = 2,
    )   #  must have restricted set of choices

    def __str__(self):
        return f'{self.content} - {self.get_status_display()}'

    # prooperties and descriptor protocol in Python
    @property
    def foo(self):
        return 'hello'
