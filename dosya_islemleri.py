import csv
import os
from finans_modeli import Islem

def csv_kaydet(dosya_adi: str, gelirler: list, giderler: list) -> bool:
    """
    Tüm gelir ve gider verilerini belirtilen CSV dosyasına kaydeder.

    dosya_adi: str -> Kaydedilecek dosyanın adı/yolu
    gelirler: list -> Gelir Islem nesnelerinden oluşan liste
    giderler: list -> Gider Islem nesnelerinden oluşan liste
    """
    try:
        # UTF-8 kodlama kullanarak dosyayı yazma modunda açıyoruz
        with open(dosya_adi, mode='w', newline='', encoding='utf-8') as dosya:
            yazici = csv.writer(dosya)
            # Başlık satırı
            yazici.writerow(['id', 'tutar', 'tarih', 'aciklama', 'tip'])
            
            # Tüm işlemleri sırayla yazıyoruz
            for islem in gelirler + giderler:
                yazici.writerow([islem.id, islem.tutar, islem.tarih, islem.aciklama, islem.tip])
                
        print(f"\n[Başarılı] {len(gelirler) + len(giderler)} adet işlem '{dosya_adi}' dosyasına başarıyla kaydedildi.")
        return True
    except Exception as e:
        print(f"\n[Hata] Dosya kaydedilirken bir hata oluştu: {e}")
        return False

def csv_oku(dosya_adi: str) -> tuple:
    """
    CSV dosyasındaki verileri okuyarak gelir ve gider listelerini oluşturur ve döndürür.

    dosya_adi: str -> Okunacak dosyanın adı/yolu
    Döndürür: tuple (gelirler, giderler) -> Ayrıştırılmış Islem nesneleri listeleri
    """
    gelirler = []
    giderler = []
    
    # Dosya mevcut değilse boş listeler döner
    if not os.path.exists(dosya_adi):
        print(f"\n[Bilgi] '{dosya_adi}' dosyası bulunamadı. Yeni bir veri tabanı oluşturulacak.")
        return gelirler, giderler
        
    try:
        with open(dosya_adi, mode='r', encoding='utf-8') as dosya:
            okuyucu = csv.DictReader(dosya)
            for satir in okuyucu:
                try:
                    # Satırı ayrıştırıp Islem nesnesine dönüştürme (hata yönetimi ile)
                    islem = Islem(
                        id=int(satir['id']),
                        tutar=float(satir['tutar']),
                        tarih=satir['tarih'].strip(),
                        aciklama=satir['aciklama'].strip(),
                        tip=satir['tip'].strip().lower()
                    )
                    
                    if islem.tip == 'gelir':
                        gelirler.append(islem)
                    elif islem.tip == 'gider':
                        giderler.append(islem)
                    else:
                        print(f"[Uyarı] Geçersiz işlem tipi atlandı: '{islem.tip}' (ID: {islem.id})")
                except (ValueError, KeyError) as e:
                    print(f"[Uyarı] Satır ayrıştırma hatası nedeniyle atlandı. Satır: {satir}. Hata: {e}")
                    
        print(f"\n[Başarılı] Veriler '{dosya_adi}' dosyasından yüklendi.")
        print(f"-> Toplam Gelir İşlemi: {len(gelirler)}")
        print(f"-> Toplam Gider İşlemi: {len(giderler)}")
    except Exception as e:
        print(f"\n[Hata] Dosya okunurken beklenmedik bir hata oluştu: {e}")
        
    return gelirler, giderler
