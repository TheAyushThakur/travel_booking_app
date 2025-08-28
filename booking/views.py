from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import TravelOption, Booking, UserProfile
from .forms import (UserRegisterForm, UserUpdateForm, 
                   ProfileUpdateForm, BookingForm, TravelSearchForm)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'booking/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.userprofile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'booking/profile.html', context)

def travel_list(request):
    form = TravelSearchForm(request.GET or None)
    travel_options = TravelOption.objects.all()
    
    if form.is_valid():
        type = form.cleaned_data.get('type')
        source = form.cleaned_data.get('source')
        destination = form.cleaned_data.get('destination')
        departure_date = form.cleaned_data.get('departure_date')
        
        if type:
            travel_options = travel_options.filter(type=type)
        if source:
            travel_options = travel_options.filter(source__icontains=source)
        if destination:
            travel_options = travel_options.filter(destination__icontains=destination)
        if departure_date:
            travel_options = travel_options.filter(departure_date=departure_date)
    
    context = {
        'travel_options': travel_options,
        'form': form
    }
    return render(request, 'booking/travel_list.html', context)

@login_required
def book_travel(request, travel_id):
    travel_option = get_object_or_404(TravelOption, pk=travel_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST, travel_option=travel_option)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.travel_option = travel_option
            booking.total_price = travel_option.price * booking.number_of_seats
            booking.save()
            
            # Update available seats
            travel_option.available_seats -= booking.number_of_seats
            travel_option.save()
            
            messages.success(request, 'Your booking has been confirmed!')
            return redirect('booking_list')
    else:
        form = BookingForm(travel_option=travel_option)
    
    context = {
        'travel_option': travel_option,
        'form': form
    }
    return render(request, 'booking/book_travel.html', context)

@login_required
def booking_list(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    return render(request, 'booking/booking_list.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)
    
    if request.method == 'POST':
        # Return seats to available pool
        travel_option = booking.travel_option
        travel_option.available_seats += booking.number_of_seats
        travel_option.save()
        
        # Cancel booking
        booking.status = 'Cancelled'
        booking.save()
        
        messages.success(request, 'Your booking has been cancelled.')
        return redirect('booking_list')
    
    return render(request, 'booking/cancel_booking.html', {'booking': booking})