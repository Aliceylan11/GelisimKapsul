# courses/admin.py

from django.contrib import admin
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    # Slug'ı başlığı yazarken otomatik doldurur:
    prepopulated_fields = {'slug': ('title',)}