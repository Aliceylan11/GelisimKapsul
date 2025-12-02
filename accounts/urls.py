from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/duzenle/', views.profile_duzenle_view, name='profile_duzenle'),
    
]