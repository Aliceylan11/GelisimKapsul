# 🚀 Gelişim Kapsül

**Gelişim Kapsül**, üniversite öğrencileri ve akademisyenler için özel olarak tasarlanmış; ders materyallerine (PDF, Video) tek bir merkezden, hızlı ve kolay erişim sağlayan modern bir eğitim platformu prototipidir.

---

## 🎯 Proje Vizyonu ve Amacı

Günümüzde öğrencilerin en büyük problemlerinden biri, ders kaynaklarının farklı platformlara dağılmış olmasıdır. Gelişim Kapsül, bu dağınıklığı ortadan kaldırmayı hedefler.

* **Merkezi Erişim:** Tüm ders notları, videolar ve kaynaklar tek bir çatı altında toplanır.
* **Fırsat Eşitliği:** Kaynaklara erişimi kolaylaştırarak her öğrencinin bilgiye eşit şartlarda ulaşmasını destekler.
* **Kullanıcı Dostu Deneyim:** Karmaşık sistemler yerine, sade ve odaklanmış bir arayüz sunar.

---


## 👥 Proje Ekibi (Zamansızlar Takımı)

Projenin başarısı, görevleri net bir şekilde ayrılmış, disiplinli bir takım çalışmasına dayanmaktadır.

| Üye Adı | Rol | Sorumluluklar |
| :--- | :--- | :--- |
| **Ali Ceylan** | Proje Lideri & Materials App | Proje mimarisinin kurulması, GitHub yönetimi, Materyal yükleme ve listeleme modüllerinin geliştirilmesi. |
| **Arda Irmak** | Dashboard App & UI/UX | Ana sayfa tasarımı, Navbar/Footer entegrasyonu ve genel görsel şablonun (Base Template) oluşturulması. |
| **Hasan Hüseyin Keskin** | Accounts App | Kullanıcı giriş, kayıt ve profil yönetimi arayüzlerinin tasarlanması. |
| **Edanur Bozlar** | Courses App | Derslerin kategorize edilmesi ve ders listeleme ekranlarının geliştirilmesi. |

---

## 🛠️ Teknik Altyapı ve Teknoloji Yığını

Proje, modern web standartlarına uygun, ölçeklenebilir ve güvenli bir mimari üzerine inşa edilmiştir.

| Katman | Teknoloji | Açıklama |
| :--- | :--- | :--- |
| **Backend (Arka Uç)** | Python & Django | Güçlü MVT (Model-View-Template) mimarisi ile güvenli ve hızlı veri yönetimi. |
| **Frontend (Ön Yüz)** | HTML5, CSS3, Bootstrap 5 | Mobil uyumlu (Responsive), modern ve estetik kullanıcı arayüzü. |
| **Veritabanı** | SQLite | Prototip aşamasında hızlı kurulum ve taşınabilirlik için tercih edilmiştir. |
| **Versiyon Kontrol** | Git & GitHub | Takım içi senkronizasyon ve kod güvenliği. |

---

## 📂 Kurulum Kılavuzu

Projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları sırasıyla uygulayınız.

### 1. Projeyi İndirin
Terminal veya Komut İstemi'ni açarak projeyi klonlayın:
```bash
git clone [https://github.com/Aliceylan11/GelisimKapsul.git](https://github.com/Aliceylan11/GelisimKapsul.git)

🔄 Çalışma Adımları
Mevcut Branch'leri Listeleme:
git branch

Yeni Branch Oluşturma ve Geçiş Yapma:
git checkout -b isim-gorev-adi
# Örnek: git checkout -b arda-navbar-tasarimi

Farklı Bir Branch'e Geçiş Yapma:
git checkout branch-adi

1. Yeni Bir Göreve Başlarken:
git checkout -b isim-gorev-adi
# Örnek: git checkout -b hasan-login-formu

2. Kodları Kaydetme ve Gönderme
git add .
git commit -m "Yapılan işi özetleyen net bir mesaj yazın"
git push origin isim-gorev-adi

3. Birleştirme (Merge) Talebi: GitHub üzerinden "Compare & Pull Request" butonuna tıklayarak Proje Liderine birleştirme isteği gönderin.

4. Güncellemeleri Alma:
git checkout main
git pull origin main
Ardından kendi dalınıza dönüp çalışmaya devam edebilirsiniz:
git checkout kendi-dalim
git merge main

