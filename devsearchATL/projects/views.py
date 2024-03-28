from django.shortcuts import render
from django.http import HttpResponse

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
    page = 'projects'
    number = 10
    context = {'page': page, 'number': number, 'projects': projectsList}
    return render(request, 'devsearchProjects/projects.html', context)

def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'devsearchProjects/single-project.html', {'project': projectObj})



# Create your views here.
