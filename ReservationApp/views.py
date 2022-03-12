from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import datetime

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


# class GetGenericReservationList(generics.ListCreateAPIView):
#     queryset = ReservationDetails.objects.all()
#     serializer_class = ReservationSerializer
#
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['hotel_name']

# def post(self, request, *args, **kwargs):
#     return HttpResponse(f"Booking Confirmed. Your confirmation number : {request.data}")


class GetGenericReservationList(APIView):

    def get_queryset(self):
        reservations = ReservationDetails.objects.all()
        return reservations

    def get(self, request, format=None):
        # print(request.query_params)
        checkindate = self.request.query_params.get('checkin_date')
        checkoutdate = self.request.query_params.get('checkout_date')
        city = self.request.query_params.get('address')
        print(city)
        if (city != None):
            checkindate = datetime.strptime(checkindate, "%Y-%m-%d").date()
            checkoutdate = datetime.strptime(checkoutdate, "%Y-%m-%d").date()
            # and checkindate != None and checkoutdate != None):
            # reserve = ReservationDetails.objects.filter(hotel_name=city)
            reservations = ReservationDetails.objects.filter(hotel_name__in=HotelList.objects.filter(address=city))
            reservation_count = {}
            for reservation in reservations:
                # if reservation.checkin_date >= checkoutdate or reservation.checkout_date <= checkindate:
                if ((checkindate <= reservation.checkin_date and checkoutdate >= reservation.checkout_date) | (
                        reservation.checkin_date <= checkindate <= reservation.checkout_date)
                        | (checkindate >= reservation.checkin_date and checkoutdate <= reservation.checkout_date) | (
                                checkindate <= reservation.checkin_date and checkoutdate >= reservation.checkout_date)):
                    if reservation.hotel_name.name in reservation_count:
                        reservation_count[reservation.hotel_name.name] += 1
                    else:
                        reservation_count[reservation.hotel_name.name] = 1
            # hotel_ob = [r.hotel_name.name for r in reservations]
            # reservation_count = {k:hotel_ob.count(k) for k in set(hotel_ob)}
            hotels = HotelList.objects.filter(address=city)
            for hotel in hotels:
                if hotel.name in reservation_count:
                    hotel.rooms_available -= reservation_count[hotel.name]
            hotel_serializer = HotelSerializer(hotels, many=True)
            return Response(hotel_serializer.data)
            print([(reservations.filter(hotel_name=hotel.name)).count() for hotel in hotels])
            count = 0
            serializer = HotelSerializer(hotels, many=True)
            print(count)

        else:
            reservations = self.get_queryset()
            serializer = ReservationSerializer(reservations, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            var = serializer.data.pop('confirmation_num')
            return Response(f"Booking Confirmed. Your confirmation number is : {var}", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
