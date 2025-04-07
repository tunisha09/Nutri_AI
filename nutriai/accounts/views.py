from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_http_methods
from .forms import CustomUserCreationForm, ProfileUpdateForm, CustomPasswordChangeForm

@csrf_protect
@require_http_methods(["GET", "POST"])
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        try:
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, 'Registration successful! Please complete your profile.')
                return redirect('profile_update')
        except IntegrityError:
            messages.error(request, 'Username or email already exists')
        except ValidationError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, 'An error occurred during registration')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'registration/profile.html', {'user': request.user})

@csrf_protect
@login_required
@require_http_methods(["GET", "POST"])
def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Your profile has been updated!')
                return redirect('dashboard')
        except ValidationError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, 'An error occurred while updating your profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'registration/profile_update.html', {'form': form})

@csrf_protect
@login_required
@require_http_methods(["GET", "POST"])
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        try:
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated!')
                return redirect('profile')
            else:
                messages.error(request, 'Please correct the error below.')
        except ValidationError as e:
            messages.error(request, str(e))
        except Exception as e:
            messages.error(request, 'An error occurred while changing your password')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {'form': form})
