from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course
from django.db.models import Q # Arama yapmak için gerekli

@login_required
def list(request):
    all_courses = Course.objects.all()

    # 1. Arama Mantığı (Title veya Description içinde arar)
    search_query = request.GET.get('search')
    if search_query:
        all_courses = all_courses.filter(
            Q(title__icontains=search_query) | 
            Q(description__icontains=search_query)
        )

    # 2. Sıralama Mantığı
    sort_option = request.GET.get('sort')
    if sort_option == 'newest':
        all_courses = all_courses.order_by('-created_at') # Yeniden eskiye
    elif sort_option == 'rating':
        all_courses = all_courses.order_by('-rating') # Yüksek puandan düşüğe

    context = {
        'courses': all_courses
    }
    return render(request, 'courses/list.html', context)