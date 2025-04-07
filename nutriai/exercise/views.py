from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'exercise/home.html')

def body_part(request):
    return render(request, 'exercise/body_part.html')

def history(request):
    return render(request, 'exercise/history.html')

def log_exercise(request):
    return render(request, 'exercise/log_exercise.html')

def recommendations(request):
    return render(request, 'exercise/recommendations.html')
