from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseForbidden
from .models import Task
from .forms import TaskForm


class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.resolved:
            return HttpResponseForbidden('Cannot edit a resolved task.')
        return super().dispatch(request, *args, **kwargs)


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')


def toggle_resolved(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.resolved = not task.resolved
    task.save()
    return redirect('task-list')
