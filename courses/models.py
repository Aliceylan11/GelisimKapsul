from django.db import models

class Course(models.Model):
    CATEGORY_CHOICES = [
        ('Yazılım Mühendisliği', 'Yazılım Mühendisliği'),
        ('Bilgisayar Programlama', 'Bilgisayar Programlama'),
        ('Akademik', 'Akademik'),
        ('Matematik','Matematik'),
        ('Fizik', 'Fizik'),
        ('Kimya', 'Kimya'),
        ('Tasarım', 'Tasarım'),
        ('Kişisel Gelişim', 'Kişisel Gelişim'),
        ('Pazarlama', 'Pazarlama'),
        ('Fotoğrafçılık', 'Fotoğrafçılık'),
        ('Müzik', 'Müzik'),
    ]

    title = models.CharField(max_length=200, verbose_name="Ders Adı")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL Yolu (Slug)")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Yazılım', verbose_name="Kategori")
    description = models.TextField(blank=True, null=True, verbose_name="Açıklama")
    image = models.ImageField(upload_to='courses/', blank=True, null=True, verbose_name="Ders Resmi")
    
    instructor_name = models.CharField(max_length=100, verbose_name="Eğitmen Adı", default="Eğitmen Bilgisi Yok")
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=5.0, verbose_name="Puan")
    is_active = models.BooleanField(default=True, verbose_name="Aktif mi? (Yakında değilse aktif)")
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title