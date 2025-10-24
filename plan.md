# 🗓️ Simple Reservation System – Project Plan

## 📘 Overview

A **Django-based web application** that allows users to make, view, and manage reservations. This could be adapted for restaurants, meeting rooms, events, etc.

---

## ⚙️ Tech Stack

* **Backend:** Django (Python)
* **Database:** SQLite (for dev) / PostgreSQL (for production)
* **Frontend:** Django Templates (HTML, CSS, Bootstrap)
* **Authentication:** Django’s built-in auth system
* **Deployment:** Gunicorn + Nginx (Linux server) or Render/Heroku for simplicity

---

## 🧱 Project Structure

```
reservation_system/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── reservation_system/        # Main project folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
└── reservations/              # Main app
    ├── migrations/
    ├── templates/reservations/
    ├── static/reservations/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    └── views.py
```

---

## 🧩 Core Features

| Feature                       | Description                                                                      |
| ----------------------------- | -------------------------------------------------------------------------------- |
| **User Registration & Login** | Users can sign up and log in using Django’s auth system.                         |
| **Reservation Creation**      | Authenticated users can make a reservation by selecting date, time, and details. |
| **View Reservations**         | Users can view their existing reservations.                                      |
| **Edit/Cancel Reservation**   | Users can update or delete their reservations.                                   |
| **Admin Panel**               | Staff can view and manage all reservations.                                      |

---

## 🗄️ Models

**`Reservation`**

```python
from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"
```

---

## 🧮 Forms

**`ReservationForm`**

```python
from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'date', 'time', 'guests', 'notes']
```

---

## 🌐 URLs

**`reservations/urls.py`**

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('new/', views.create_reservation, name='create_reservation'),
    path('<int:id>/edit/', views.edit_reservation, name='edit_reservation'),
    path('<int:id>/delete/', views.delete_reservation, name='delete_reservation'),
]
```

---

## 🧠 Views

**Example: Create Reservation**

```python
from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required

@login_required
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'reservations/reservation_form.html', {'form': form})
```

---

## 🎨 Templates

Basic **Bootstrap-based** layout in:

```
reservations/templates/reservations/
├── base.html
├── reservation_form.html
├── reservation_list.html
```

Example snippet for `reservation_list.html`:

```html
{% extends 'reservations/base.html' %}
{% block content %}
<h2>Your Reservations</h2>
<a href="{% url 'create_reservation' %}" class="btn btn-primary">New Reservation</a>
<ul>
  {% for reservation in reservations %}
    <li>{{ reservation.name }} on {{ reservation.date }} at {{ reservation.time }}
      <a href="{% url 'edit_reservation' reservation.id %}">Edit</a> |
      <a href="{% url 'delete_reservation' reservation.id %}">Delete</a>
    </li>
  {% empty %}
    <li>No reservations yet.</li>
  {% endfor %}
</ul>
{% endblock %}
```

---

## 🚀 Deployment Steps

1. Set up virtual environment
2. Install dependencies (`pip install -r requirements.txt`)
3. Configure production database and environment variables
4. Run migrations and create superuser
5. Collect static files
6. Deploy using Gunicorn + Nginx or Render/Heroku

---

## 📅 Timeline (Example)

| Week | Task                                     |
| ---- | ---------------------------------------- |
| 1    | Set up Django project, app, and database |
| 2    | Implement models, forms, and views       |
| 3    | Build templates and user authentication  |
| 4    | Testing, bug fixes, and deployment       |

---
