from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='exercise_home'),
    path('body-part/<str:body_part>/', views.body_part_exercises, name='body_part'),
    path('log/', views.log_exercise, name='log_exercise'),
    path('history/', views.exercise_history, name='exercise_history'),
]