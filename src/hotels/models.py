from django.db import models

# Create your models here.
class Hotels(models.Model):
    hotel_id = models.AutoField(primary_key=True)
    title  = models.CharField(max_length=50, default='default_title')
    name = models.CharField(max_length=30, default='default_name')
    alt = models.CharField(max_length=30, blank=True, null=True)
    address = models.CharField(max_length=100, default='default_address')
    directions = models.CharField(max_length=200, default='default_directions')
    phone = models.CharField(max_length=15, blank=True, null=True)
    tollfree = models.CharField(max_length=20, blank=True, null=True)
    fax = models.CharField(max_length=30, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    hours = models.CharField(max_length=5, blank=True, null=True)
    checkin = models.CharField(max_length=5, blank=True, null=True)
    checkout = models.CharField(max_length=5, blank=True, null=True)
    image = models.CharField(blank=True, null=True)
    price = models.CharField(max_length=10, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    activity = models.CharField(max_length=100, default='default_activity')
    type = models.CharField(max_length=20, default='default')
    availability = models.BooleanField(default=False)




    