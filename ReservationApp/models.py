from django.db import models
from django.utils import timezone

# Create your models here.


class HotelList(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    price = models.IntegerField()
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class ReservationDetails(models.Model):
    res_id = models.ForeignKey(HotelList, on_delete=models.CASCADE, primary_key=True)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.res_id





