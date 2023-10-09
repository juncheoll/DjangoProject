from django.db import models

# Create your models here.

class Menu(models.Model):
    category = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    cost = models.IntegerField()
    dateTimeOfPosting = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='menu_image/', null=True, blank=True)
    class Meta:
        ordering = ["dateTimeOfPosting"]
