from datetime import datetime
from django.contrib.auth.models import update_last_login
from django.db import models
from users.models import Account
import datetime
# Create your models here.


class Venue(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    venue_name = models.CharField(max_length=100)
    desc = models.CharField(null=True, max_length=1000)
    size = models.DecimalField(null=True, decimal_places=2, max_digits=15)
    capacity = models.IntegerField(default=0)
    picture = models.ImageField(
        upload_to='listings/',  db_column='Image', default='default.jpeg')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    pin = models.CharField(max_length=6)
    contact = models.CharField(max_length=10)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.venue_name


class Request(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    request_time = models.DateTimeField(auto_now=True)


class Booking(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    playground = models.ForeignKey(Venue, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    booking_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str([self.user, self.pk, self.booking_time])
