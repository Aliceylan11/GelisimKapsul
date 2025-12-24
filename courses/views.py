from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course
from django.db.models import Q, Count

@login_required
def list(request):
    # Başlangıç QuerySet'i
    all_courses = Course.objects.filter(is_active=True)

    # 1. Kategori Filtreleme
    selected_category = request.GET.get('category')
    if selected_category:
        all_courses = all_courses.filter(category=selected_category)

    # 2. Arama Mantığı (Title, Description VEYA Category içinde arar)
    search_query = request.GET.get('search')
    if search_query:
        all_courses = all_courses.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query) |
            Q(category__icontains=search_query) # Kategori ismine göre de arama eklendi
        )
 
    min_rating = request.GET.get('min_rating')
    if min_rating:
        all_courses = all_courses.filter(rating__gte=float(min_rating))
        
        
    # 4. Sıralama Mantığı
    sort_option = request.GET.get('sort')
    if sort_option == 'newest':
        all_courses = all_courses.order_by('-created_at')
    elif sort_option == 'rating':
        all_courses = all_courses.order_by('-rating')
    else:
        all_courses = all_courses.order_by('-created_at') # Varsayılan sıralama

    # Sidebar için Kategorileri ve Sayılarını çekme
    categories = Course.objects.values('category').annotate(count=Count('id')).order_by('category')
    total_count = Course.objects.filter(is_active=True).count()

    context = {
        'courses': all_courses,
        'categories': categories,
        'total_count': total_count,
        'selected_category': selected_category,
    }
    return render(request, 'courses/list.html', context)