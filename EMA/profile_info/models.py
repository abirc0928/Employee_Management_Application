from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class user_profile(models.Model):
    address = models.CharField(max_length=255)  # Text input
    phone_number = models.CharField(max_length=20, ) 
    date_of_brith = models.DateField(null=True, blank=True)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile", default=1) #forein key add

    def __str__(self):
        return self.address