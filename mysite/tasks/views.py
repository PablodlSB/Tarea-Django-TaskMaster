from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from .models import Project

# Create your views here.

@login_required
def dashboard(request):
    user = request.user

    mis_proyectos = (
        Project.objects
        .filter(owner=user)
        .annotate(
            total_tasks=Count('tasks'),
            done_tasks=Count('tasks', filter=Q(tasks__status='DONE'))
        )
    )

    colaboraciones = (
        Project.objects
        .filter(collaborators=user)
        .exclude(owner=user)
        .annotate(
            total_tasks=Count('tasks'),
            done_tasks=Count('tasks', filter=Q(tasks__status='DONE'))
        )
    )

    return render(request, 'tasks/dashboard.html', {
        'mis_proyectos': mis_proyectos,
        'colaboraciones': colaboraciones
    })


@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    done = project.tasks.filter(status='DONE').count()
    pending = project.tasks.exclude(status='DONE').count()

    return render(request, 'tasks/project_detail.html', {
        'project': project,
        'done_tasks': done,
        'pending_tasks': pending
    })
