from django.shortcuts import render, redirect
from task.models import Task
from datetime import date

# Create your views here.


def show_tasks(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks
    }
    return render(request, 'tasks/show_tasks.html', context)


def new_task(request):
    if (request.method == "POST"):
        task = Task()
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.category = request.POST['category']
        task.date_expiration = request.POST['date_expiration']
        task.save()
        return redirect('/')
    else:
        return render(request, 'tasks/new_task.html')


def edit_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    if (request.method == "POST"):
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.category = request.POST['category']
        task.date_expiration = request.POST['date_expiration']
        task.save()
        return redirect('/')
    else:
        return render(request, 'tasks/edit_task.html', {'task': task})


def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    if (request.method == "POST"):
        task.delete()
        return redirect('/')
    else:
        return render(request, 'tasks/delete_task.html', {'task': task})


def pendding_task(resquest):
    tasks = Task.objects.filter(date_expiration__lte=date.today())
    context = {
        'tasks': tasks
    }
    return render(resquest, 'tasks/pendding_tasks.html', context)
