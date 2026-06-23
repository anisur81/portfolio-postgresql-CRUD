from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='overview'),
    path('contact/', views.contact, name='contact'),
]