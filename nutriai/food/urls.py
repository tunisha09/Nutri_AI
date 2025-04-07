from django.urls import path
from . import views

urlpatterns = [
    path('log/', views.log_food, name='log_food'),
    path('log/camera/', views.log_camera, name='log_camera'),
    path('log/voice/', views.log_voice, name='log_voice'),
    path('history/', views.food_history, name='food_history'),
]