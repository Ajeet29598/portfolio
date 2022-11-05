from django.shortcuts import render

# Create your views here.

def skills(request):
    active={'skills':'active'}
    return render(request,'skills/skills.html',active)