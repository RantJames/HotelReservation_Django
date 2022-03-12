from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone



# Create your models here.


class HotelList(models.Model):
    name = models.CharField(max_length=200, primary_key=True, validators=[
            RegexValidator(regex='^[a-zA-Z0-9]*$',
                           message='Hotel Name must be Alphanumeric',
                            code='invalid_hotel_name'
                        ),
                        ])
    address = models.CharField(max_length=500)
    price = models.IntegerField()
    last_updated = models.DateTimeField(default=timezone.now)
    rooms_available = models.IntegerField()


    def __str__(self):
        return self.name


class ReservationDetails(models.Model):
    confirmation_num = models.IntegerField(default=1000)
    hotel_name = models.ForeignKey(HotelList, on_delete=models.CASCADE)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    last_updated = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            last_id = ReservationDetails.objects.all().aggregate(largest=models.Max('confirmation_num'))['largest']
            if last_id is not None:
                self.confirmation_num = last_id + 1

        super(ReservationDetails, self).save(*args, **kwargs)

    def __str__(self):
        return self.hotel_name


class GuestList(models.Model):
    res = models.ForeignKey(ReservationDetails, on_delete=models.CASCADE, related_name="guestInReservation")
    first_name = models.CharField(max_length=200, validators=[
                RegexValidator(
                    regex='^[a-zA-Z]*$',
                    message='First Name must be Alphabets',
                    code='invalid_first_name'
                ),
            ])
    last_name = models.CharField(max_length=200, validators=[
                RegexValidator(
                    regex='^[a-zA-Z]*$',
                    message='Last Name must be Alphabets',
                    code='invalid_last_name'
                ),
            ])
    address = models.CharField(max_length=500)
    gender = models.CharField(max_length=1)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name+" "+self.last_name





