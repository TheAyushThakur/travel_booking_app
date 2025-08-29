# pythonanywhere_config.py
import os
import sys

# Add your project directory to the Python path
path = '/home/Ayushthakur741/travel-booking-app'
if path not in sys.path:
    sys.path.append(path)

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'travel_bookings.settings'

# Import Django and set up
import django
django.setup()