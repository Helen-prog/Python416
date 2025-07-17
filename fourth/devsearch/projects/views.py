from django.shortcuts import render
from .models import Project


def projects(request):
    pr = Project.objects.all()
    contex = {
        'projects': pr
    }
    return render(request, "projects/projects.html", contex)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    return render(request, "projects/single-project.html", {'project': project_obj})

