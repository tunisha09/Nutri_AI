from django.urls import path
from . import views

urlpatterns = [
    path('weekly/', views.weekly_report, name='weekly_report'),
    path('monthly/', views.monthly_report, name='monthly_report'),
    path('nutrition/', views.nutrition_report, name='nutrition_report'),
    path('exercise/', views.exercise_report, name='exercise_report'),
    path('progress/', views.progress_report, name='progress_report'),
]