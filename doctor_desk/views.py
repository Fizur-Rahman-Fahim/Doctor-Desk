# core/views.py (or any app, e.g. home/views.py)

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
