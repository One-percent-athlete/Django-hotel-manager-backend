from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(blank=True, null=True)
    message = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.name} - {self.created_at}"
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to="profile_images/")
    phone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user} {self.phone}"
    
@receiver(post_save, sender=User)
def create_user_profiel(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)