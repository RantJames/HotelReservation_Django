from django.urls import path
from . import views

urlpatterns = [
    path('', views.health_check, name='HealthCheck'),
    path('hotelList/', views.hotel_list, name='HotelList'),
    path('resList/', views.reservation_list, name='ReservationList')
]
