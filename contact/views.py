from django.shortcuts import render

# Create your views here.
def contact(request):
    active={'contact':'active'}
    return render(request,'contact/contact.html',active)