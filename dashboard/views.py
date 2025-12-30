from django.shortcuts import render
from django.contrib.auth import get_user_model
from courses.models import Course
User = get_user_model()

def home(request):
   
    courses = Course.objects.all()[:4]
    ogrenci_sayisi = User.objects.count()
    egitmen_sayisi = User.objects.filter(is_staff=True).count()

    if egitmen_sayisi < 4:
        egitmen_sayisi = 4

    context = {
        "courses": courses,
        "stats": {
            "ogrenci": ogrenci_sayisi,
            "egitmen": egitmen_sayisi,
            "ders": Course.objects.count(),
            "memnuniyet": 98
        }
    }

    return render(request, 'dashboard/home.html', context)

def privacy_policy(request):
    return render(request, 'dashboard/privacy.html') 

def terms_of_use(request):
    return render(request, 'dashboard/terms.html') 

def pricing(request):
    return render(request, 'dashboard/pricing.html')

def corporate(request):
    ogrenci_sayisi = User.objects.count()
    egitmen_sayisi = User.objects.filter(is_staff=True).count()

    if egitmen_sayisi < 4:
        egitmen_sayisi = 4

    context = {
        "stats": {
            "ogrenci": ogrenci_sayisi,
            "egitmen": egitmen_sayisi,
            "ders": 4,
            "memnuniyet": 98
        }
    }
    return render(request, 'dashboard/corporate.html', context)