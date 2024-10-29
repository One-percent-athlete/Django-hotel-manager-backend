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
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.IntegerField()
    message = models.TextField()
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


class Careers(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.IntegerField(null=True)
    message = models.TextField(null=True)
    cv = models.FileField(upload_to="cv_files/")
    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.name} - {self.created_at}"
    
    class Meta:
        verbose_name_plural = 'Careers'

class Banners(models.Model):
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='banner_images/')

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "banners"
        verbose_name_plural = 'Banners'


class ControlPanel(models.Model):
    image = models.ImageField(upload_to='logo_images/')


