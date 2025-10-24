
from django.urls import path
from . import views

urlpatterns = [
    path('', views.reservation_list, name='reservation_list'),
    path('new/', views.create_reservation, name='create_reservation'),
    path('<int:id>/edit/', views.edit_reservation, name='edit_reservation'),  # Fixed!
    path('<int:id>/delete/', views.delete_reservation, name='delete_reservation'),  # Fixed!
]