from django import forms
from .models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['course', 'title', 'description', 'material_type', 'file', 'video_url']
 