from django.urls import path
from . import views  
from . import paytr  

urlpatterns = [
    path('', views.material_list, name='material_list'),
    path('upload/', views.upload_material, name='upload_material'),
    path('<int:id>/', views.material_detail, name='material_detail'),
    path('access_denied/', views.access_denied, name='access_denied'),
    path('sil/<int:pk>/', views.delete_material, name='delete_material'),
    
    # Ödeme İşlemleri (paytr.py'dan geliyor)
    path('odeme-yap/', paytr.odeme_sayfasi, name='payment_page'),
    path('callback/', paytr.callback, name='paytr_callback'),
    # YENİ EKLEYECEKLERİN:
    path('odeme-basarili/', views.odeme_basarili, name='odeme_basarili'),
    path('odeme-hata/', views.odeme_hata, name='odeme_hata'),
]