from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import MaterialForm
from courses.models import Course
from .models import Material
from django.shortcuts import get_object_or_404

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

def access_denied(request):
    return render(request, 'materials/access_denied.html')

def payment(request):
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