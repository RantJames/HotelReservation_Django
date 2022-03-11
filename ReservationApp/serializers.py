from rest_framework import serializers, status
from rest_framework.response import Response

from .models import HotelList, ReservationDetails, GuestList
from django.core.exceptions import ValidationError


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelList
        fields = ['name', 'address', 'price']


class GuestSerializer(serializers.ModelSerializer):

    class Meta:
        model = GuestList
        fields = ['first_name', 'last_name', 'gender', 'address', 'age']


class ReservationSerializer(serializers.ModelSerializer):
    guestInReservation = GuestSerializer(many=True)

    class Meta:
        model = ReservationDetails
        fields = ['hotel_name', 'confirmation_num', 'checkin_date', 'checkout_date', 'guestInReservation']

    def create(self, validated_data):
        guest_validated_data = validated_data.pop('guestInReservation')
        reserve = ReservationDetails.objects.create(**validated_data)
        guest_set_serializer = self.fields['guestInReservation']
        for each in guest_validated_data:
            each['res'] = reserve
        guest_set_serializer.create(guest_validated_data)
        return reserve

    # def date_validate(self, validated_data):
    #     if validated_data['checkin_date'] > validated_data['checkout_date']:
    #         raise ValidationError("Checkin date should be less than checkout date")
    #     return validated_data
