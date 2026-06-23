from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='overview'),
    path('skills/', views.skills, name='skills'),
]