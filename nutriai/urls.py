from django.urls import path, include
from rest_framework.routers import DefaultRouter
from nutriai.food.views import (
    log_camera,
    log_voice,
    weekly_report,
    food_history,
    log_food
)

router = DefaultRouter()

urlpatterns = [
    path('api/v1/', include([
        path('food/', include([
            path('logs/', log_food, name='food-logs'),
            path('logs/camera/', log_camera, name='food-logs-camera'),
            path('logs/voice/', log_voice, name='food-logs-voice'),
            path('history/', food_history, name='food-history'),
            path('reports/weekly/', weekly_report, name='food-reports-weekly'),
        ]))
    ])),
    
    # Legacy URLs with redirects for backward compatibility
    path('log/camera/', log_camera, name='legacy-log-camera'),
    path('log/voice/', log_voice, name='legacy-log-voice'),
    path('reports/weekly/', weekly_report, name='legacy-weekly-report'),
]
