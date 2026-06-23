from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='overview'),
    path('cert/', views.cert, name='cert'),
]