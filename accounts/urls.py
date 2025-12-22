from django.urls import path, reverse_lazy
from . import views 
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/', views.login_view, name='accounts/login'),
    path('register/', views.register_view, name='accounts/register'),
    path('logout/', views.logout_view, name='logout'), 


    path('profile/', views.profile_view, name='accounts/profile'),
    path('profile/duzenle/', views.profile_duzenle_view, name='accounts/profile_duzenle'),
    path('verify/', views.verify_email, name='verify_email'),
    
    # 1. Email Girme Ekranı  
    path('forgot-password/', auth_views.PasswordResetView.as_view(
        template_name="accounts/forgot_password.html",
        html_email_template_name="accounts/password_reset_email.html", 
        subject_template_name="accounts/password_reset_subject.txt",
        success_url=reverse_lazy("password_reset_done")
    ), name="forgot_password"),
    
    # 2. "Email Gönderildi" Ekranı
    path('forgot-password/done/', auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_done.html"
    ), name="password_reset_done"),

    # 3. Yeni Şifre Belirleme Ekranı (Linke tıklayınca gelir)
    path('reset-password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="accounts/reset_password.html",
        success_url=reverse_lazy("password_reset_complete")
    ), name="password_reset_confirm"),

    # 4. "Başardın" Ekranı
    path('reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="accounts/password_reset_complete.html"
    ), name="password_reset_complete"),
]