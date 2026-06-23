from django.shortcuts import render

 

from django.http import HttpResponse
# Create your views here. (skills views)


def skills(request):
    return render(request, 'skills.html')
