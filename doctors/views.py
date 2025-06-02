from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor
from patients.models import Prescription, Patient
from .forms import DoctorRegistrationForm, DoctorProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

# ⬇️ Functions for doctor management or administration ⬇️

def doctor_list(request): # List all doctors
    doctors = Doctor.objects.all()
    return render(request, 'doctor/doctor_list.html', {'doctors': doctors})

# def doctor_create(request): # Create a new doctor
#     if request.method == 'POST':
#         form = DoctorRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('doctor_list')
#     else:
#         form = DoctorRegistrationForm()
#     return render(request, 'doctor/doctor_form.html', {'form': form, 'title': 'Add Doctor'})

def doctor_update(request, pk): # Update an existing doctor
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorRegistrationForm(instance=doctor)
    return render(request, 'doctor/doctor_form.html', {'form': form, 'title': 'Edit Doctor'})

def doctor_delete(request, pk): # Delete a doctor
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'doctor/doctor_confirm_delete.html', {'doctor': doctor})



# ⬇️ Doctors functions for registration, login, dashboard, profile, and logout ⬇️

def doctor_register(request): # Register a new doctor
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already exists.')
            else:
                form.save()  # Custom save method will handle user and doctor creation
                messages.success(request, "Registration successful. Please log in.")
                return redirect('doctor_login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = DoctorRegistrationForm()
    
    return render(request, 'doctor/register.html', {'form': form})


def doctor_login_view(request): # Login view for doctors
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            try:
                if hasattr(user, 'doctor'):
                    login(request, user)
                    return redirect('doctor_dashboard')
                else:
                    messages.error(request, 'You are not registered as a doctor.')
            except Doctor.DoesNotExist:
                messages.error(request, 'Doctor profile not found.')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'doctor/login.html')



@login_required
def doctor_logout_view(request): # Logout view for doctors
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('doctor_login')


@login_required
def doctor_dashboard(request): # Dashboard view for doctors
    doctor = request.user  # User instance
    prescriptions = Prescription.objects.filter(doctor=doctor).order_by('-date')
    patients = Patient.objects.filter(doctor=doctor)

    context = {
        'prescriptions': prescriptions,
        'patients': patients,
    }
    return render(request, 'doctor/dashboard.html', context)

@login_required
def doctor_profile(request): # Profile view for doctors
    doctor = get_object_or_404(Doctor, user=request.user)
    return render(request, 'doctor/profile.html', {'doctor': doctor})



@login_required
def edit_doctor_profile(request): # Edit profile view for doctors
    doctor = get_object_or_404(Doctor, user=request.user)

    if request.method == 'POST':
        form = DoctorProfileForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_profile')
    else:
        form = DoctorProfileForm(instance=doctor)

    return render(request, 'doctor/edit_profile.html', {'form': form})
