import base64
import hmac
import hashlib
import requests
import json
import random
import os
from django.conf import settings
from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt 
from django.shortcuts import redirect
# Kullanıcı modelini çekiyoruz
from django.contrib.auth import get_user_model
User = get_user_model()

def odeme_sayfasi(request):
    if request.user.user_type in ['student', 'instructor', 'premium']:
        return redirect('material_list')
    # 1. AYARLARI ÇEKİYORUZ
    # Settings.py içindeki değerlerin string olduğundan emin oluyoruz.
    merchant_id = str(settings.PAYTR_MERCHANT_ID)
    merchant_key = str(settings.PAYTR_MERCHANT_KEY).encode()
    merchant_salt = str(settings.PAYTR_MERCHANT_SALT)
    
    # 2. KULLANICI BİLGİLERİ
    email = "test@site.com" 
    user_name = "Ali Ceylan"
    
    if request.user.is_authenticated:
        email = request.user.email
        # İsim boşsa 'Kullanici' yazsın, boş kalmasın
        user_name = request.user.get_full_name() or request.user.username or "Kullanici"

    # Önemli: PayTR'da kuruş ayracı olmaz, integer kuruş gönderilir veya string.
    # Genelde iFrame API için "100" şeklinde 100 TL anlamında kabul görür (yapılandırmaya göre değişir).
    # Biz standart string "100" gönderiyoruz.
    payment_amount = "15500" 
    
    merchant_oid = "SIPARIS" + str(random.randint(100000, 999999))
    user_address = "Gumushane Universitesi" 
    user_phone = "05555555555"
    
    # IP ADRESİ AYARI
    user_ip = request.META.get('REMOTE_ADDR')
    # Localhost IPv6 (::1) veya normal localhost ise rastgele gerçek IP verelim.
    if user_ip == '127.0.0.1' or user_ip == '::1': 
        user_ip = '85.85.85.85'

    # Callback URL
    base_url = "http://127.0.0.1:8000"
    # Araya /materials/ ekliyoruz çünkü urls.py yapın öyle
    merchant_ok_url = base_url + "/materials/odeme-basarili/"
    merchant_fail_url = base_url + "/materials/odeme-hata/"
    # 3. SEPET OLUŞTURMA (HATA BURADAYDI)
    
    # separators=(',', ':') ekleyerek JSON içindeki boşlukları siliyoruz.
    user_basket_list = [['Premium Uyelik', payment_amount, 1]]
    user_basket_json = json.dumps(user_basket_list, separators=(',', ':'))
    user_basket_b64 = base64.b64encode(user_basket_json.encode())
    
    timeout_limit = "30"
    debug_on = "1"
    test_mode = "1" 
    no_installment = "1"
    max_installment = "0"
    currency = "TL"
    
    # 4. TOKEN OLUŞTURMA (HASH ZİNCİRİ)
    # Sıralama çok kritiktir, değiştirmeyin.
    hash_str = (
        merchant_id + 
        user_ip + 
        merchant_oid + 
        email + 
        payment_amount + 
        user_basket_b64.decode() + 
        no_installment + 
        max_installment + 
        currency + 
        test_mode + 
        merchant_salt
    )
    
    paytr_token = hmac.new(
        merchant_key, 
        hash_str.encode(), 
        hashlib.sha256
    ).digest()
    
    paytr_token = base64.b64encode(paytr_token)

    # 5. PAYTR İSTEĞİ
    params = {
        'merchant_id': merchant_id,
        'user_ip': user_ip,
        'merchant_oid': merchant_oid,
        'email': email,
        'payment_amount': payment_amount,
        'paytr_token': paytr_token,
        'user_basket': user_basket_b64.decode(),
        'debug_on': debug_on,
        'no_installment': no_installment,
        'max_installment': max_installment,
        'user_name': user_name,
        'user_address': user_address,
        'user_phone': user_phone,
        'merchant_ok_url': merchant_ok_url,
        'merchant_fail_url': merchant_fail_url,
        'timeout_limit': timeout_limit,
        'currency': currency,
        'test_mode': test_mode
    }

    try:
        result = requests.post('https://www.paytr.com/odeme/api/get-token', data=params)
        res = json.loads(result.text)

        if res['status'] == 'success':
            context = {'iframe_token': res['token']}
            return render(request, 'materials/payment.html', context)
        else:
            # Hata nedenini ekrana basıyoruz
            print("PAYTR HATA DETAYI:", res) # Konsola da yazsın
            return HttpResponse(f"PayTR Bağlantı Hatası: {res['reason']}")
    except Exception as e:
        return HttpResponse(f"Bir hata oluştu: {str(e)}")


# --- CALLBACK FONKSİYONU ---
@csrf_exempt
def callback(request):
    if request.method != 'POST':
        return HttpResponse('')

    post_data = request.POST
    
    # Hash doğrulama
    content = post_data.get('merchant_oid') + \
              settings.PAYTR_MERCHANT_SALT + \
              post_data.get('status') + \
              post_data.get('total_amount')

    stored_hash = base64.b64encode(
        hmac.new(
            str(settings.PAYTR_MERCHANT_KEY).encode(), 
            content.encode(), 
            hashlib.sha256
        ).digest()
    ).decode()

    if stored_hash != post_data.get('hash'):
        return HttpResponse('PAYTR notification failed: bad hash')

    if post_data.get('status') == 'success':
        gelen_email = post_data.get('email')
        try:
            user = User.objects.get(email=gelen_email)
            user.user_type = 'premium'
            user.save()
            print(f"Kullanıcı ({user.username}) statüsü 'premium' yapıldı.")
        except User.DoesNotExist:
            print(f"HATA: {gelen_email} kullanıcısı bulunamadı!")
        except Exception as e:
            print(f"Hata: {str(e)}")
    
    return HttpResponse('OK')