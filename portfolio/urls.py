"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from  home import views as views_home
from  skills import views as views_skills
from  projects import views as views_projects
from  about import views as views_about
from  cert import views as views_cert

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_home.home, name='overview'),
    path('skills/', views_skills.skills, name='skills'),
    path('projects/', views_projects.projects, name='projects'),
    path('contact/', views_home.contact, name='contact'),
    path('about/', views_about.about, name='about'),
    path('cert/', views_cert.cert, name='cert'),
]

 
 