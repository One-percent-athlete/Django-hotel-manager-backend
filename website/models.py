from django.db import models
from django.contrib.auth.models import User
from rooms.models import RoomBooking
from events.models import EventBooking

class Review(models.Model):
    user = user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(null=True)
    rating = models.IntegerField(default=1)
    room_booking = models.ForeignKey(RoomBooking, on_delete=models.SET_NULL, null=True)
    event_booking = models.ForeignKey(EventBooking, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.rating} - {self.created_at}"

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.IntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.name} - {self.created_at}"