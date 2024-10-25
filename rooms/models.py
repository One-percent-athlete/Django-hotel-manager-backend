from django.db import models

class RoomType(models.Model):
    title = models.CharField(max_length=20)
    details = models.JSONField(null=True)