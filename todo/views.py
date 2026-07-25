from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.db.models import Q
from .models import Task
from .forms import TaskForm


def home(request):

    query = request.GET.get('q', '')

    if request.method == "POST":

        form = TaskForm(request.POST)

        if form.is_valid():

            task = form.save(commit=False)
            task.time = timezone.localtime().time()
            task.save()

            return redirect('home')

    else:

        form = TaskForm()

    all_tasks = Task.objects.order_by('completed', '-created_at')

    tasks = all_tasks

    if query:
        tasks = tasks.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query)
        )

    total = all_tasks.count()

    completed = all_tasks.filter(completed=True).count()

    pending = total - completed

    progress = 0

    if total > 0:

        progress = int((completed / total) * 100)

    context = {

        'tasks': tasks,

        'form': form,

        'total': total,

        'completed': completed,

        'pending': pending,

        'progress': progress,

        'today': timezone.now(),

        'query': query,

    }

    return render(request, 'index.html', context)


def edit_task(request, task_id):

    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':

        form = TaskForm(request.POST, instance=task)

        if form.is_valid():

            form.save()

            return redirect('home')

    else:

        form = TaskForm(instance=task)

    return render(request, 'edit_task.html', {
        'form': form,
        'task': task,
    })


def delete_task(request, task_id):

    task = get_object_or_404(Task, id=task_id)

    task.delete()

    return redirect('home')


def toggle_task(request, task_id):

    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task.completed = request.POST.get('completed') == 'on'
        task.save()

        completed = Task.objects.filter(completed=True).count()
        total = Task.objects.count()
        pending = total - completed
        progress = int((completed / total) * 100) if total > 0 else 0

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({
                'completed': task.completed,
                'completed_count': completed,
                'pending_count': pending,
                'progress': progress,
            })

    return redirect('home')
