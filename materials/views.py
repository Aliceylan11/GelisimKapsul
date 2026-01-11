from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MaterialForm
from courses.models import Course
from .models import Material
from django.shortcuts import get_object_or_404, HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse

User = get_user_model()

@login_required
def material_list(request):
    user = request.user
     
    if user.user_type == 'regular' and not user.is_superuser:
        return redirect('access_denied') 
   
    course_param = request.GET.get('course') # Sorgu parametresini al
    course_obj = None # Seçili dersi tutmak için

    if course_param: 
        if course_param.isdigit():
            # Evet sayı, o zaman ID'ye göre ara
            materials = Material.objects.filter(course_id=course_param).order_by('-created_at')
            course_obj = Course.objects.filter(id=course_param).first()
        else:
            # Hayır sayı değil (Veri Tabanı vb. yazıyor), o zaman Başlığa göre ara
            materials = Material.objects.filter(course__title=course_param).order_by('-created_at')
            course_obj = Course.objects.filter(title=course_param).first()
            
        current_course_name = course_obj.title if course_obj else "Bilinmeyen Ders"
    else:
        # Hiçbir şey gelmediyse hepsini getir
        materials = Material.objects.all().order_by('-created_at')
        current_course_name = 'Tüm Dersler'
        
    context = {
        'materials': materials, 
        'course_name': current_course_name,
        'course': course_obj
    }
    return render(request, 'materials/list.html', context)


@login_required
def upload_material(request,course_id):
    if request.user.user_type != 'instructor':
        return redirect('material_list')
    
    course = get_object_or_404(Course, id=course_id)
    courses = Course.objects.filter(id=course_id)
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            material = form.save(commit=False)
            material.course = get_object_or_404(Course, id=course_id)
            material.uploaded_by = request.user
            material.save()
            messages.success(request, 'Materyal başarıyla yüklendi.')
            return redirect(f"{reverse('material_list')}?course={course.title}")
    else:
        form = MaterialForm()
    context = {
        'course': course,      
        'courses': courses,  
        'form': form,
        'course_id': course_id
        }
    return render(request, 'materials/upload.html', context)


@login_required
def material_detail(request, id): 
    if request.user.user_type == 'regular' and not request.user.is_superuser:
        return redirect('access_denied')
     
    material = get_object_or_404(Material, id=id)
 
    other_materials = Material.objects.filter(course=material.course).exclude(id=id) # Diğer materyalleri filtrele seçilen materyal hariç

    context = {
        'material': material,
        'other_materials': other_materials  
    }
    
    return render(request, 'materials/detail.html', context)


@login_required
def delete_material(request, pk):
    material = get_object_or_404(Material, pk=pk)
    if request.user.user_type != 'instructor' and not request.user.is_superuser:
        return redirect('material_list')
    
    if request.method == 'POST':
        course_title = material.course.title
        material.delete()
        return redirect(f"{reverse('material_list')}?course={course_title}")

    return redirect('material_list')




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