# courses/models.py
from django.db import models

class Course(models.Model):
    # Dersin Adı (Örn: Web Programlama, Matematik 101)
    title = models.CharField(max_length=200, verbose_name="Ders Adı")
    
    # URL'de görünecek isim (Örn: web-programlama)
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL Yolu (Slug)")
    
    # Dersin kısa açıklaması
    description = models.TextField(blank=True, null=True, verbose_name="Açıklama")
    
    # Dersin kapak resmi
    image = models.ImageField(upload_to='courses/', blank=True, null=True, verbose_name="Ders Resmi")
    
    # Oluşturulma tarihi
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title