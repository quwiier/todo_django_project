from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'todolist/task.html'


class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    template_name = 'todolist/task_create_form.html'


class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    template_name = 'todolist/task_update_form.html'


class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    template_name = 'todolist/task_delete_form.html'
