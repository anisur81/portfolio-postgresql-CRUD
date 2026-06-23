from django.shortcuts import render

# Create your views here. (home apps views)
from django.http import HttpResponse

def home(request):
    return render(request, 'overview.html')

def contact(request):
    return render(request, 'contact.html')
