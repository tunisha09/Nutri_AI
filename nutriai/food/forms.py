from django import forms
from .models import FoodLog

class FoodLogForm(forms.ModelForm):
    class Meta:
        model = FoodLog
        fields = ['name', 'calories', 'protein', 'carbs', 'fat', 'meal_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'calories': forms.NumberInput(attrs={'class': 'form-control'}),
            'protein': forms.NumberInput(attrs={'class': 'form-control'}),
            'carbs': forms.NumberInput(attrs={'class': 'form-control'}),
            'fat': forms.NumberInput(attrs={'class': 'form-control'}),
            'meal_type': forms.Select(attrs={'class': 'form-control'}),
        }
