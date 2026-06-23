from django.shortcuts import render

# Create your views here. (cert views)

def cert(request):
    return render(request, 'cert.html')
