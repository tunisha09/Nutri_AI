from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.db import DatabaseError
from django.contrib import messages
from food.models import FoodLog
from exercise.models import ExerciseLog
from datetime import datetime, timedelta
import random

@csrf_protect
@login_required
def weekly_report(request):
    try:
        user = request.user
        end_date = datetime.now()
        start_date = end_date - timedelta(days=7)
        
        # Mock data for demonstration
        days = [end_date - timedelta(days=i) for i in range(7)]
        days.reverse()
        
        calorie_data = [random.randint(1200, 2500) for _ in range(7)]
        exercise_data = [random.randint(100, 500) for _ in range(7)]
        
        return render(request, 'reports/weekly.html', {
            'days': days,
            'calorie_data': calorie_data,
            'exercise_data': exercise_data,
            'start_date': start_date,
            'end_date': end_date,
        })
    except Exception as e:
        messages.error(request, 'Error generating weekly report')
        return render(request, 'reports/weekly.html', {
            'days': [],
            'calorie_data': [],
            'exercise_data': [],
            'start_date': datetime.now(),
            'end_date': datetime.now(),
        })

@csrf_protect
@login_required
def monthly_report(request):
    try:
        user = request.user
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)
        
        # Mock data for demonstration
        weeks = [end_date - timedelta(weeks=i) for i in range(4)]
        weeks.reverse()
        
        calorie_data = [random.randint(6000, 15000) for _ in range(4)]
        exercise_data = [random.randint(500, 2000) for _ in range(4)]
        
        return render(request, 'reports/monthly.html', {
            'weeks': weeks,
            'calorie_data': calorie_data,
            'exercise_data': exercise_data,
            'start_date': start_date,
            'end_date': end_date,
        })
    except Exception as e:
        messages.error(request, 'Error generating monthly report')
        return render(request, 'reports/monthly.html', {
            'weeks': [],
            'calorie_data': [],
            'exercise_data': [],
            'start_date': datetime.now(),
            'end_date': datetime.now(),
        })

@csrf_protect
@login_required
def nutrition_report(request):
    try:
        # Mock data for demonstration
        macros = {
            'protein': random.randint(50, 150),
            'carbs': random.randint(100, 300),
            'fat': random.randint(30, 100),
        }
        
        return render(request, 'reports/nutrition.html', {
            'macros': macros,
        })
    except Exception as e:
        messages.error(request, 'Error generating nutrition report')
        return render(request, 'reports/nutrition.html', {
            'macros': {'protein': 0, 'carbs': 0, 'fat': 0},
        })

@csrf_protect
@login_required
def exercise_report(request):
    try:
        # Mock data for demonstration
        body_parts = ['Chest', 'Back', 'Arms', 'Abs', 'Legs', 'Full Body']
        exercise_counts = [random.randint(3, 15) for _ in range(6)]
        
        return render(request, 'reports/exercise.html', {
            'body_parts': body_parts,
            'exercise_counts': exercise_counts,
        })
    except Exception as e:
        messages.error(request, 'Error generating exercise report')
        return render(request, 'reports/exercise.html', {
            'body_parts': [],
            'exercise_counts': [],
        })

@csrf_protect
@login_required
def progress_report(request):
    try:
        # Mock data for demonstration
        weeks = [f"Week {i}" for i in range(1, 5)]
        weight_data = [round(random.uniform(60, 80), 1) for _ in range(4)]
        calorie_data = [random.randint(1500, 2500) for _ in range(4)]
        
        return render(request, 'reports/progress.html', {
            'weeks': weeks,
            'weight_data': weight_data,
            'calorie_data': calorie_data,
        })
    except Exception as e:
        messages.error(request, 'Error generating progress report')
        return render(request, 'reports/progress.html', {
            'weeks': [],
            'weight_data': [],
            'calorie_data': [],
        })
