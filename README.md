🚀 Gelişim Kapsül Projesi

Gelişim Kapsül Projesi, üniversite öğrencileri ve akademisyenler için geliştirilmiş; ders materyallerine (PDF, Video) kolayca erişim sağlayan, Django altyapısı üzerine kurulu bir eğitim platformu prototipidir.

🎯 Proje Amacı

Öğrencilerin dağınık kaynaklar yerine tek bir platform üzerinden ders notlarına erişmesini sağlamak ve eğitimde fırsat eşitliğini desteklemektir.

🛠️ Kullanılan Teknolojiler

Backend: Python, Django

Frontend: HTML5, CSS3, Bootstrap 5

Veritabanı: SQLite

👥 Takım Üyeleri (Zamansızlar Takımı)

Proje Lideri & Materials App: Ali Ceylan

Accounts App: Hasan Hüseyin Keskin

Dashboard App & Base Templates: Arda Irmak

Courses App: Edanur Bozlar

📂 Kurulum

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

Repoyu klonlayın:

git clone [https://github.com/Aliceylan11/GelisimKapsul.git](https://github.com/Aliceylan11/GelisimKapsul.git)


Sanal ortamı kurun ve aktif edin (Windows için):

python -m venv venv
venv\Scripts\activate


Gerekli paketleri yükleyin:

pip install django


Veritabanı tablolarını oluşturun:

python manage.py migrate


Projeyi çalıştırın:

python manage.py runserver


⚡ Geliştirici Kılavuzu & GitHub Kuralları (ÖNEMLİ)

Projenin sağlığı ve kodların karışmaması için tüm ekip üyeleri aşağıdaki kurallara uymalıdır.

1. ASLA main Dalında Çalışmayın!

Ana dal (main), sadece çalışan ve hatasız kodları barındırır. Herkes kendi geliştirmesi için yeni bir dal (branch) açmalıdır.

Yeni Dal Oluşturma:

git checkout -b isim-gorev-adi
# Örnek: git checkout -b hasan-login-formu


2. Kodları Yükleme (Push)

İşiniz bittiğinde kodları GitHub'a göndermek için:

Değişiklikleri Kaydet:

git add .
git commit -m "Yaptığınız işi anlatan kısa mesaj"


Kendi Dalınıza Gönderin (Main'e Değil!):

git push origin isim-gorev-adi


3. Kodları Birleştirme (Pull Request)

Kodlarınızı yükledikten sonra GitHub sayfasına gidin ve "Compare & Pull Request" butonuna tıklayarak Proje Liderine birleştirme isteği gönderin.

4. Güncellemeleri Alma (Pull)

Başkalarının yaptığı değişiklikleri kendi bilgisayarınıza çekmek için önce main dalına geçin, sonra çekin:

git checkout main
git pull origin main


(Not: git pull yaptıktan sonra her zaman python manage.py migrate komutunu çalıştırın!)
