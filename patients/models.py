from django.db import models
from django.contrib.auth.models import User
from doctors.models import Doctor
from django.contrib.auth.models import User

# Create your models here.

class Patient(models.Model): # Represents a patient in the healthcare system
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    address = models.TextField()
    occupation = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    medical_history = models.TextField(blank=True, null=True)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patients')

    def __str__(self):
        return self.name


class MedicalRecord(models.Model): # Represents a medical record associated with a patient
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    record_type = models.CharField(max_length=50, choices=[
        ('report', 'Report'),
        ('xray', 'X-Ray'),
        ('prescription', 'Prescription'),
        ('other', 'Other'),
    ])
    file = models.FileField(upload_to='medical_records/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} - {self.record_type}"


class Prescription(models.Model): # Represents a prescription for a patient
    doctor = models.ForeignKey(User, on_delete=models.CASCADE) 
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    diagnosis = models.TextField()
    medications = models.TextField()
    advice = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} - {self.date}"


class Report(models.Model): # Represents a report associated with a patient
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='reports')
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='reports/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.name} - {self.title}"


