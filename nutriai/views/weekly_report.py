from datetime import datetime, timedelta
import random
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from nutriai.food.models import FoodLog

@login_required
def weekly_report(request):
    # Calculate date range (Monday to Sunday of current week)
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    
    # Get user's food logs for the week
    logs = FoodLog.objects.filter(
        user=request.user,
        date__range=[start_of_week, end_of_week]
    ).order_by('date')
    
    # Calculate summary stats
    total_foods = logs.count()
    total_calories = sum(log.calories for log in logs) if logs else 0
    avg_protein = round(sum(log.protein for log in logs)/7, 1) if logs else 0
    
    # Prepare daily calories data for chart
    daily_labels = []
    daily_values = []
    max_calories = 0
    
    for i in range(7):
        day = start_of_week + timedelta(days=i)
        day_logs = logs.filter(date=day)
        day_calories = sum(log.calories for log in day_logs)
        
        daily_labels.append(day.strftime('%A'))
        daily_values.append(day_calories)
        
        if day_calories > max_calories:
            max_calories = day_calories
    
    # Fallback for empty week
    if max_calories == 0:
        max_calories = 1
    
    # Calculate macronutrient distribution
    total_protein = sum(log.protein for log in logs)
    total_carbs = sum(log.carbs for log in logs)
    total_fat = sum(log.fat for log in logs)
    total_macros = total_protein + total_carbs + total_fat
    
    macros = {
        'protein': round((total_protein/total_macros)*100) if total_macros > 0 else 0,
        'carbs': round((total_carbs/total_macros)*100) if total_macros > 0 else 0,
        'fat': round((total_fat/total_macros)*100) if total_macros > 0 else 0
    }
    
    # Generate AI feedback
    ai_feedback = generate_ai_feedback(logs, macros)
    
    context = {
        'week_start': start_of_week,
        'week_end': end_of_week,
        'total_foods': total_foods,
        'total_calories': total_calories,
        'avg_protein': avg_protein,
        'daily_labels': daily_labels,
        'daily_values': daily_values,
        'macros': macros,
        'ai_feedback': ai_feedback
    }
    
    return render(request, 'food/weekly_report.html', context)

def generate_ai_feedback(logs, macros):
    """Generate personalized nutrition feedback based on user's data"""
    if not logs:
        return "You haven't logged any foods this week. Start tracking to get personalized feedback!"
    
    # Basic feedback based on macros
    feedback = []
    
    if macros['protein'] < 20:
        feedback.append("Try increasing your protein intake for better muscle maintenance.")
    elif macros['protein'] > 35:
        feedback.append("Your protein intake is quite high - make sure to balance with other nutrients.")
    
    if macros['carbs'] < 40:
        feedback.append("Consider adding more complex carbs for sustained energy.")
    
    if macros['fat'] < 20:
        feedback.append("Healthy fats are important - try adding some nuts, avocados or olive oil.")
    
    if not feedback:
        feedback.append("Great job maintaining balanced macronutrients this week!")
    
    # Add random encouraging anime-themed message
    anime_messages = [
        "Keep up the good work! Your nutrition journey is like an anime training arc! 💪",
        "Every meal is a step closer to your health goals! Believe in the you that believes in yourself! ✨",
        "Your food logs are looking sharp! Just like a shonen protagonist's training regimen! 🍱",
        "Balanced macros? You're basically a nutrition ninja already! 🥷"
    ]
    feedback.append(random.choice(anime_messages))
    
    return " ".join(feedback)
