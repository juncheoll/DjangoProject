from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=10)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    job_position = models.CharField(max_length=10)
    age = models.IntegerField(max_length=5)
    dateTimeOfPosting = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='user_image/', null=True, blank=True)
    class Meta:
        ordering = ["dateTimeOfPosting"]
