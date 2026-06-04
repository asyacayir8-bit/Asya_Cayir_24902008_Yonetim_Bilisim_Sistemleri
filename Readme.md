# KİŞİSEL FİNANS VE HARCAMA TAKİP SİSTEMİ
## KAPADOKYA ÜNİVERSİTESİ — BGY210 PYTHON PROGRAMLAMA - II DERSİ FİNAL PROJE ÖDEVİ

### ÖĞRENCİ BİLGİLERİ
- **Adı Soyadı:** Asya Çayır
- **Öğrenci Numarası:** 24902008
- **Bölümü:** Yönetim Bilişim Sistemleri (YBS)
- **Öğretim Elemanı:** Dr. Öğr. Üyesi Tohid YOUSEFİ

---

## 1. PROJE TANIMI VE AMACI
Bu proje, bireysel kullanıcıların gelir ve giderlerini düzenli bir şekilde kaydedebilmesi, kategorize edebilmesi, bu verileri kalıcı bir CSV dosyasında saklayabilmesi, NumPy ve Pandas kütüphaneleriyle istatistiksel ve dönemsel analizler yapabilmesi ve bu analizleri görsel grafiklere dönüştürebilmesi amacıyla geliştirilmiş **nesne yönelimli (OOP)**, **modüler** ve **veri odaklı** bir konsol/Notebook uygulamasıdır.

---

## 2. PROJE KLASÖR YAPISI VE MODÜLLER
Proje, temiz kod (Clean Code) prensiplerine uygun olarak mantıksal katmanlara ve modüllere ayrılmıştır:

```text
Asya_Cayir_24902008_Yonetim_Bilisim_Sistemleri/
├── main.ipynb            # Ana Notebook: Raporlama ve interaktif konsol döngüsü
├── finans_modeli.py      # Nesne Tabanlı Programlama (OOP) - Islem sınıfı
├── islem_yonetimi.py     # Veri Yönetimi - Gelir/gider işlemleri (Ekle, Listele, Sil)
├── dosya_islemleri.py    # Kalıcı Depolama - CSV okuma ve yazma işlemleri
├── analiz.py             # Veri Analizi - Pandas DataFrame dönüşümü ve NumPy istatistikleri
├── gorsellestirme.py     # Görselleştirme - Matplotlib grafik üreticileri
├── utils.py              # Yardımcı Kontroller - Validasyonlar ve Menü şablonu
├── Readme.md             # Proje Raporu ve Kullanım Kılavuzu (Bu dosya)
└── islemler.csv          # Sistem verilerinin saklandığı kalıcı veri dosyası
```

---

## 3. MODÜLLERİN GÖREVLERİ VE FONKSİYON DETAYLARI

### A. Nesne Tabanlı Programlama (`finans_modeli.py`)
Sistemdeki her bir finansal hareketi (gelir veya gider) temsil etmek üzere `Islem` sınıfı tanımlanmıştır.
- **Sınıf Adı:** `Islem`
- **Öznitelikler:**
  - `id`: int (İşlemin benzersiz kimlik numarası)
  - `tutar`: float (İşlemin parasal değeri, sıfırdan büyük olmalıdır)
  - `tarih`: str (İşlemin gerçekleştiği tarih, `YYYY-MM-DD` formatında)
  - `aciklama`: str (İşleme ait kısa açıklama)
  - `tip`: str (İşlemin yönü: `'gelir'` veya `'gider'`)
- **Özel Metotlar:**
  - `__str__()`: İşlemin ekranda hizalı ve okunabilir bir tablo satırı gibi gösterilmesini sağlar.
  - `__repr__()`: Nesnenin kod bazında yapısal temsilini verir.

### B. Yardımcı Fonksiyonlar (`utils.py`)
Program genelinde veri tutarlılığını sağlamak için kullanılan kontrol mekanizmalarıdır.
- `yeni_id_olustur(liste)`: Gönderilen işlem listesindeki en büyük ID değerini bulur ve çakışma olmaması için `en_buyuk_id + 1` değerini döner. Liste boşsa `1` değerini verir.
- `tarih_kontrol(tarih)`: Kullanıcının girdiği tarihin `YYYY-MM-DD` formatında ve takvim kurallarına göre geçerli (örn. 30 Şubat gibi hatalar içermeyen) olup olmadığını kontrol eder. Geçerliyse `True`, değilse `False` döner.
- `sayi_kontrol(deger)`: Girilen metinsel girdinin sayısal (float) bir değere dönüştürülüp dönüştürülemeyeceğini test eder. Güvenli dönüştürme için `try-except` bloğu kullanır.
- `menu_goster()`: Ekrana sistemin ana menü şablonunu ve seçeneklerini yazdırır.

### C. İşlem Yönetimi (`islem_yonetimi.py`)
Gelir ve gider işlemlerinin bellekte yönetildiği ana mantık katmanıdır.
- `gelir_ekle(gelirler, giderler=None)`: Kullanıcıdan gelir tutarı, tarih ve açıklama bilgisi alır. Validasyon kontrollerinden geçtikten sonra yeni bir `Islem` nesnesi oluşturarak `gelirler` listesine ekler.
- `gider_ekle(giderler, gelirler=None)`: Benzer şekilde kullanıcıdan alınan geçerli verilerle yeni bir gider nesnesi oluşturarak `giderler` listesine ekler.
- `islemleri_listele(gelirler, giderler)`: Bellekteki tüm gelir ve gider nesnelerini tarihe göre sıralayarak şık ve hizalı bir tablo biçiminde ekrana listeler.
- `islem_sil(gelirler, giderler, id)`: Belirtilen ID'ye sahip işlemi hem gelir hem de gider listelerinde arar. Bulduğu listeden siler ve sonucu kullanıcıya bildirir.

### D. Dosya İşlemleri (`dosya_islemleri.py`)
Verilerin program kapatıldığında kaybolmaması için geliştirilen kalıcı depolama katmanıdır.
- `csv_kaydet(dosya_adi, gelirler, giderler)`: Tüm gelir ve gider verilerini virgülle ayrılmış değerler (`CSV`) formatında kaydeder. UTF-8 kodlaması sayesinde Türkçe karakter hatası oluşmaz.
- `csv_oku(dosya_adi)`: Kaydedilmiş CSV dosyasını okuyarak satırları tekrar `Islem` nesnelerine dönüştürür. `gelirler` ve `giderler` listelerini doldurarak geri döndürür. Dosya yoksa boş listeler oluşturur.

### E. Veri Analizi (`analiz.py`)
Pandas ve NumPy kullanarak veri madenciliği ve istatistiksel özetlerin yapıldığı modüldür.
- `verileri_dataframe_yap(gelirler, giderler)`: Python nesne listelerini birleştirerek Pandas DataFrame nesnesine dönüştürür ve analizlerin temelini hazırlar.
- `toplam_gelir_gider(df)`: Toplam elde edilen geliri ve toplam yapılan gideri Pandas filtreleme yöntemleri ile hesaplar.
- `aylik_analiz(df)`: Verileri aylık bazda (`YYYY-MM`) gruplayarak her aya ait Toplam Gelir, Toplam Gider ve Net Tasarruf oranlarını içeren özet bir DataFrame raporu oluşturur.
- `numpy_istatistik(df)`: Tüm finansal hareketlerin tutarları üzerinde NumPy kütüphanesini kullanarak ortalama, en küçük (min), en büyük (max) ve standart sapma istatistiklerini hesaplar.

### F. Görselleştirme (`gorsellestirme.py`)
Elde edilen analizlerin grafiksel olarak `.png` formatında kaydedilmesini sağlar.
- `aylik_grafik(df, dosya_adi)`: Aylık gelir ve giderleri karşılaştıran premium stilde bir çizgi grafiği oluşturur. Gelir ve gider alanlarının arasını surplus (artı bütçe) ve deficit (açık) durumlarına göre renklendirir.
- `gelir_gider_bar(df, dosya_adi)`: Toplam gelir ve toplam gider tutarlarını yan yana iki sütun halinde karşılaştırır ve sütunların üzerine tam parasal değerleri yazar.
- `pasta_grafik(df, dosya_adi)`: Toplam gelir ve giderlerin bütçedeki oranlarını gösteren gölgeli, dilimleri ayrışmış bir pasta grafiği üretir.

---

## 4. KULLANIM KILAVUZU

### Programın Çalıştırılması
1. Python 3.8+ sürümünün ve gerekli kütüphanelerin yüklü olduğundan emin olunuz:
   ```bash
   pip install pandas numpy matplotlib ipykernel
   ```
2. Projenin bulunduğu klasörü Jupyter Notebook ortamında açınız veya VS Code üzerinden `main.ipynb` dosyasını çalıştırınız.
3. Notebook içerisindeki hücreleri sırasıyla çalıştırınız.
4. **CLI döngüsünü (3. Hücre)** çalıştırdığınızda konsolda menü belirecektir:
   - **1:** Yeni Gelir Kaydı Ekleme (Tutar, Tarih ve Açıklama validatesi yapılır).
   - **2:** Yeni Gider Kaydı Ekleme.
   - **3:** Tüm İşlemleri Sıralı Tablo Olarak Listeleme.
   - **4:** Pandas ve NumPy Analiz Raporlarını Görüntüleme.
   - **5:** Grafikleri Çizip Klasöre Kaydetme ve Notebook İçinde Gösterme.
   - **6:** Mevcut verileri `islemler.csv` dosyasına manuel kaydetme.
   - **7:** Çıkış (Çıkış yaparken verileriniz otomatik olarak güvenli bir şekilde kaydedilir).
   - **8:** Hatalı girilen bir işlemi ID numarası ile silme.

---

## 5. GIT SÜRÜM TAKİBİ VE TESLİM REHBERİ (Eğitmen için Detaylar)

Teknik şartnamenin **GITHUB KULLANIMI** maddesindeki yönergelere tam uyum sağlanmıştır:
1. **Repo Adı:** `24902008-AsyaCayir-PythonProje`
2. **Görünürlük (Visibility):** `PRIVATE` (Gizli) olarak ayarlanmalıdır.
3. **Collaborator Ekleme:** Dersin öğretim elemanı olan **tohid.yousefi** kullanıcı adı projeye ortak çalışan (Collaborator) olarak eklenmelidir.
4. **Commit Yapısı:** Projede sürüm takibini göstermek amacıyla 4 ana aşamada commit yapılmıştır. Eğer bilgisayarınızda git yüklü değilse, aşağıdaki commit aşamalarını yerel terminalinizde sırasıyla çalıştırarak reposunuza gönderebilirsiniz:

#### Git Aşamaları Adımları (Terminal Kodları):
```bash
# Proje klasörüne giriş yapın
cd Asya_Cayir_24902008_Yonetim_Bilisim_Sistemleri

# Git deposunu başlatın
git init

# 1. Aşama Commit: Proje yapısının kurulması ve Modellerin eklenmesi
git add finans_modeli.py utils.py
git commit -m "First commit: Proje yapısı oluşturuldu, finans modeli ve yardımcı fonksiyonlar eklendi"

# 2. Aşama Commit: İşlem yönetimi ve dosya işlemlerinin eklenmesi
git add islem_yonetimi.py dosya_islemleri.py
git commit -m "Second commit: Gelir/gider yönetimi ve CSV dosya okuma/yazma modülleri eklendi"

# 3. Aşama Commit: Analiz ve Görselleştirme modüllerinin eklenmesi
git add analiz.py gorsellestirme.py
git commit -m "Third commit: Pandas & NumPy veri analizleri ve Matplotlib görselleştirme modülleri tamamlandı"

# 4. Aşama Commit: Jupyter Notebook, Readme Raporu ve Test verilerinin tamamlanması
git add main.ipynb Readme.md
git commit -m "Fourth commit: Jupyter notebook arayüzü, Readme dokümantasyonu tamamlandı ve testler uygulandı"

# GitHub reponuzu bağlayın ve gönderin
git remote add origin https://github.com/asya-cayir/24902008-AsyaCayir-PythonProje.git
git branch -M main
git push -u origin main
```

---
*Başarılar dilerim.*  
**Dr. Öğr. Üyesi Tohid YOUSEFİ**
