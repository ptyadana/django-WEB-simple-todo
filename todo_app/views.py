from django.shortcuts import render,redirect
from .models import Task

# Create your views here.
def home(request,id=None):
    tasks = Task.objects.all()

    #if this is for completed task to delete, id will be passed
    if id:
        complete_task(id)
        return redirect('/')

    return render(request,'todo_app/home.html',{'tasks':tasks})


def add_task(request):
    """add new task"""
    if request.method == "POST":
        name = request.POST.get('name','')
        priority = request.POST.get('priority','')

        task = Task(name=name,priority=priority)
        task.save()

        #return to home page
        return redirect('/')

    return render(request,'todo_app/add_task.html',{})


def complete_task(id):
    """mark as complete for task and delete it"""
    task = Task.objects.get(id=id)
    task.delete()
     
        