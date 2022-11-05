from django.shortcuts import render

# Create your views here.

def education(request):
    active={'education':'active'}
    return render(request,'education/education.html',active)