from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

projectsList = [
    {
        'id':'1',
        'title': 'Playbliss',
        'desc': 'Video game catalog'

    },
    {
        'id':'2',
        'title': 'Playbliss',
        'desc': 'Video game catalog'

    },
    {
        'id':'3',
        'title': 'Playbliss',
        'desc': 'Video game catalog'

    }
    
]

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'devsearchProjects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'devsearchProjects/single-project.html', {'project': projectObj})



# Create your views here.
