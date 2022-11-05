from django.shortcuts import render

# Create your views here.
def home(request):
    active={'home':'active'}
    return render(request, 'core/home.html',active)
