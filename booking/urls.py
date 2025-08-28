from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='booking/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='booking/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('', views.travel_list, name='travel_list'),
    path('book/<int:travel_id>/', views.book_travel, name='book_travel'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
]