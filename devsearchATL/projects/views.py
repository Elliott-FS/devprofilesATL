from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm



def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'devsearchProjects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'devsearchProjects/single-project.html', {'project': projectObj})


def createProject(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request, 'devsearchProjects/projects_form.html', context)
# Create your views here.
