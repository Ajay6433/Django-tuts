from django.shortcuts import render

# Create your views here.

def auth_views(request):
    return render(request,'auth.html')

def auth_login(request):
    return render(request,'login.html')