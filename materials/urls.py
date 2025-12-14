from django.urls import path
from . import views

urlpatterns = [
    path('', views.material_list, name='material_list'),
    path('upload/', views.upload_material, name='upload_material'),
    path('<int:id>/', views.material_detail, name='material_detail'),
    path('access_denied/', views.access_denied, name='access_denied'),
    path('payment/', views.payment, name='payment_page'),
    path('sil/<int:pk>/', views.delete_material, name='delete_material'),
]