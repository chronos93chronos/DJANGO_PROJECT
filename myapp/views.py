from django.http import HttpResponse, JsonResponse
from myapp.models import Project, Task
from django.shortcuts import render

# Create your views here.

def index(request):
    titulo = "DJANGO ES LA RAJA"
    return render(request, 'index.html',{
        'titulo':titulo
    })

def hello(request, username):
    return HttpResponse("<h1>hello %s</h1>"% username)

def about(request):
    return HttpResponse("ABOUT")

def projects(request):
    
    projects = Project.objects.all()
    return render(request, 'projectos.html',{
        'projects': projects
    })


def tasks(request):
    #task = Task.object(id=id)
    
    return render(request,'tasks.html')


