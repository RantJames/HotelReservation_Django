from django.shortcuts import render
from django.http import HttpResponse
from .models import HotelList, ReservationDetails
# Create your views here.


def health_check(request):
    return HttpResponse('<h1>Health Ok</h1>')


def hotel_list(request):
    context = {
        'hotels': HotelList.objects.all()
    }
    return render(request, 'Hotel/HotelList.html', context)


def reservation_list(request):
    context = {
        'hotels': HotelList.objects.all(),
        'reservationList': ReservationDetails.objects.all()
    }
    return render(request, 'Reservation/ReservationList.html', context)
