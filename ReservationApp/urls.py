from django.urls import path
from . import views

urlpatterns = [
    path('', views.health_check, name='HealthCheck'),
    path('hotelList/', views.hotel_list, name='HotelList'),
    path('resList/', views.reservation_list, name='ReservationList'),
    path('HotelGenList/', views.GetGenericHotelList.as_view(), name='GenericHotelList'),
    path('ResGenList/', views.GetGenericReservationList.as_view(), name='GenericReservationList')
]
