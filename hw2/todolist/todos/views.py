from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo

def index(request):
    todos = Todo.objects.all()[:10]
    context = {
        'todos':todos
    }
    return render(request, 'index.html', context)


def details(request, id):
    todos = Todo.objects.get(id=id)
    context = {
        'todos':todos
    }
    print(todos.title, todos.text, todos.created_at)
    return render(request, 'details.html', context)
