from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    page = 'projects'
    number = 10
    context = {'page': page, 'number': number}
    return render(request, 'devsearchProjects/projects.html', context)

def project(request, pk):
    return render(request, 'devsearchProjects/single-project.html')



# Create your views here.
