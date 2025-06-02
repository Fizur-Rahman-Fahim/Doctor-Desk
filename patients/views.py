# patients/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient, MedicalRecord,Prescription, Report
from .forms import PatientForm, MedicalRecordForm, PrescriptionForm, ReportForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q


# Create your views here.

# Patient section


def patient_profile(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    prescriptions = Prescription.objects.filter(patient=patient).order_by('-date')
    reports = Report.objects.filter(patient=patient).order_by('-uploaded_at')
    medical_records = MedicalRecord.objects.filter(patient=patient).order_by('-uploaded_at')

    return render(request, 'patients/patient_profile.html', {
        'patient': patient,
        'prescriptions': prescriptions,
        'reports': reports,
        'medical_records': medical_records,
    })

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    medical_records = patient.medical_records.all()
    prescriptions = Prescription.objects.filter(patient=patient).order_by('-date')
    reports = Report.objects.filter(patient=patient)

    return render(request, 'patients/patient_detail.html', {
        'patient': patient,
        'medical_records': medical_records,
        'prescriptions': prescriptions,
        'reports': reports,
    })


@login_required
def patient_list(request):
    patients = Patient.objects.filter(doctor=request.user).order_by('-created_at')  # Filter by logged-in doctor
    return render(request, 'patients/patient_list.html', {'patients': patients})


@login_required
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.doctor = request.user  # Associates the patient with the logged-in doctor
            patient.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patients/add_patient.html', {'form': form})

def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    
    return render(request, 'patients/delete_patient_confirm.html', {'patient': patient})


def patient_search(request):
    query = request.GET.get('q', '')  # সার্চ টেক্সট
    gender = request.GET.get('gender', '')  # gender filter

    patients = Patient.objects.all()

    if query:
        patients = patients.filter(
            Q(name__icontains=query) |
            Q(phone__icontains=query) |
            Q(address__icontains=query) |
            Q(occupation__icontains=query)
        )
    if gender:
        patients = patients.filter(gender=gender)

    return render(request, 'patients/patient_search.html', {
        'patients': patients,
        'query': query,
        'gender': gender,
    })



# Patient section ends here

# Medical Record section

def upload_medical_record(request, patient_id): # Handles the upload of a medical record for a patient
    patient = get_object_or_404(Patient, id=patient_id)
    
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, request.FILES)
        if form.is_valid():
            record = form.save(commit=False) # Create a MedicalRecord instance without saving it to the database yet
            record.patient = patient # Associates the record with the patient
            record.save() # Save the record to the database
            return redirect('patient_profile', patient_id = patient.id) # Redirect to the patient's profile page
    else:
        form = MedicalRecordForm()
    return render(request, 'patients/upload_record.html', {'form': form, 'patient': patient})


def record_list(request): # Displays a list of all medical records in the system
    records = MedicalRecord.objects.all().order_by('-uploaded_at')
    return render(request, 'patients/record_list.html', {'records': records})


def edit_medical_record(request, record_id):
    medical_record = get_object_or_404(MedicalRecord, id=record_id)

    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, request.FILES, instance=medical_record)
        if form.is_valid():
            form.save()
            return redirect('patient_profile', patient_id=medical_record.patient.id)
    else:
        form = MedicalRecordForm(instance=medical_record)

    return render(request, 'patients/edit_medical_record.html', {
        'form': form,
        'medical_record': medical_record
    })


def delete_medical_record(request, record_id):
    record = get_object_or_404(MedicalRecord, id=record_id)
    if request.method == 'POST':
        record.delete()
        return redirect('patient_profile', patient_id=record.patient.id)
    return render(request, 'patients/delete_medical_record_confirm.html', {'record': record})



# Medical Record section ends here

# Prescription Section

@login_required
def upload_prescription(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if request.method == 'POST':
        diagnosis = request.POST.get('diagnosis')
        medications = request.POST.get('medications')
        advice = request.POST.get('advice')

        Prescription.objects.create(
            patient=patient,
            doctor=request.user,
            diagnosis=diagnosis,
            medications=medications,
            advice=advice
        )
        return redirect('patient_profile', patient_id=patient.id)

    return render(request, 'patients/prescription_form.html', {'patient': patient})


@login_required
def prescription_list(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    #  Doctor check
    if patient.doctor != request.user:
        return redirect('unauthorized_access')

    prescriptions = Prescription.objects.filter(patient=patient).order_by('-date')
    return render(request, 'patients/prescription_list.html', {
        'patient': patient,
        'prescriptions': prescriptions
    })


def edit_prescription(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    
    if request.method == 'POST':
        form = PrescriptionForm(request.POST, instance=prescription)
        if form.is_valid():
            form.save()
            return redirect('patient_profile', patient_id=prescription.patient.id)
    else:
        form = PrescriptionForm(instance=prescription)
    
    return render(request, 'patients/edit_prescription.html', {'form': form, 'prescription': prescription})


def delete_prescription(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    
    if request.method == 'POST':
        patient_id = prescription.patient.id
        prescription.delete()
        return redirect('patient_profile', patient_id=patient_id)
    else:
        # Render a confirmation page before deletion
        if prescription.doctor != request.user:
            return redirect('unauthorized_access')

    return render(request, 'patients/delete_prescription_confirm.html', {'prescription': prescription})


# End of Prescription Section

# Report Section


@login_required
def upload_report(request, patient_id): # Handles the upload of a report for a patient
    patient = get_object_or_404(Patient, id=patient_id)
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        title = request.POST.get('title')
        file = request.FILES.get('file')

        Report.objects.create(patient=patient, title=title, file=file)
        return redirect('patient_profile', patient_id=patient.id)

    patients = Patient.objects.filter(doctor=request.user) # Filter patients by the logged-in doctor
    return render(request, 'patients/report_form.html', {'patient': patient})


@login_required
def report_list(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    # Ensure doctor can only see their own patient's report
    if patient.doctor != request.user:
        return redirect('unauthorized_access')  

    reports = Report.objects.filter(patient=patient).order_by('-uploaded_at')
    return render(request, 'patients/report_list.html', {
        'patient': patient,
        'reports': reports
    })


def edit_report(request, pk):
    report = get_object_or_404(Report, pk=pk)

    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES, instance=report)
        if form.is_valid():
            form.save()
            return redirect('patient_profile', patient_id=report.patient.id)
    else:
        form = ReportForm(instance=report)

    return render(request, 'patients/edit_report.html', {'form': form, 'report': report})


def delete_report(request, pk):
    report = get_object_or_404(Report, pk=pk)

    if request.method == 'POST':
        patient_id = report.patient.id
        report.delete()
        return redirect('patient_profile', patient_id=patient_id)

    return render(request, 'patients/delete_report_confirm.html', {'report': report})


# End of Report Section 


# Authorization Check
def unauthorized_access(request):
    return render(request, 'patients/unauthorized.html')


