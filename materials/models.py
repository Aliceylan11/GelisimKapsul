from django.db import models

# Create your models here.
from courses.models import Course


class Material(models.Model):
    TYPE_CHOICES = (
        ('pdf', 'PDF Document'),
        ('video', 'Video File')
    )
    course=models.ForeignKey(Course, on_delete=models.CASCADE, related_name='materials',verbose_name='Ders')
    title=models.CharField(max_length=255,verbose_name='Başlık')
    file=models.FileField(upload_to='materials/pdfs/',blank=True,null=True,verbose_name='Dosya')
    video_url=models.URLField(blank=True,null=True,verbose_name='Video URL')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name='Oluşturulma Tarihi')
    material_type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='pdf', verbose_name="Materyal Türü")
    def __str__(self):
        return f"{self.title} - ({self.course.title})"
    