from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title)
        return redirect('task_list')
    tasks = Task.objects.order_by('-created_at')
    return render(request, 'task_list.html', {'tasks': tasks})


def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.done = not task.done
    task.save()
    return redirect('task_list')


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')
