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
    description = models.TextField(blank=True, null=True, verbose_name='Açıklama')
    
    def __str__(self):
        return f"{self.title} - ({self.course.title})"
    
    def get_embed_url(self):
        if not self.video_url:
            return ""
        # YouTube kontrolü (mevcut kodun)
        if "youtube.com" in self.video_url or "youtu.be" in self.video_url:
            if "v=" in self.video_url:
                video_id = self.video_url.split("v=")[1].split("&")[0]
                return f"https://www.youtube.com/embed/{video_id}"
            elif "youtu.be/" in self.video_url:
                video_id = self.video_url.split("/")[-1]
                return f"https://www.youtube.com/embed/{video_id}"

        # VIMEO KONTROLÜ (Yeni eklenen kısım)
        if "vimeo.com" in self.video_url:
            # Link: https://vimeo.com/1063281516 -> ID: 1063281516
            video_id = self.video_url.split("/")[-1]
            return f"https://player.vimeo.com/video/{video_id}"

        return self.video_url