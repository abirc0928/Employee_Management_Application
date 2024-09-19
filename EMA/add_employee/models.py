from django.db import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=255)  # Text input
    address = models.CharField(max_length=255)  # Text input
    phone_number = models.CharField(max_length=20, )  # Text input
    salary = models.CharField(max_length=20)  # Numeric/Text input, non-editable after saving
    DESIGNATION_CHOICES = [
        ('Manager', 'Manager'),
        ('Developer', 'Developer'),
        ('Designer', 'Designer'),
        ('Intern', 'Intern'),
    ]
    designation = models.CharField(max_length=100, choices=DESIGNATION_CHOICES)  # Dropdown, non-editable after saving
    short_description = models.TextField()  # Text area input for a brief profile summary
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="employee", default=1) #forein key add
    
    def __str__(self):
        return self.name
    
    def get_truncated_content(self, num_words=15):
        words = self.short_description.split()  # Split content into words
        if len(words) > num_words:
            return ' '.join(words[:num_words]) + '...'  # Truncate and add '...' if needed
        return self.short_description  
   