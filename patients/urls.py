# patients/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # ⬇️ URL patterns for patient ⬇️
    path('', views.patient_list, name='patient_list'),
    path('add/', views.add_patient, name='add_patient'),
    path('delete/<int:pk>/', views.delete_patient, name='delete_patient'),
    path('search/', views.patient_search, name='patient_search'),
    path('patient/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('patients/<int:patient_id>/profile/', views.patient_profile, name='patient_profile'),


    # ⬇️ URL patterns for medical records ⬇️
    path('upload-record/<int:patient_id>/', views.upload_medical_record, name='upload_record'),
    path('records/', views.record_list, name='record_list'),
    path('record/<int:record_id>/edit/', views.edit_medical_record, name='edit_medical_record'),
    path('record/<int:record_id>/delete/', views.delete_medical_record, name='delete_medical_record'),
   

    # ⬇️ URL patterns for prescriptions ⬇️
    path('prescriptions/<int:patient_id>/', views.prescription_list, name='prescription_list'),
    path('upload-prescription/<int:patient_id>/', views.upload_prescription, name='upload_prescription'),
    path('prescription/<int:pk>/delete/', views.delete_prescription, name='delete_prescription'),
    path('prescription/<int:pk>/edit/', views.edit_prescription, name='edit_prescription'),


    # ⬇️ URL patterns for reports ⬇️
    path('reports/<int:patient_id>/', views.report_list, name='report_list'),
    path('upload-report/<int:patient_id>/', views.upload_report, name='upload_report'),
    path('report/<int:pk>/edit/', views.edit_report, name='edit_report'),
    path('report/<int:pk>/delete/', views.delete_report, name='delete_report'),
    
    
    # ⬇️ URL patterns for Authorization ⬇️
    path('unauthorized/', views.unauthorized_access, name='unauthorized_access'),

    
]

