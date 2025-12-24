from django.contrib import admin
from .models import Material

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin): 
    list_display = ('title', 'course', 'material_type', 'created_at') 
    fields = ('course', 'title', 'description', 'material_type', 'file', 'video_url')