from django.shortcuts import render
from django.contrib import messages
from responsibility.models import responsibility


def responsibilityview(request):
    responsibilites = responsibility.objects.all()

    tasks_list = []

    for resp in responsibilites:
        tasks = [getattr(resp, f'task{i}') for i in range(1, 21) if getattr(resp, f'task{i}')]
        tasks_list.append({'name': resp, 'tasks': tasks})

    return render(request, 'responsibility.html', {'tasks_list': tasks_list})


