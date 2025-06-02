from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Doctor(models.Model):
#     GENDER_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other'),
#     ]

#     full_name = models.CharField(max_length=100)
#     specialization = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=15)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     biography = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.full_name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    bio = models.TextField(blank=True)

    def __str__(self):
        if self.user:   
            return f"Dr. {self.user.get_full_name()}"
        return "Doctor"
    
    def full_name(self):
        return self.user.get_full_name()