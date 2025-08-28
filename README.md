# Travel Booking Application

A Django-based web application for booking travel options (flights, trains, buses) with user authentication, booking management, and responsive design.

## Features

- **User Management**: Registration, login, logout, and profile management
- **Travel Options**: Browse flights, trains, and buses with filtering capabilities
- **Booking System**: Book travel options with seat validation
- **Booking Management**: View and cancel bookings
- **Responsive Design**: Bootstrap 5 based UI that works on all devices
- **Admin Interface**: Manage travel options and bookings through Django admin
- **MySQL Database**: Production-ready database setup

## Live Demo

Check out the live application: [Your Deployment URL Here]

## Prerequisites

- Python 3.8+
- MySQL Server
- pip (Python package manager)

## Installation & Setup

### 1. Clone the Repository

git clone https://github.com/TheAyushThakur/travel_booking_app
cd travel-booking-app

### 2. Create virtual environment
python -m venv venv

#### Activate virtual environment
##### On Windows:
  venv\Scripts\activate
##### On macOS/Linux:
source venv/bin/activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Database Setup
MySQL Setup:

CREATE DATABASE travel_booking_db;
CREATE USER 'travel_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON travel_booking_db.* TO 'travel_user'@'localhost';
FLUSH PRIVILEGES;

### 5. Apply Migrations
python manage.py makemigrations
python manage.py migrate

### 6. Create Superuser
python manage.py createsuperuser

### 7. Run Development Server
python manage.py runserver
Visit http://127.0.0.1:8000/ to view the application.

## Testing
Run the test suite:
python manage.py test


