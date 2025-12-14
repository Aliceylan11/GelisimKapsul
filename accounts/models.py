from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    STATUS_CHOICES = (
        ('regular', 'Standart Kullanıcı'),
        ('student', 'Öğrenci'),
        ('premium', 'Premium Üye'),
    )

    
    university = models.CharField(max_length=150, blank=True, null=True, verbose_name="Üniversite")
    department = models.CharField(max_length=150, blank=True, null=True, verbose_name="Bölüm")
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name="Hakkımda")
    profile_image = models.ImageField(upload_to='avatars/', blank=True, null=True, default='avatars/default.png', verbose_name="Profil Fotoğrafı")

    
    user_type = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='regular',
        verbose_name="Kullanıcı Statüsü"
    )

    
    email = models.EmailField(unique=True, verbose_name="E-posta Adresi")

    def save(self, *args, **kwargs):
       
        
        if self.user_type == 'regular' and self.email:
            email_domain = self.email.split('@')[-1]
            if 'edu.tr' in email_domain or 'edu' in email_domain:
                self.user_type = 'student'
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
