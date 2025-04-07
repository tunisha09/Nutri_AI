from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError
from food.models import FoodLog
from exercise.models import ExerciseLog
import random

@csrf_protect
@login_required
def dashboard(request):
    user = request.user
    context = {}
    
    try:
        # Mock data for demonstration
        today_calories = random.randint(1200, 2500)
        calorie_goal = 2000
        
        try:
            if user.height and user.weight and user.age:
                calorie_goal = user.calculate_daily_calories()
        except (AttributeError, TypeError, ValueError) as e:
            pass  # Fall back to default calorie_goal

        # Safely calculate percentage
        calorie_percentage = 0
        if calorie_goal > 0:
            calorie_percentage = min(100, int((today_calories / calorie_goal) * 100))

        # Get recent activities with error handling
        recent_foods = []
        recent_exercises = []
        try:
            recent_foods = FoodLog.objects.filter(user=user).order_by('-date')[:3]
            recent_exercises = ExerciseLog.objects.filter(user=user).order_by('-date')[:3]
        except (ObjectDoesNotExist, DatabaseError):
            pass  # Empty lists will be handled in template

        context = {
            'user': user,
            'today_calories': today_calories,
            'calorie_goal': calorie_goal,
            'calorie_percentage': calorie_percentage,
            'macros': {
                'protein': random.randint(50, 150),
                'carbs': random.randint(100, 300),
                'fat': random.randint(30, 100),
            },
            'heart_rate': random.randint(60, 100),
            'recent_foods': recent_foods,
            'recent_exercises': recent_exercises,
        }
        
    except Exception as e:
        # Log error here in production
        context['error'] = 'Unable to load dashboard data'

    return render(request, 'dashboard/dashboard.html', context)
