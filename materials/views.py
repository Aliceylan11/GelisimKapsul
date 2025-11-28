from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def material_list(request):
    materials_data = [
        {'id': 1, 'title': 'Hafta 1: Algoritma Temelleri', 'type': 'PDF', 'uploader': 'Dr. Ahmet Yılmaz', 'date': '20.11.2025'},
        {'id': 2, 'title': 'Python Kurulum Rehberi', 'type': 'Video', 'uploader': 'Arş. Gör. Ali Ceylan', 'date': '27.11.2025'},
        {'id': 3, 'title': 'Veri Tabanı Yönetim Sistemleri İzlencesi', 'type': 'PDF', 'uploader': 'Prof. Dr. Ayşe Kaya', 'date': '01.10.2025'},
    ]
    return render(request, 'list.html', {'materials': materials_data})

def upload_material(request):
    return render(request, 'upload.html')