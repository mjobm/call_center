from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Request(models.Model):
    project_name = models.CharField(max_length=100)
    number_of_slots = models.CharField(max_length=100)
    date_from = models.DateField(auto_now_add=True)
    date_to = models.DateField()
    email = models.EmailField()
    notes = models.TextField()
    approved = models.BooleanField(default=False)
    declined = models.BooleanField(default=False)


class Computer(models.Model):
    label = models.CharField(verbose_name="Label", max_length=100)
    serial_number = models.CharField(verbose_name="Serial Number", max_length=100)


class Booker(models.Model):
    computer_slot = models.ForeignKey(Computer, verbose_name="Computer Slot", related_name="call_center_computer")
    booker = models.ForeignKey(User, verbose_name="User Booking", related_name='inventory_borrower')
    date_booked = models.DateField(verbose_name="Date Booked", auto_now_add=True)
    date_released = models.DateField(verbose_name="Date Released", null=True)
    project = models.CharField(verbose_name="Project", max_length=100)

