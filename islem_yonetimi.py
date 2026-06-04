from finans_modeli import Islem
from utils import yeni_id_olustur, tarih_kontrol, sayi_kontrol

def gelir_ekle(gelirler, giderler=None):
    """
    Kullanıcıdan alınan bilgileri doğrulayarak yeni bir gelir kaydı oluşturur ve listeye ekler.

    gelirler: list -> Gelir nesnelerinin bulunduğu liste
    giderler: list (opsiyonel) -> Gider listesi (global benzersiz ID oluşturmak için kullanılır)
    """
    print("\n=== YENİ GELİR EKLEME ===")
    
    # 1. Tutar Alımı ve Validasyonu
    while True:
        tutar_str = input("Gelir Tutarını Giriniz (Örn: 12500.75): ").strip()
        if sayi_kontrol(tutar_str):
            tutar = float(tutar_str)
            if tutar > 0:
                break
            else:
                print("Hata: Tutar 0'dan büyük olmalıdır.")
        else:
            print("Hata: Geçersiz sayısal değer girdiniz. Lütfen tekrar deneyin.")
            
    # 2. Tarih Alımı ve Validasyonu
    while True:
        tarih = input("Tarih Giriniz (Format: YYYY-MM-DD, Örn: 2026-06-04): ").strip()
        if tarih_kontrol(tarih):
            break
        else:
            print("Hata: Geçersiz tarih formatı veya geçersiz gün/ay. Lütfen YYYY-MM-DD şeklinde girin.")
            
    # 3. Açıklama Alımı
    aciklama = input("Gelir Açıklaması Giriniz: ").strip()
    if not aciklama:
        aciklama = "Belirtilmemiş Gelir"
        
    # Benzersiz ID oluşturulması (Gider listesi verilmişse ikisini birleştirerek kontrol eder)
    referans_listesi = gelirler
    if giderler is not None:
        referans_listesi = gelirler + giderler
        
    yeni_id = yeni_id_olustur(referans_listesi)
    
    # Gelir nesnesinin oluşturulup listeye eklenmesi
    yeni_gelir = Islem(id=yeni_id, tutar=tutar, tarih=tarih, aciklama=aciklama, tip='gelir')
    gelirler.append(yeni_gelir)
    print(f"\n[Başarılı] Gelir kaydı başarıyla eklendi:\n{yeni_gelir}")

def gider_ekle(giderler, gelirler=None):
    """
    Kullanıcıdan alınan bilgileri doğrulayarak yeni bir gider kaydı oluşturur ve listeye ekler.

    giderler: list -> Gider nesnelerinin bulunduğu liste
    gelirler: list (opsiyonel) -> Gelir listesi (global benzersiz ID oluşturmak için kullanılır)
    """
    print("\n=== YENİ GIDER EKLEME ===")
    
    # 1. Tutar Alımı ve Validasyonu
    while True:
        tutar_str = input("Gider Tutarını Giriniz (Örn: 150.00): ").strip()
        if sayi_kontrol(tutar_str):
            tutar = float(tutar_str)
            if tutar > 0:
                break
            else:
                print("Hata: Tutar 0'dan büyük olmalıdır.")
        else:
            print("Hata: Geçersiz sayısal değer girdiniz. Lütfen tekrar deneyin.")
            
    # 2. Tarih Alımı ve Validasyonu
    while True:
        tarih = input("Tarih Giriniz (Format: YYYY-MM-DD, Örn: 2026-06-04): ").strip()
        if tarih_kontrol(tarih):
            break
        else:
            print("Hata: Geçersiz tarih formatı veya geçersiz gün/ay. Lütfen YYYY-MM-DD şeklinde girin.")
            
    # 3. Açıklama Alımı
    aciklama = input("Gider Açıklaması Giriniz: ").strip()
    if not aciklama:
        aciklama = "Belirtilmemiş Gider"
        
    # Benzersiz ID oluşturulması (Gelir listesi verilmişse ikisini birleştirerek kontrol eder)
    referans_listesi = giderler
    if gelirler is not None:
        referans_listesi = giderler + gelirler
        
    yeni_id = yeni_id_olustur(referans_listesi)
    
    # Gider nesnesinin oluşturulup listeye eklenmesi
    yeni_gider = Islem(id=yeni_id, tutar=tutar, tarih=tarih, aciklama=aciklama, tip='gider')
    giderler.append(yeni_gider)
    print(f"\n[Başarılı] Gider kaydı başarıyla eklendi:\n{yeni_gider}")

def islemleri_listele(gelirler, giderler):
    """
    Tüm gelir ve gider kayıtlarını kronolojik olarak (tarihe göre) düzenli bir formatta ekrana yazdırır.
    """
    print("\n" + "-"*75)
    print(f"{'KAYITLI TÜM FİNANSAL İŞLEMLERİN LİSTESİ':^75}")
    print("-"*75)
    
    tum_islemler = gelirler + giderler
    # Tarihe göre sıralama (En eskiden en yeniye)
    tum_islemler.sort(key=lambda x: x.tarih)
    
    if not tum_islemler:
        print(f"{'Henüz kayıtlı bir gelir veya gider işlemi bulunmamaktadır.':^75}")
        print("-"*75)
        return
        
    # Tablo Başlığı
    print(f"{'ID':<6} | {'Tarih':<10} | {'Tip':<5} | {'Tutar (TL)':>12} | {'Açıklama':<30}")
    print("-"*75)
    for islem in tum_islemler:
        tip_str = "Gelir" if islem.tip == 'gelir' else "Gider"
        print(f"{islem.id:04d}   | {islem.tarih} | {tip_str:<5} | {islem.tutar:12.2f} | {islem.aciklama:<30}")
    print("-"*75)

def islem_sil(gelirler, giderler, id):
    """
    Verilen ID'ye sahip işlemi bularak ilgili listeden siler.
    """
    # Girdi tipini int formatına dönüştürme (hata yönetimi ile)
    try:
        id_int = int(id)
    except (ValueError, TypeError):
        print("Hata: Geçersiz ID formatı! ID tam sayı olmalıdır.")
        return False

    silindi = False
    
    # Gelirler listesinden arama ve silme
    for islem in gelirler:
        if islem.id == id_int:
            gelirler.remove(islem)
            silindi = True
            print(f"\n[Başarılı] ID: {id_int} olan Gelir işlemi başarıyla silindi.")
            break
            
    # Eğer gelirlerde bulunup silinmediyse giderler listesinde arama ve silme
    if not silindi:
        for islem in giderler:
            if islem.id == id_int:
                giderler.remove(islem)
                silindi = True
                print(f"\n[Başarılı] ID: {id_int} olan Gider işlemi başarıyla silindi.")
                break
                
    if not silindi:
        print(f"\nHata: ID: {id_int} değerine sahip herhangi bir işlem bulunamadı.")
        return False
        
    return True
