from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.home, name='dashboard/home'),
    path('gizlilik-politikasi/', views.privacy_policy, name='privacy'),
    path('kullanim-sartlari/', views.terms_of_use, name='terms'),
    path('fiyatlandirma/', views.pricing, name='pricing'),
    path('kurumsal/', views.corporate, name='corporate'),
]