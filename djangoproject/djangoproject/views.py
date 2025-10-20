from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home_view(request):
    # return HttpResponse("Welcome to the Django Project Home Page!")
    return render(request, 'index.html')

def about_view(request):
    return HttpResponse("This is the about page of the Django Project.")

def contact_view(request):
    return HttpResponse("Contact us at xyz@gmail.com")