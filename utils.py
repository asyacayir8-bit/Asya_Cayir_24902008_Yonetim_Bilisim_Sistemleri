from datetime import datetime

def yeni_id_olustur(liste) -> int:
    """
    Verilen listedeki en büyük ID'yi bulup bir artırarak yeni benzersiz ID üretir.
    Liste boşsa 1 değerini döndürür.

    liste: list -> Islem nesnelerinden oluşan liste
    """
    if not liste:
        return 1
    # Liste içindeki her Islem nesnesinin id özniteliğini kontrol eder
    return max(islem.id for islem in liste) + 1

def tarih_kontrol(tarih: str) -> bool:
    """
    Girilen tarihin doğru formatta (YYYY-MM-DD) ve geçerli bir tarih olup olmadığını kontrol eder.

    tarih: str -> Kontrol edilecek tarih dizisi
    """
    try:
        # datetime.strptime ile YYYY-MM-DD formatı kontrol edilir
        datetime.strptime(tarih, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def sayi_kontrol(deger) -> bool:
    """
    Kullanıcıdan alınan değerin sayıya dönüştürülebilir (float/int) olup olmadığını kontrol eder.

    deger: str/any -> Kontrol edilecek değer
    """
    try:
        float(deger)
        return True
    except (ValueError, TypeError):
        return False

def menu_goster():
    """
    Programın ana menüsünü kullanıcıya ekrana yazdırır.
    """
    print("\n" + "="*50)
    print("   KİŞİSEL FİNANS VE HARCAMA TAKİP SİSTEMİ   ")
    print("="*50)
    print("  1. Gelir Ekle")
    print("  2. Gider Ekle")
    print("  3. Listele (Gelir & Gider)")
    print("  4. Analiz Yap (Pandas & NumPy)")
    print("  5. Grafik Göster (Matplotlib)")
    print("  6. CSV Kaydet")
    print("  7. Çıkış")
    print("  8. İşlem Sil (Ekstra)")
    print("="*50)
