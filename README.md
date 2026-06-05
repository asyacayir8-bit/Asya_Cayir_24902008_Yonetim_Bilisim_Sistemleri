# KİŞİSEL FİNANS VE HARCAMA TAKİP SİSTEMİ
### ÖĞRENCİ BİLGİLERİ
- **Adı Soyadı:** Asya Çayır
- **Öğrenci Numarası:** 24902008
- **Bölümü:** Yönetim Bilişim Sistemleri (YBS)
---

## 1. PROJE TANIMI VE AMACI: 
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

<img width="1024" height="1024" alt="ekran_goruntusu_analiz" src="https://github.com/user-attachments/assets/0ec71ac4-f5b6-48ea-8906-6137fc50a1c4" />
<img width="1486" height="884" alt="aylik_analiz_cizgi" src="https://github.com/user-attachments/assets/fa3dc23a-3ac0-4c3f-b886-909bca8b8289" />
<img width="1186" height="883" alt="gelir_gider_toplam_bar" src="https://github.com/user-attachments/assets/7f8d53fe-5b95-47af-a1f2-f00d06346202" />
<img width="980" height="1034" alt="gelir_gider_pasta" src="https://github.com/user-attachments/assets/2411b2a3-dce7-458a-9b5d-5e9c5e175481" />
<img width="1024" height="1024" alt="ekran_goruntusu_menu" src="https://github.com/user-attachments/assets/6b831fc0-1220-4b04-a3f2-f117b6d436c6" />
<img width="1024" height="1024" alt="ekran_goruntusu_listele" src="https://github.com/user-attachments/assets/2d123b24-214c-41d8-8684-269ad597c484" />



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
