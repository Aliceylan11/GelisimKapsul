from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='accounts/login'),
    path('register/', views.register_view, name='accounts/register'),
    
    path('logout/', views.logout_view, name='logout'), 

    path('profile/', views.profile_view, name='accounts/profile'),
    path('profile/duzenle/', views.profile_duzenle_view, name='accounts/profile_duzenle'),
]