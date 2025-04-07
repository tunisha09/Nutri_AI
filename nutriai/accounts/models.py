from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class User(AbstractUser):
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='accounts_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='accounts_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='O', blank=True)
    height = models.FloatField(help_text="Height in cm", null=True, blank=True)
    weight = models.FloatField(help_text="Weight in kg", null=True, blank=True)
    medical_history = models.TextField(blank=True, null=True)
    activity_level = models.FloatField(
        default=1.2,
        validators=[MinValueValidator(1.2), MaxValueValidator(2.5)],
        help_text="1.2 (sedentary) to 2.5 (very active)"
    )
    goal = models.CharField(max_length=20, choices=[
        ('lose', 'Lose Weight'),
        ('maintain', 'Maintain Weight'),
        ('gain', 'Gain Weight'),
    ], default='maintain')
    
    def __str__(self):
        return self.username
    
    def calculate_bmr(self):
        if self.gender == 'M':
            return 88.362 + (13.397 * self.weight) + (4.799 * self.height) - (5.677 * self.age)
        else:
            return 447.593 + (9.247 * self.weight) + (3.098 * self.height) - (4.330 * self.age)
    
    def calculate_daily_calories(self):
        return round(self.calculate_bmr() * self.activity_level)