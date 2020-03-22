from django.shortcuts import render,redirect
from .models import Task

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    return render(request,'todo_app/home.html',{'tasks':tasks})


def add_task(request):
    if request.method == "POST":
        name = request.POST.get('name','')
        priority = request.POST.get('priority','')

        task = Task(name=name,priority=priority)
        task.save()

        #return to home page
        return redirect('/')

    return render(request,'todo_app/add_task.html',{})