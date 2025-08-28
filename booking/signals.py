from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Booking

@receiver(post_save, sender=Booking)
def update_seats_on_booking(sender, instance, created, **kwargs):
    if created and instance.status == 'Confirmed':
        # Update available seats
        travel_option = instance.travel_option
        travel_option.available_seats -= instance.number_of_seats
        travel_option.save()

@receiver(pre_delete, sender=Booking)
def return_seats_on_cancel(sender, instance, **kwargs):
    if instance.status == 'Confirmed':
        # Return seats to available pool
        travel_option = instance.travel_option
        travel_option.available_seats += instance.number_of_seats
        travel_option.save()