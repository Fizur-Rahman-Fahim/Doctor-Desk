from django import forms
from .models import Patient, MedicalRecord, Prescription, Report

class PatientForm(forms.ModelForm): # Form for creating or updating patient information
    class Meta:
        model = Patient
        fields = ['name', 'age', 'gender', 'address', 'phone', 'occupation', 'medical_history']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter patient name'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter age'
            }),
            'gender': forms.Select(attrs={
                'class': 'form-select'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 2,
                'placeholder': 'Enter address'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number'
            }),
            'occupation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter occupation'
            }),
            'medical_history': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Enter medical history'
            }),
        }


class MedicalRecordForm(forms.ModelForm): # Form for uploading medical records associated with a patient
    class Meta:
        model = MedicalRecord
        fields = ['record_type', 'file']

        widgets = {
            'patient': forms.Select(attrs={
                'class': 'form-control'
            }),
            'record_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['patient', 'diagnosis', 'medications', 'advice']

        widgets = {
            'patient': forms.Select(attrs={
                'class': 'form-control'
            }),
            'diagnosis': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write diagnosis details...',
                'rows': 3
            }),
            'medications': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'List medications...',
                'rows': 4
            }),
            'advice': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter any additional advice...',
                'rows': 3
            }),
        }

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['title', 'file']
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter report title'
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

