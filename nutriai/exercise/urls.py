from django.urls import path
from . import views

app_name = 'exercise'

urlpatterns = [
    path('', views.home, name='home'),
    path('body_part/', views.body_part, name='body_part'),
    path('history/', views.history, name='history'),
    path('log_exercise/', views.log_exercise, name='log_exercise'),
    path('recommendations/', views.recommendations, name='recommendations'),
]
