🚀 Gelişim Kapsül Projesi (LearnHub)

Gelişim Kapsül, üniversite öğrencileri ve akademisyenler için özel olarak tasarlanmış; ders materyallerine (PDF, Video) tek bir merkezden, hızlı ve kolay erişim sağlayan modern bir eğitim platformu prototipidir.

🎯 Proje Vizyonu ve Amacı

Günümüzde öğrencilerin en büyük problemlerinden biri, ders kaynaklarının farklı platformlara dağılmış olmasıdır. Gelişim Kapsül, bu dağınıklığı ortadan kaldırmayı hedefler.

Merkezi Erişim: Tüm ders notları, videolar ve kaynaklar tek bir çatı altında toplanır.

Fırsat Eşitliği: Kaynaklara erişimi kolaylaştırarak her öğrencinin bilgiye eşit şartlarda ulaşmasını destekler.

Kullanıcı Dostu Deneyim: Karmaşık sistemler yerine, sade ve odaklanmış bir arayüz sunar.

🛠️ Teknik Altyapı ve Teknoloji Yığını

Proje, modern web standartlarına uygun, ölçeklenebilir ve güvenli bir mimari üzerine inşa edilmiştir.

Katman

Teknoloji

Açıklama

Backend (Arka Uç)

Python & Django

Güçlü MVT (Model-View-Template) mimarisi ile güvenli ve hızlı veri yönetimi.

Frontend (Ön Yüz)

HTML5, CSS3, Bootstrap 5

Mobil uyumlu (Responsive), modern ve estetik kullanıcı arayüzü.

Veritabanı

SQLite

Prototip aşamasında hızlı kurulum ve taşınabilirlik için tercih edilmiştir.

Versiyon Kontrol

Git & GitHub

Takım içi senkronizasyon ve kod güvenliği.

👥 Proje Ekibi (Zamansızlar Takımı)

Projenin başarısı, görevleri net bir şekilde ayrılmış, disiplinli bir takım çalışmasına dayanmaktadır.

Üye Adı

Rol ve Sorumluluk

Ali Ceylan

Proje Lideri & Materials App Sorumlusu 



 Proje mimarisinin kurulması, GitHub yönetimi, Materyal yükleme ve listeleme modüllerinin geliştirilmesi.

Arda Irmak

Dashboard App & UI/UX Tasarımcısı 



 Ana sayfa tasarımı, Navbar/Footer entegrasyonu ve genel görsel şablonun (Base Template) oluşturulması.

Hasan Hüseyin Keskin

Accounts App Sorumlusu 



 Kullanıcı giriş, kayıt ve profil yönetimi arayüzlerinin tasarlanması.

Edanur Bozlar

Courses App Sorumlusu 



 Derslerin kategorize edilmesi ve ders listeleme ekranlarının geliştirilmesi.

📂 Kurulum Kılavuzu

Projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları sırasıyla uygulayınız:

1. Projeyi İndirin

Terminal veya Komut İstemi'ni açarak projeyi klonlayın:

git clone [https://github.com/Aliceylan11/GelisimKapsul.git](https://github.com/Aliceylan11/GelisimKapsul.git)


2. Sanal Ortamı (Virtual Environment) Kurun

Proje klasörüne girdikten sonra izole bir Python ortamı oluşturun:

cd GelisimKapsul
python -m venv venv


Sanal Ortamı Aktif Edin:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

3. Gerekli Paketleri Yükleyin

Django ve diğer bağımlılıkları kurun:

pip install django


4. Veritabanını Hazırlayın

Gerekli tabloların oluşturulması için migrasyon işlemini yapın:

python manage.py migrate


5. Projeyi Başlatın

Geliştirme sunucusunu ayağa kaldırın:

python manage.py runserver


Tarayıcınızda http://127.0.0.1:8000/ adresine giderek projeyi görüntüleyebilirsiniz.

⚡ Geliştirici Kuralları ve Git Akışı (Workflow)

Proje bütünlüğünü korumak adına tüm ekip üyeleri aşağıdaki kurallara kesinlikle uymalıdır.

🛑 Temel Kurallar

Main Dalı Kutsaldır: main dalına doğrudan kod yüklemesi (push) yapılmamalıdır.

Branch (Dal) Kullanımı: Her yeni özellik veya düzeltme için yeni bir dal açılmalıdır.

🔄 Çalışma Adımları

1. Yeni Bir Göreve Başlarken:
Kendi isminizle veya görevinizle bir dal oluşturun:

git checkout -b isim-gorev-adi
# Örnek: git checkout -b hasan-login-formu


2. Kodları Kaydetme ve Gönderme:
İşiniz bittiğinde değişiklikleri kaydedip kendi dalınıza gönderin:

git add .
git commit -m "Yapılan işi özetleyen net bir mesaj yazın"
git push origin isim-gorev-adi


3. Birleştirme (Merge) Talebi:
GitHub üzerinden "Compare & Pull Request" butonuna tıklayarak Proje Liderine birleştirme isteği gönderin.

4. Güncellemeleri Alma:
Arkadaşlarınızın yaptığı değişiklikleri almak için önce ana dala geçin, sonra çekin:

git checkout main
git pull origin main
# Ardından kendi dalınıza dönüp çalışmaya devam edebilirsiniz:
# git checkout kendi-dalim
# git merge main
