from django.shortcuts import render

# Create your views here.

def projects(request):
    active={'projects':'active'}
    return render(request,'projects/projects.html',active)