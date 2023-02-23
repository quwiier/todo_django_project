from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods

from .models import ToDo


# Create your views here.

def index(request):
    todos = ToDo.objects.all()
    return render(request, 'todoapp/index.html', {'todo_list': todos, 'title': 'Главная страница'})
