from django.shortcuts import render

materials_data = [
    {
        'id': 1, 
        'course': 'Web Programlama',
        'title': 'Hafta 1: Algoritma Temelleri', 
        'type': 'PDF', 
        'uploader': 'Arş. Gör. Arda Irmak', 
        'date': '20.11.2025',
        'description': 'Algoritma mantığına giriş, akış şemaları ve temel kavramlar.',
        'source': 'https://rezanhas.meb.k12.tr/meb_iys_dosyalar/34/30/316637/dosyalar/2021_02/04133655_1-Algoritmalar.pdf' 
    },
    {
        'id': 2, 
        'course': 'Web Programlama',
        'title': 'Python Kurulum Rehberi', 
        'type': 'Video', 
        'uploader': 'Arş. Gör. Edanur Bozlar', 
        'date': '27.11.2025',
        'description': 'VS Code kurulumu, Python ortam değişkenleri ve ilk "Hello World" uygulaması.',
        'source': 'https://www.youtube.com/embed/rKSfMRkpy-Y'
    },  
    {
        'id': 3, 
        'course': 'Web Programlama',
        'title': 'C# Kurulum Rehberi (Visual Studio)', 
        'type': 'Video', 
        'uploader': 'Arş. Gör. Ali Ceylan', 
        'date': '27.11.2025',
        'description': 'Visual Studio 2022 kurulumu, .NET ortam değişkenleri ve ilk "Console.WriteLine" uygulaması.',
        'source': 'https://player.vimeo.com/video/76979871'
    },
    {
        'id': 4, 
        'course': 'Web Programlama',
        'title': 'Veri Tabanı Yönetim Sistemleri', 
        'type': 'PDF', 
        'uploader': 'Arş. Gör. Ali Ceylan', 
        'date': '01.11.2025',
        'description': 'SQL dili temelleri, normalizasyon kuralları ve ER diyagramları.',
        'source': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'
    },{
        'id': 5, 
        'course': 'Web Programlama',
        'title': 'Bilgisayar Ağları ve Protokoller', 
        'type': 'PDF', 
        'uploader': 'Arş. Gör. Hasan Hüseyin Keskin', 
        'date': '01.12.2025',
        'description': 'Bilgisayar Ağları ve Protokoller konulu ders notları.',
        'source': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf'
    },
    {
        'id': 6, 
        'course': 'Matematik',
        'title': 'Türev ve İntegral Formülleri', 
        'type': 'PDF', 
        'uploader': 'Dr. Arda Irmak', 
        'date': '01.12.2025',
        'description': 'Mühendislik için temel türev alma kuralları.',
        'file_url': 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf' 
    },
    {
        'id': 7, 
        'course': 'Matematik',
        'title': 'Lineer Cebir - Matrisler', 
        'type': 'Video', 
        'uploader': 'Doç. Dr. Ali Ceylan', 
        'date': '02.12.2025',
        'description': 'Matrislerde toplama, çarpma ve determinant hesabı.',
        'video_url': 'https://www.youtube.com/embed/8st_Blr67vA' 
    },
]
def material_list(request):
    course_filter = request.GET.get('course')
    if course_filter:
        filtered_materials = [m for m in materials_data if m.get('course') == course_filter]
        current_course_name = course_filter
    else:
        filtered_materials = materials_data
        current_course_name = 'Tüm Dersler'
    context={
        'materials': filtered_materials,
        'course_name': current_course_name
    }
    return render(request, 'materials/list.html', context)

def upload_material(request):
    return render(request, 'materials/upload.html')

def material_detail(request, id):
    selected_material = None
    for material in materials_data:
        if material['id'] == id:
            selected_material = material
            break     
    return render(request, 'materials/detail.html', {'material': selected_material})

