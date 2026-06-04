import os
import sys

# Modüllerin doğru import edilebilmesi için geçerli çalışma dizinini sys.path'e ekliyoruz
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from finans_modeli import Islem
from analiz import verileri_dataframe_yap, toplam_gelir_gider, aylik_analiz, numpy_istatistik
from gorsellestirme import aylik_grafik, gelir_gider_bar, pasta_grafik
from dosya_islemleri import csv_kaydet, csv_oku

def run_tests():
    print("=== KİŞİSEL FİNANS PROJESİ INTEGRASYON TESTLERİ BAŞLATILIYOR ===")
    print("="*60)
    
    # 1. Örnek veri oluşturma (OOP Sınıfı Testi)
    gelirler = [
        Islem(id=1, tutar=45000.0, tarih="2026-04-15", aciklama="Maaş Geliri", tip="gelir"),
        Islem(id=2, tutar=15000.0, tarih="2026-04-20", aciklama="Freelance Proje", tip="gelir"),
        Islem(id=3, tutar=48000.0, tarih="2026-05-15", aciklama="Maaş Geliri", tip="gelir"),
        Islem(id=4, tutar=8000.0, tarih="2026-05-25", aciklama="Yatırım Temettü", tip="gelir"),
        Islem(id=5, tutar=50000.0, tarih="2026-06-15", aciklama="Maaş Geliri", tip="gelir"),
        Islem(id=6, tutar=12000.0, tarih="2026-06-18", aciklama="E-Ticaret Satışı", tip="gelir")
    ]

    giderler = [
        Islem(id=7, tutar=12000.0, tarih="2026-04-18", aciklama="Kira Ödemesi", tip="gider"),
        Islem(id=8, tutar=4500.0, tarih="2026-04-22", aciklama="Market Alışverişi", tip="gider"),
        Islem(id=9, tutar=2000.0, tarih="2026-04-28", aciklama="Fatura Ödemeleri", tip="gider"),
        Islem(id=10, tutar=12000.0, tarih="2026-05-18", aciklama="Kira Ödemesi", tip="gider"),
        Islem(id=11, tutar=6500.0, tarih="2026-05-20", aciklama="Dışarıda Yemek", tip="gider"),
        Islem(id=12, tutar=3800.0, tarih="2026-05-30", aciklama="Ulaşım & Yakıt", tip="gider"),
        Islem(id=13, tutar=14000.0, tarih="2026-06-18", aciklama="Kira Ödemesi", tip="gider"),
        Islem(id=14, tutar=7200.0, tarih="2026-06-22", aciklama="Market Alışverişi", tip="gider"),
        Islem(id=15, tutar=5000.0, tarih="2026-06-25", aciklama="Eğlence & Sosyal", tip="gider")
    ]
    print("[1/8] OOP Islem Sınıfı Testi: BAŞARILI (Nesneler hatasız oluşturuldu).")
    
    # 2. CSV Kaydetme Testi
    csv_dosya = "islemler.csv"
    success_save = csv_kaydet(csv_dosya, gelirler, giderler)
    assert success_save, "CSV Kaydedilemedi!"
    print("[2/8] CSV Yazma Testi: BAŞARILI (islemler.csv oluşturuldu).")
    
    # 3. CSV Okuma Testi
    read_gelirler, read_giderler = csv_oku(csv_dosya)
    assert len(read_gelirler) == len(gelirler), "Okunan gelir listesi boyutu uyuşmuyor!"
    assert len(read_giderler) == len(giderler), "Okunan gider listesi boyutu uyuşmuyor!"
    print("[3/8] CSV Okuma ve Nesneye Çevirme Testi: BAŞARILI.")
    
    # 4. Pandas DataFrame Testi
    df = verileri_dataframe_yap(read_gelirler, read_giderler)
    assert not df.empty, "DataFrame boş oluşturuldu!"
    assert len(df) == len(gelirler) + len(giderler), "DataFrame satır sayısı uyuşmuyor!"
    print("[4/8] Pandas DataFrame Dönüşümü Testi: BAŞARILI.")
    
    # 5. Toplam Gelir Gider Testi
    t_gelir, t_gider = toplam_gelir_gider(df)
    assert t_gelir == 178000.0, f"Toplam gelir yanlış hesaplandı: {t_gelir}"
    assert t_gider == 67000.0, f"Toplam gider yanlış hesaplandı: {t_gider}"
    print(f"[5/8] Toplam Gelir/Gider Hesabı: BAŞARILI (Gelir: {t_gelir} TL, Gider: {t_gider} TL).")
    
    # 6. Aylık Analiz Testi
    aylik_df = aylik_analiz(df)
    assert 'net_tasarruf' in aylik_df.columns, "Aylık analiz net_tasarruf sütununu içermiyor!"
    print("[6/8] Pandas Aylık Özet Gruplama Testi: BAŞARILI.")
    
    # 7. NumPy İstatistik Testi
    ist = numpy_istatistik(df)
    assert ist['ortalama'] > 0, "Ortalama sıfır çıktı!"
    assert ist['minimum'] == 2000.0, f"Min değer yanlış: {ist['minimum']}"
    assert ist['maksimum'] == 50000.0, f"Max değer yanlış: {ist['maksimum']}"
    print("[7/8] NumPy İstatistik Testi: BAŞARILI (Ortalama, Min, Max, Standart Sapma hesaplandı).")
    
    # 8. Grafik Oluşturma Testi
    aylik_grafik(df, "aylik_analiz_cizgi.png")
    gelir_gider_bar(df, "gelir_gider_toplam_bar.png")
    pasta_grafik(df, "gelir_gider_pasta.png")
    
    assert os.path.exists("aylik_analiz_cizgi.png"), "Aylık çizgi grafik dosyası oluşturulamadı!"
    assert os.path.exists("gelir_gider_toplam_bar.png"), "Toplam bar grafik dosyası oluşturulamadı!"
    assert os.path.exists("gelir_gider_pasta.png"), "Pasta grafik dosyası oluşturulamadı!"
    print("[8/8] Matplotlib Grafik Çıktıları Üretim Testi: BAŞARILI (.png dosyaları oluşturuldu).")
    
    print("="*60)
    print("=== TÜM ENTEGRASYON VE DOĞRULAMA TESTLERİ BAŞARIYLA TAMAMLANDI ===")
    print("="*60)

if __name__ == "__main__":
    run_tests()
