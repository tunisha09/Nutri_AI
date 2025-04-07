from django import forms
from .models import ExerciseLog

class ExerciseLogForm(forms.ModelForm):
    class Meta:
        model = ExerciseLog
        fields = ['name', 'duration', 'calories_burned', 'body_part']
        widgets = {
            'duration': forms.NumberInput(attrs={'min': 1}),
            'calories_burned': forms.NumberInput(attrs={'min': 1}),
        }

    def __init__(self, *args, body_part=None, **kwargs):
        super().__init__(*args, **kwargs)
        if body_part:
            self.fields['body_part'].initial = body_part
            self.fields['body_part'].widget = forms.HiddenInput()
