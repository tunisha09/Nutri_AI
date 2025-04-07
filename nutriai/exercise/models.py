from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ExerciseLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='Exercise')
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    calories_burned = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    body_part = models.CharField(max_length=20, default='full', choices=[
        ('chest', 'Chest'),
        ('back', 'Back'),
        ('arms', 'Arms'),
        ('abs', 'Abs'),
        ('legs', 'Legs'),
        ('full', 'Full Body'),
    ])
    
    def __str__(self):
        return f"{self.name} ({self.duration} min)"