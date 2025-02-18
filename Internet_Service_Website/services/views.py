from django.shortcuts import render
from .models import InternetPlan

def home(request):
    plans = InternetPlan.objects.all()  # <-- Add this line to load plans on home page
    return render(request, 'home.html', {'plans': plans})

def plans(request):
    plans = InternetPlan.objects.all()
    return render(request, 'plans.html', {'plans': plans})
