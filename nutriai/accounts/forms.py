from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'medical_history')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'medical_history')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['age', 'gender', 'height', 'weight', 'activity_level', 'goal', 'medical_history']
        widgets = {
            'medical_history': forms.Textarea(attrs={'rows': 3}),
        }

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})