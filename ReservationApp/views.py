from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from rest_framework import filters
from .models import HotelList, ReservationDetails, GuestList
from rest_framework.decorators import api_view

# Create your views here.
from .serializers import HotelSerializer, ReservationSerializer


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
        'reservationList': ReservationDetails.objects.all(),
        'guestList': GuestList.objects.all()
    }
    return render(request, 'Reservation/ReservationList.html', context)


class GetGenericHotelList(generics.ListCreateAPIView):
    queryset = HotelList.objects.all()
    serializer_class = HotelSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'address']


class GetGenericReservationList(generics.ListCreateAPIView):
    queryset = ReservationDetails.objects.all()
    serializer_class = ReservationSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['hotel_name']

    # def post(self, request, *args, **kwargs):
    #     return HttpResponse(f"Booking Confirmed. Your confirmation number : {request.data}")

