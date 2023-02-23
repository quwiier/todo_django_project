from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import Task


# Create your views here.

def index(request):
    todos = Task.objects.all()
    return render(request, 'todoapp/index.html', {'todo_list': todos, 'title': 'Главная страница'})


@require_http_methods(['POST'])
def add(request):
    title = request.POST['title']
    todo = Task(title=title)
    todo.save()
    return redirect('index')


def update(request, todo_id):
    todo = Task.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()
    return redirect('index')


def delete(request, todo_id):
    todo = Task.objects.get(id=todo_id)
    todo.delete()
    return redirect('index')
