from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
# Create your views here.

def index(request):
    all_tasks = Todo.objects.all()
    context = {"all_tasks":all_tasks}
    return render(request, "todo/index.html", context)

def add(request):
    if request.method == "POST":
        title = request.POST["title"]
        task = Todo.objects.create(title=title)
    else:
        return redirect("todo:index")
    return redirect("todo:index")

def complete(request, todo_id):
    if request.method == "POST":
        task = get_object_or_404(Todo, pk=todo_id)
        task.completed = True
        task.save()
    else:
        return redirect("todo:index")
    return redirect("todo:index")

def delete(request, todo_id):
    if request.method == 'POST':
        task = get_object_or_404(Todo, pk=todo_id)
        task.delete()
    else:
        return redirect("todo:index")
    return redirect("todo:index")