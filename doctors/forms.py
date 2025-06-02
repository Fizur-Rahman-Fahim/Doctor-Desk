from django import forms
from .models import Doctor
from django.contrib.auth.models import User


# class DoctorForm(forms.ModelForm):
#     class Meta:
#         model = Doctor
#         fields = '__all__'
#         widgets = {
#             'full_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'specialization': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'phone': forms.TextInput(attrs={'class': 'form-control'}),
#             'gender': forms.Select(attrs={'class': 'form-control'}),
#             'biography': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
#         }

class DoctorRegistrationForm(forms.ModelForm): # Custom form for doctor registration
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta: # Meta class to define model and fields for the form
        model = Doctor
        fields = ['specialization', 'phone', 'bio']

    def save(self, commit=True): # Method to save the form data
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email']
        )
        doctor = super().save(commit=False) # Create a doctor instance without saving it yet
        doctor.user = user
        if commit: # If commit is True, save the doctor instance
            doctor.save()
        return doctor
    

class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['specialization', 'phone', 'bio']

    def __init__(self, *args, **kwargs):
        super(DoctorProfileForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': f'Enter {field.label}'
            })
