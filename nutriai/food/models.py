from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class FoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='Unnamed Food')
    calories = models.PositiveIntegerField()
    protein = models.FloatField(default=0)
    carbs = models.FloatField(default=0)
    fat = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    meal_type = models.CharField(max_length=10, choices=[
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
    ])
    
    def __str__(self):
        return f"{self.name} ({self.calories} kcal)"