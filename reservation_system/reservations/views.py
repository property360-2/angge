
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Reservation
from .forms import ReservationForm

@login_required
def reservation_list(request):
    reservations = Reservation.objects.filter(user=request.user)
    return render(request, 'reservations/reservation_list.html', {
        'reservations': reservations
    })

@login_required
def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, 'Reservation created successfully!')
            return redirect('reservation_list')
    else:
        form = ReservationForm()
    return render(request, 'reservations/reservation_form.html', {
        'form': form,
        'title': 'New Reservation'
    })

@login_required
def edit_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id, user=request.user)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reservation updated successfully!')
            return redirect('reservation_list')
    else:
        form = ReservationForm(instance=reservation)
    return render(request, 'reservations/reservation_form.html', {
        'form': form,
        'title': 'Edit Reservation'
    })

@login_required
def delete_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id, user=request.user)
    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Reservation deleted successfully!')
        return redirect('reservation_list')
    return render(request, 'reservations/reservation_confirm_delete.html', {
        'reservation': reservation
    })