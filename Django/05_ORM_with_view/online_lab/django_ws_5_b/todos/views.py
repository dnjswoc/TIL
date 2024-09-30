from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    todo_list = Todo.objects.all()
    context = {
        'todo_list': todo_list
    }
    return render(request, 'todos/index.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')

def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    context = {
        'todo': todo
    }
    return render(request, 'todos/detail.html', context)


def new_todo(request):
    new_todo = Todo()
    new_todo.work = request.POST.get('work')
    new_todo.content = request.POST.get('content')
    new_todo.is_completed = False
    new_todo.save()
    return redirect('todos:detail', new_todo.pk)


def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('todos:index')