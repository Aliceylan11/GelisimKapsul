from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MaterialForm
from courses.models import Course
from .models import Material
from django.shortcuts import get_object_or_404, HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import messages
User = get_user_model()


@login_required
def material_list(request):
    user = request.user
    
    if user.user_type == 'regular' and not user.is_superuser:
        return redirect('access_denied') 
  
    course_filter = request.GET.get('course') 
    if course_filter:
        materials = Material.objects.filter(course__id=course_filter).order_by('-created_at')
        
        course_obj = Course.objects.filter(id=course_filter).first()
        current_course_name = course_obj.title if course_obj else "Bilinmeyen Ders"
    else:
        materials = Material.objects.all().order_by('-created_at')
        current_course_name = 'Tüm Dersler'
        
    context = {
        'materials': materials, 
        'course_name': current_course_name
    }
    return render(request, 'materials/list.html', context)

@login_required
def upload_material(request):
    if request.user.user_type != 'instructor':
        return redirect('material_list')
    return render(request, 'materials/upload.html')



@login_required
def material_detail(request, id):
    
    if request.user.user_type == 'regular':
        return redirect('access_denied')
    materials_data = Material.objects.all().values()
    selected_material = None
    for material in materials_data:
        if material['id'] == id:
            selected_material = material
            break     
    return render(request, 'materials/detail.html', {'material': selected_material})

@login_required
def access_denied(request):
    if request.user.user_type in ['student', 'instructor', 'premium']:
        return redirect('material_list')
    return render(request, 'materials/access_denied.html')

@login_required
def payment(request):
    if  request.user.user_type in ['student', 'instructor', 'premium']:
        return redirect('material_list') 
    return render(request, 'materials/payment.html')


@login_required
def add_material(request): 
    if not request.user.is_staff:
         return redirect('home')    

    if request.method == 'POST': 
        form = MaterialForm(request.POST, request.FILES)
        
        if form.is_valid(): 
            material = form.save(commit=False) 
            
            if material.material_type == 'pdf':
                material.video_url = None
            
            elif material.material_type == 'video':
                material.file = None
            
            material.save()
            return redirect('material_list') 
    else:
        form = MaterialForm()
        
    courses = Course.objects.all()

    context = {
        'form': form,
        'courses': courses
    }
    return render(request, 'materials/add_material.html', context)

@login_required
def delete_material(request, pk):
    material = get_object_or_404(Material, pk=pk)
    
    if request.method == 'POST':
        material.delete()
        
    return redirect(request.META.get('HTTP_REFERER', 'materials:material_list'))





@login_required
def odeme_basarili(request):
    user = request.user
    if request.user.is_authenticated and request.user.user_type in ['student', 'instructor', 'premium']:
        return redirect('dashboard/home')
    
    if user.is_authenticated: 
        User.objects.filter(id=request.user.id).update(user_type='premium')
        user.user_type = 'premium'
        print(f"Sihirli Değnek: {user.username} kullanıcısı ödeme ekranından dönünce Premium yapıldı!")
        
    return HttpResponse("""
        <div style="text-align:center; margin-top:50px;">
            <h1 style="color:green;">TEBRİKLER! ÖDEME BAŞARILI 🚀</h1>
            <p>PayTR işleminden başarıyla döndünüz.</p>
            <p style="background:#eee; padding:10px; display:inline-block;">
                <b>Sunum Notu:</b> Bildirim URL'si localhost olduğu için otomatik onay çalışmadı.<br>
                Lütfen Admin panelinden kullanıcıyı manuel olarak Premium yapın.
            </p>
            <br><br>
            <a href="/">Ana Sayfaya Dön</a>
        </div>
    """)
    
    

@login_required
def odeme_hata(request):
    return HttpResponse("""
        <div style="text-align:center; margin-top:50px;">
            <h1 style="color:red;">Üzgünüz, Ödeme Başarısız 😔</h1>
            <p>Bir sorun oluştu.</p>
            <a href="/">Ana Sayfaya Dön</a>
        </div>
    """)