
from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'date', 'time', 'guests', 'created_at']
    list_filter = ['date', 'created_at']
    search_fields = ['name', 'user__username']
    date_hierarchy = 'date'