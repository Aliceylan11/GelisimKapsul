from django.shortcuts import render


def home(request):
    context_dersler = [
        {
            "id": 1,
            "baslik": "Python ve Django",
            "aciklama": "Gelişim Kapsül projesi için backend geliştirme temelleri.",
            "resim": "https://placehold.co/600x400/1A374D/white?text=Django", 
            "egitmen": "Arda IRMAK"
        },
        {
            "id": 2,
            "baslik": "Web Tasarım (UI/UX)",
            "aciklama": "Bootstrap ve CSS ile modern, responsive arayüzler.",
            "resim": "https://placehold.co/600x400/F2994A/white?text=Tasarim",
            "egitmen": "Edanur BOZLAR"
        },
        {
            "id": 3,
            "baslik": "Veri Tabanı Yönetimi",
            "aciklama": "SQLite veritabanı modellemesi ve sorgular.",
            "resim": "https://placehold.co/600x400/406882/white?text=SQL",
            "egitmen": "Hasan Hüseyin KESKİN"
        },
        {
            "id": 4,
            "baslik": "Mobil Programlama",
            "aciklama": "Mobil uyumlu yapılar ve uygulama geliştirme.",
            "resim": "https://placehold.co/600x400/2D3436/white?text=Mobil",
            "egitmen": "Ali CEYLAN"
        },
        
    ]

    return render(request, 'dashboard/home.html', {"dersler": context_dersler})


def privacy_policy(request):
    return render(request, 'dashboard/privacy.html') 

def terms_of_use(request):
    return render(request, 'dashboard/terms.html') 

def pricing(request):
    return render(request, 'dashboard/pricing.html')

def corporate(request):
    return render(request, 'dashboard/corporate.html')