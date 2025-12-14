from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    list_display = ['username', 'email', 'first_name', 'last_name', 'user_type', 'university', 'is_staff']
    
    list_display_links = ['username', 'email']
    
    list_filter = ['user_type', 'is_staff', 'is_superuser', 'university']
    
    search_fields = ['username', 'email', 'first_name', 'last_name', 'university']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Gelişim Kapsül Özel Bilgiler', {
            'fields': ('user_type', 'university', 'department', 'bio', 'profile_image')
        }),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('email', 'first_name', 'last_name', 'user_type', 'university', 'department')
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)