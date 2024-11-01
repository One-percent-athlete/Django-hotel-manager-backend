import uuid
from django.db import models
from django.contrib.auth.models import User

# from django.contrib.auth import get_user_model
# User = get_user_model()

class RoomType(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=20)
    details = models.JSONField(null=True)

    def __str__(self):
        return f"{self.title} - {self.uuid}"
    
class RoomImage(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, null=True, related_name="room_type_image")
    image = models.ImageField(upload_to="room_images/")

class Room(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return f"{self.room_number} - {self.room_type}"

class RoomBooking(models.Model):
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    total_guest = models.IntegerField()
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_details = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.room_number} - {self.user} - {self.checkin_date} - {self.checkout_date} - ${self.price}"
    
class Payment(models.Model):
    booking = models.ForeignKey(RoomBooking, on_delete=models.CASCADE)
    text_id = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    response_data = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.booking} - {self.total_price} - {self.date}"

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery_images/')

    class Meta:
        verbose_name_plural = 'Galleries'
