from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from todolist.models import TaskList

# Create your views here.
def todolist(request):
    allTasks = TaskList.objects.all

    return render(request, 'todolist.html', {'allTasks': allTasks})

    context = {
    'welcome_text': "Welcome to the Task Page"
    }
    return render(request, 'todolist.html', context)

def contact(request):
    context = {
    'welcome_text': "Welcome to the Contact Us Page"
    }
    return render(request, 'todolist.html', context)

def about(request):
    context = {
    'welcome_text': "Welcome to the About Us Page"
    }
    return render(request, 'todolist.html', context)