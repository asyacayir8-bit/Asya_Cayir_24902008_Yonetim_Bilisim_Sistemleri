import pandas as pd
import numpy as np

def verileri_dataframe_yap(gelirler: list, giderler: list) -> pd.DataFrame:
    """
    Gelir ve gider listelerini birleştirerek bir Pandas DataFrame yapısına dönüştürür.
    Tarih sütununu datetime tipine çevirir.

    gelirler: list -> Gelir Islem nesneleri listesi
    giderler: list -> Gider Islem nesneleri listesi
    """
    sutunlar = ['id', 'tutar', 'tarih', 'aciklama', 'tip']
    
    # Listeler boşsa sütun yapısı belli ama boş bir DataFrame döner
    if not gelirler and not giderler:
        df = pd.DataFrame(columns=sutunlar)
        df['tarih'] = pd.to_datetime(df['tarih'])
        return df
        
    veri_listesi = []
    for islem in gelirler + giderler:
        veri_listesi.append({
            'id': islem.id,
            'tutar': islem.tutar,
            'tarih': islem.tarih,
            'aciklama': islem.aciklama,
            'tip': islem.tip
        })
        
    df = pd.DataFrame(veri_listesi)
    # Tarih formatını Pandas Datetime yapısına çeviriyoruz
    df['tarih'] = pd.to_datetime(df['tarih'])
    return df

def toplam_gelir_gider(df: pd.DataFrame) -> tuple:
    """
    DataFrame üzerinden toplam gelir ve toplam gider değerlerini hesaplar.

    df: pd.DataFrame -> Analiz edilecek verilerin bulunduğu DataFrame
    Döndürür: tuple -> (toplam_gelir, toplam_gider)
    """
    if df.empty:
        return 0.0, 0.0
        
    toplam_gelir = df[df['tip'] == 'gelir']['tutar'].sum()
    toplam_gider = df[df['tip'] == 'gider']['tutar'].sum()
    
    return float(toplam_gelir), float(toplam_gider)

def aylik_analiz(df: pd.DataFrame) -> pd.DataFrame:
    """
    Verileri tarihe göre gruplayarak aylık bazda özet analiz (gelir, gider, net tasarruf) oluşturur.

    df: pd.DataFrame -> İşlem verileri DataFrame'i
    """
    if df.empty:
        # Boş veri durumunda uygun sütunlarla boş DataFrame döndürür
        return pd.DataFrame(columns=['gelir', 'gider', 'net_tasarruf'])
        
    df_kopya = df.copy()
    # Tarihi YYYY-MM formatında periyot olarak ayarlıyoruz
    df_kopya['ay'] = df_kopya['tarih'].dt.to_period('M')
    
    # Aylık bazda tip (gelir/gider) toplamlarını alıp sütunlara dağıtıyoruz (unstack)
    analiz_df = df_kopya.groupby(['ay', 'tip'])['tutar'].sum().unstack(fill_value=0.0)
    
    # Sütunların varlığından emin oluyoruz
    if 'gelir' not in analiz_df.columns:
        analiz_df['gelir'] = 0.0
    if 'gider' not in analiz_df.columns:
        analiz_df['gider'] = 0.0
        
    # Net tasarrufu (Gelir - Gider) hesaplıyoruz
    analiz_df['net_tasarruf'] = analiz_df['gelir'] - analiz_df['gider']
    
    # İndeksi grafik çizimi ve tablo gösterimi için string formatına dönüştürüyoruz (Örn: "2026-06")
    analiz_df.index = analiz_df.index.astype(str)
    
    # Kolay okunabilirlik için sütunları düzenliyoruz
    analiz_df = analiz_df[['gelir', 'gider', 'net_tasarruf']]
    
    return analiz_df

def numpy_istatistik(df: pd.DataFrame) -> dict:
    """
    NumPy kullanarak tüm işlem tutarları üzerinde temel istatistikleri
    (ortalama, minimum, maksimum ve standart sapma) hesaplar.

    df: pd.DataFrame -> İşlem verileri DataFrame'i
    """
    if df.empty:
        return {
            'ortalama': 0.0,
            'minimum': 0.0,
            'maksimum': 0.0,
            'standart_sapma': 0.0
        }
        
    # Tutarlar sütununu NumPy dizisine (ndarray) dönüştürüyoruz
    tutarlar = df['tutar'].to_numpy()
    
    # NumPy fonksiyonları ile hesaplama yapıyoruz
    istatistikler = {
        'ortalama': float(np.mean(tutarlar)),
        'minimum': float(np.min(tutarlar)),
        'maksimum': float(np.max(tutarlar)),
        'standart_sapma': float(np.std(tutarlar))
    }
    
    return istatistikler
