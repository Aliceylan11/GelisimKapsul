from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required

User = get_user_model()

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard/home')

    if request.method == "POST":
        girilen_veri = request.POST.get('username') 
        sifre = request.POST.get('password')

        user = authenticate(request, username=girilen_veri, password=sifre)

        if user is None:
            try:
                temp_user = User.objects.get(email=girilen_veri)
                user = authenticate(request, username=temp_user.username, password=sifre)
            except User.DoesNotExist:
                user = None

        if user is not None:
            login(request, user)
            messages.success(request, f"Tekrar hoş geldin, {user.first_name}!")
            return redirect('dashboard/home')
        else:
            messages.error(request, "Girdiğin bilgiler (Email veya Şifre) hatalı.")
            return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard/home')

    if request.method == "POST":
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        
        university = request.POST.get("university")
        department = request.POST.get("department")

        if password != confirm_password:
            messages.warning(request, "Girdiğin şifreler uyuşmuyor, gözlerini bir baktır kanka 😂")
            return render(request, "accounts/register.html")
        
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Bu kullanıcı adı alınmış, başka bir şey bul.")
            return render(request, "accounts/register.html")

        if User.objects.filter(email=email).exists():
            messages.warning(request, "Bu mail adresi zaten kayıtlı.")
            return render(request, "accounts/register.html")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        
        user.university = university
        user.department = department
        user.save() 

        login(request, user)
        messages.success(request, "Kayıt tamam, içeri alındın.")
        return redirect("dashboard/home")

    return render(request, "accounts/register.html")

def logout_view(request):
    logout(request)
    messages.info(request, "Çıkış yapıldı, kendine iyi bak.")
    return redirect('accounts/login')

@login_required(login_url='accounts/login')
def profile_view(request):
    return render(request, 'accounts/profile.html')

@login_required(login_url='accounts/login')
def profile_duzenle_view(request):
    user = request.user
    if request.method == "POST":
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.university = request.POST.get("university")
        user.department = request.POST.get("department")
        user.bio = request.POST.get("bio")
        
        if request.FILES.get('profile_image'):
            user.profile_image = request.FILES.get('profile_image')
            
        user.save()
        messages.success(request, "Profil güncellendi.")
        return redirect('accounts/profile')
        
    return render(request, 'accounts/profile_duzenle.html')