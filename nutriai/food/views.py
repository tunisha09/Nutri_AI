from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ValidationError
from django.db import IntegrityError, DatabaseError
from .models import FoodLog
from .forms import FoodLogForm
import random

@csrf_protect
@login_required
@require_http_methods(["GET", "POST"])
def log_food(request):
    if request.method == 'POST':
        form = FoodLogForm(request.POST)
        try:
            if form.is_valid():
                food = form.save(commit=False)
                food.user = request.user
                food.save()
                messages.success(request, f'Successfully logged {food.name}')
                return redirect('dashboard')
        except (IntegrityError, ValidationError) as e:
            messages.error(request, f'Error saving food log: {str(e)}')
        except Exception as e:
            messages.error(request, f'Unexpected error: {str(e)}')
    else:
        form = FoodLogForm()
    return render(request, 'food/log_food.html', {'form': form})

@csrf_protect
@login_required
@require_http_methods(["GET", "POST"])
def log_camera(request):
    if request.method == 'POST':
        try:
            # Mock implementation - in a real app, this would process an image
            # Default to apple nutrition values
            food_name = "Apple (default)"
            food = FoodLog.objects.create(
                user=request.user,
                name=food_name,
                calories=52,  # Average apple calories
                protein=0.3,  # grams
                carbs=14,     # grams
                fat=0.2,      # grams
                meal_type=request.POST.get('meal_type', 'snack')
            )
            messages.success(request, f'Successfully logged {food_name} via camera')
            return redirect('dashboard')
        except (IntegrityError, ValidationError) as e:
            messages.error(request, f'Error saving camera log: {str(e)}')
        except Exception as e:
            messages.error(request, f'Unexpected camera error: {str(e)}')
    return render(request, 'food/log_camera.html')

@csrf_protect
@login_required
@require_http_methods(["GET", "POST"])
def log_voice(request):
    if request.method == 'POST':
        try:
            # Mock implementation - in a real app, this would process voice input
            food_name = request.POST.get('food_name', 'Spoken Food')
            if not food_name.strip():
                raise ValidationError('Food name cannot be empty')
                
            calories = random.randint(100, 500)
            
            food = FoodLog.objects.create(
                user=request.user,
                name=food_name,
                calories=calories,
                protein=random.randint(5, 30),
                carbs=random.randint(10, 60),
                fat=random.randint(2, 20),
                meal_type=request.POST.get('meal_type', 'snack')
            )
            messages.success(request, f'Successfully logged {food_name} via voice')
            return redirect('dashboard')
        except (IntegrityError, ValidationError) as e:
            messages.error(request, f'Voice input error: {str(e)}')
        except Exception as e:
            messages.error(request, f'Unexpected voice error: {str(e)}')
    return render(request, 'food/log_voice.html')

@csrf_protect
@login_required
def food_history(request):
    try:
        foods = FoodLog.objects.filter(user=request.user).order_by('-date')
    except DatabaseError:
        foods = []
        messages.error(request, 'Error loading food history')
    return render(request, 'food/history.html', {'foods': foods})
