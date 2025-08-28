from django.contrib import admin
from .models import TravelOption, Booking, UserProfile

@admin.register(TravelOption)
class TravelOptionAdmin(admin.ModelAdmin):
    list_display = ('travel_id', 'type', 'source', 'destination', 'departure_date', 'departure_time', 'price', 'available_seats')
    list_filter = ('type', 'source', 'destination', 'departure_date')
    search_fields = ('source', 'destination')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id', 'user', 'travel_option', 'number_of_seats', 'total_price', 'booking_date', 'status')
    list_filter = ('status', 'booking_date')
    search_fields = ('user__username', 'travel_option__source', 'travel_option__destination')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone_number')
    search_fields = ('user__username', 'phone_number')