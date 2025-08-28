from django.test import TestCase
from django.contrib.auth.models import User
from .models import TravelOption, Booking, UserProfile

class TravelBookingTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.travel_option = TravelOption.objects.create(
            type='Flight',
            source='New York',
            destination='London',
            departure_date='2023-12-15',
            departure_time='10:00:00',
            price=500,
            available_seats=50
        )
    
    def test_travel_option_creation(self):
        self.assertEqual(self.travel_option.source, 'New York')
        self.assertEqual(self.travel_option.destination, 'London')
        self.assertEqual(self.travel_option.available_seats, 50)
    
    def test_booking_creation(self):
        # Create a booking - this should automatically decrease available seats
        booking = Booking.objects.create(
            user=self.user,
            travel_option=self.travel_option,
            number_of_seats=2,
            total_price=1000,  # This will be recalculated in save() method
            status='Confirmed'
        )
        
        # Refresh from database to get updated values
        booking.refresh_from_db()
        self.travel_option.refresh_from_db()
        
        # Check that total price was calculated correctly
        self.assertEqual(booking.total_price, 1000)  # 2 seats * 500 = 1000
        
        # Check that booking status is correct
        self.assertEqual(booking.status, 'Confirmed')
        
        # Check that available seats decreased
        self.assertEqual(self.travel_option.available_seats, 48)  # 50 - 2 = 48
    
    def test_booking_cancellation(self):
        # Create a booking first
        booking = Booking.objects.create(
            user=self.user,
            travel_option=self.travel_option,
            number_of_seats=3,
            total_price=1500,
            status='Confirmed'
        )
        
        # Refresh to get updated values
        self.travel_option.refresh_from_db()
        
        # Check that seats were deducted
        self.assertEqual(self.travel_option.available_seats, 47)  # 50 - 3 = 47
        
        # Cancel the booking by deleting it
        booking.delete()
        
        # Refresh to get updated values
        self.travel_option.refresh_from_db()
        
        # Check that seats were returned
        self.assertEqual(self.travel_option.available_seats, 50)  # 47 + 3 = 50