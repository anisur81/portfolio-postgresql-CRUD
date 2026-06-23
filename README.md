# Django CRUD Operations - Step by Step Guide

## Step 1: Create Model (Database Table)

```python
# models.py
from django.db import models

# Create your models here.
class contactreq(models.Model):
    orgtitle = models.CharField(max_length=150)
    phoneno = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    comment = models.TextField()
          
    def __str__(self):
        return self.orgtitle
```

## Step 2: Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## Step 3: Create Superuser and Register Model

```bash
python manage.py createsuperuser
```

```python
# admin.py
from django.contrib import admin
from .models import contactreq

# Register your models here.
admin.site.register(contactreq)
```

## Step 4: Configure Database Settings

```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydb',
        'USER': 'psqluser',
        'PASSWORD': 'psqluser',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

## Step 5: Create Forms

```python
# forms.py
from django import forms
from .models import contactreq

class ContactReqForm(forms.ModelForm):
    class Meta:
        model = contactreq
        fields = ['orgtitle', 'phoneno', 'email', 'address', 'comment']

        widgets = {
            'orgtitle': forms.TextInput(attrs={'class': 'form-control'}),
            'phoneno': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
```

## Step 6: Create Views

```python
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import contactreq
from .forms import ContactReqForm

# Home page views
def home(request):
    return render(request, 'overview.html')

def contact(request):
    return render(request, 'contact.html')

# 1. READ (List all contacts)
def contact_list(request):
    contacts = contactreq.objects.all()
    print("Records:", contacts.count())
    return render(request, 'contact_list.html', {'contacts': contacts})

# 2. CREATE (Add new contact)
def contact_create(request):
    if request.method == 'POST':
        form = ContactReqForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactReqForm()

    return render(request, 'contact_form.html', {
        'form': form,
        'action': 'Add New Contact'
    })

# 3. UPDATE (Edit contact)
def contact_update(request, pk):
    contact = get_object_or_404(contactreq, pk=pk)

    if request.method == 'POST':
        form = ContactReqForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactReqForm(instance=contact)

    return render(request, 'contact_form.html', {
        'form': form,
        'action': 'Update Contact'
    })

# 4. DELETE (Remove a Contact)
def contact_delete(request, pk):
    contact = get_object_or_404(contactreq, pk=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')

    return render(request, 'contact_confirm_delete.html', {
        'contact': contact
    })
```

## Step 7: Configure URLs

```python
# urls.py (main project)
from django.contrib import admin
from django.urls import path
from home import views as views_home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_home.home, name='overview'),
    path('contact/', views_home.contact, name='contact'),
    
    # CRUD URLs
    path('list/', views_home.contact_list, name='contact_list'),
    path('add/', views_home.contact_create, name='contact_create'),
    path('edit/<int:pk>/', views_home.contact_update, name='contact_update'),
    path('delete/<int:pk>/', views_home.contact_delete, name='contact_delete'),
]
```

## Step 8: Create Templates

### 8.1 Contact List Template (READ)

```html
<!-- contact_list.html -->
{% extends 'base.html' %}

{% block content %}
<section class="contact-banner section_gap">
    <div class="banner-content">
        <h1>Contact with Me</h1>
        <p>
            I am a DevSecOps Engineer specializing in CI/CD automation, cloud infrastructure,
            container orchestration, and secure system design.
        </p>
    </div>
</section>

<table border="1">
    <tr>
        <th>Organization</th>
        <th>Phone</th>
        <th>Email</th>
        <th>Address</th>
        <th>Comment</th>
        <th>Actions</th>
    </tr>

    {% for contact in contacts %}
    <tr>
        <td>{{ contact.orgtitle }}</td>
        <td>{{ contact.phoneno }}</td>
        <td>{{ contact.email }}</td>
        <td>{{ contact.address }}</td>
        <td>{{ contact.comment }}</td>
        <td>
            <a href="{% url 'contact_update' contact.id %}">Edit</a>
            <a href="{% url 'contact_delete' contact.id %}">Delete</a>
        </td>
    </tr>
    {% empty %}
    <tr>
        <td colspan="6">No records found.</td>
    </tr>
    {% endfor %}
</table>

<form>
    <a href="{% url 'contact_create' %}">Back to Entry Form</a>
</form>
{% endblock %}
```

### 8.2 Contact Form Template (CREATE/UPDATE)

```html
<!-- contact_form.html -->
{% extends 'base.html' %}

{% block content %}
<section class="contact-banner section_gap">
    <div class="banner-content">
        <h1>Contact with Me</h1>
        <p>
            I am a DevSecOps Engineer specializing in CI/CD automation, cloud infrastructure,
            container orchestration, and secure system design.
        </p>
    </div>
</section>

<form method="post">
    {% csrf_token %}

    <p>
        <label>Organization:</label><br>
        {{ form.orgtitle }}
    </p>

    <p>
        <label>Phone:</label><br>
        {{ form.phoneno }}
    </p>

    <p>
        <label>Email:</label><br>
        {{ form.email }}
    </p>

    <p>
        <label>Address:</label><br>
        {{ form.address }}
    </p>

    <p>
        <label>Comment:</label><br>
        {{ form.comment }}
    </p>

    <button type="submit">Save</button>
    <a href="{% url 'contact_list' %}">Back to List</a>
</form>
{% endblock %}
```

### 8.3 Contact Delete Confirmation Template

```html
<!-- contact_confirm_delete.html -->
{% extends 'base.html' %}

{% block content %}
<section class="contact-banner section_gap">
    <div class="banner-content">
        <h1>Contact with Me</h1>
        <h2>Delete Contact</h2>

        <p>
            Are you sure you want to delete this contact?
        </p>

        <p>
            <strong>Organization:</strong> {{ contact.orgtitle }} <br>
            <strong>Phone:</strong> {{ contact.phoneno }} <br>
            <strong>Email:</strong> {{ contact.email }}
        </p>

        <form method="post">
            {% csrf_token %}
            <button type="submit" style="color: red;">
                Yes, Delete
            </button>
            <a href="{% url 'contact_list' %}">Cancel</a>
        </form>
    </div>
</section>
{% endblock %}
```

## Summary of CRUD Operations

| Operation | URL Pattern | View Function | Template |
|-----------|-------------|---------------|----------|
| **CREATE** | `/add/` | `contact_create()` | `contact_form.html` |
| **READ** | `/list/` | `contact_list()` | `contact_list.html` |
| **UPDATE** | `/edit/<id>/` | `contact_update()` | `contact_form.html` |
| **DELETE** | `/delete/<id>/` | `contact_delete()` | `contact_confirm_delete.html` |

## Database Schema

| Field Name | Type | Max Length |
|------------|------|------------|
| orgtitle | CharField | 150 |
| phoneno | CharField | 20 |
| email | CharField | 50 |
| address | CharField | 250 |
| comment | TextField | Unlimited |
