from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'resolved', 'created_at')
    list_filter = ('resolved',)
    search_fields = ('title', 'description')
