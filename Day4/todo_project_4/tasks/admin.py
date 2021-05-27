from datetime import time
from django.contrib import admin
from . import models
from django.utils import timezone
# Register your models here.

def mark_complete(model_admin, request, queryset):
    queryset.update(
        status = models.Task.TaskStatus.COMPLETED,
        completed_at = timezone.now(),
        )
mark_complete.short_description = 'Mark these tasks as complete'

def mark_pending(model_admin, request, queryset):
    queryset.update(
        status=models.Task.TaskStatus.PENDING,
        completed_at = None
    )

mark_pending.short_description = 'Mark these tasks as pending'

class TaskAdmin(admin.ModelAdmin):
    fields = ['content',    # on one row
                'status',    # covers full row
                 ('deadline', 'tags')   # deadline and tags on one row
            ]

    # this allows me to render addl. properties
    list_display = [ 'content', 'status', 'foo']  
    list_editable = ['status']
    actions = [mark_complete, mark_pending]
    list_filter = ['status', 'deadline', 'tags']
    search_fields = ['content', 'tags__name']
    ordering = ['deadline', 'status']

    def get_ordering(self, request):
        if request.user.is_superuser:
            return ['status']
        else:
            return ['deadline']

admin.site.register(models.Task, TaskAdmin)
admin.site.register(models.Tag)