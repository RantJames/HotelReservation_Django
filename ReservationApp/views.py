from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.views import APIView

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


class GetGenericReservationList(APIView):

    def get(self, request, format=None):
        snippets = ReservationDetails.objects.all()
        serializer = ReservationSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            var = serializer.data.pop('confirmation_num')
            return Response(f"Booking Confirmed. Your confirmation number is : {var}", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)