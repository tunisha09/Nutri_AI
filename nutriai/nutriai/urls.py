from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from accounts.views import register, profile, profile_update, change_password
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url='login/')),
    path('register/', register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('login/', RedirectView.as_view(url='/accounts/login/')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/update/', profile_update, name='profile_update'),
    path('password/change/', change_password, name='change_password'),
    path('dashboard/', include('dashboard.urls')),
    path('food/', include('food.urls')),
    path('exercise/', include('exercise.urls')),
    path('reports/', include('reports.urls')),
]