from django.db import models
from helper.models import TimeStamp

class Banner(TimeStamp):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='banner_images', null=True, blank=True)

    def __str__(self):
        return self.name

class Feedback(TimeStamp):
    name = models.CharField(max_length=50)
    phone = models.PositiveIntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name
