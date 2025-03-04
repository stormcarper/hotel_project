from django.db import models
from django_countries.fields import CountryField

# Create your models here.
class Hotel(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    title  = models.CharField(max_length=50, default='default_title')
    name = models.CharField(max_length=30, default='default_name')
    alt = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=100, default='default_address')
    directions = models.CharField(max_length=200, default='default_directions')
    phone = models.CharField(max_length=15, blank=True, null=True)
    tollfree = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    hours = models.CharField(max_length=5, blank=True, null=True)
    checkin = models.CharField(max_length=5, blank=True, null=True)
    checkout = models.CharField(max_length=5, blank=True, null=True)
    image = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=25, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    activity = models.CharField(max_length=100, default='default_activity')
    type = models.CharField(max_length=20, default='default')
    availability = models.BooleanField(default=False)

class Geo(models.Model):
    geo_id = models.AutoField(primary_key=True)
    hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE, related_name='geo', null=True)
    lat = models.CharField(max_length=20, default="default_lat")
    lon = models.CharField(max_length=20, default="default_lon")

class Room(models.Model):
    room_id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='rooms', null=True)
    room_type = models.CharField(max_length=50, default="default_type")
    price = models.CharField(max_length=20, default="default_price")
    availability = models.BooleanField(default=False)

class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reservations', null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations', null=True)
    price = models.CharField(max_length=20, default="default_price")
    start_date = models.DateField()
    end_date = models.DateField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    country = CountryField()




