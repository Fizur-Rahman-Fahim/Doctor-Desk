from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctor_list, name='doctor_list'),
    #path('add/', views.doctor_create, name='doctor_add'),
    path('edit/<int:pk>/', views.doctor_update, name='doctor_edit'),
    path('delete/<int:pk>/', views.doctor_delete, name='doctor_delete'),
    path('register/', views.doctor_register, name='doctor_register'),
    path('login/', views.doctor_login_view, name='doctor_login'),
    path('dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('profile/', views.doctor_profile, name='doctor_profile'),
    path('profile/edit/', views.edit_doctor_profile, name='edit_doctor_profile'),
    path('logout/', views.doctor_logout_view, name='doctor_logout'),
    
]
