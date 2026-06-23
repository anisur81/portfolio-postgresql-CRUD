from django.shortcuts import render

from django.http import HttpResponse
# Create your views here. (about views)
def about(request):
    return render(request, 'about.html')