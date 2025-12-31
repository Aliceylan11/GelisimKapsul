from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course
from django.db.models import Q, Count # Django'nun Q nesnesi ve Count fonksiyonu filtreleme ve sayma işlemleri için kullandım.

@login_required
def list(request):
    # Başlangıç QuerySet'i
    all_courses = Course.objects.filter(is_active=True)

    # 1. Kategori Filtreleme
    selected_category = request.GET.get('category')
    if selected_category:
        all_courses = all_courses.filter(category=selected_category)

    # 2. Arama Mantığı (Title)
    search_query = request.GET.get('search')
    if search_query:
        all_courses = all_courses.filter(Q(title__icontains=search_query) | Q(instructor_name__icontains=search_query) | Q(category__icontains=search_query)) # Kategori ismine göre de arama eklendi
        
    # 3. Minimum Puan Filtreleme
    min_rating = request.GET.get('min_rating')
    if min_rating:
        all_courses = all_courses.filter(rating__gte=float(min_rating))
        

    # 4. Sıralama Mantığı
    sort_option = request.GET.get('sort')
    if sort_option == 'newest': # En yeni kurslar
        all_courses = all_courses.order_by('-created_at')
    elif sort_option == 'rating': # En yüksek puanlı kurslar
        all_courses = all_courses.order_by('-rating')
    else:
        all_courses = all_courses.order_by('-created_at') # Varsayılan sıralama

    # Sidebar için Kategorileri ve Sayılarını çekme
    categories = Course.objects.filter(is_active=True).values('category').annotate(count=Count('id')).order_by('category') # Her kategori için kurs sayısını alır.
    # Derslerin Toplam Sayısı
    total_count = Course.objects.filter(is_active=True).count()
    # Context Hazırlama
    context = {
        'courses': all_courses,
        'categories': categories,
        'total_count': total_count,
        'selected_category': selected_category,
    }
    return render(request, 'courses/list.html', context)