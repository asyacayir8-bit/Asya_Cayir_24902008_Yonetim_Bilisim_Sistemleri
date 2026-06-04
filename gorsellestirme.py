import matplotlib.pyplot as plt
import pandas as pd
from analiz import aylik_analiz, toplam_gelir_gider

# Grafiklerin genel estetik ayarlarını yapıyoruz
plt.rcParams['figure.facecolor'] = '#f8f9fa'      # Arka plan rengi (premium açık gri)
plt.rcParams['axes.facecolor'] = '#ffffff'        # Grafik eksen içi arka planı (beyaz)
plt.rcParams['font.family'] = 'sans-serif'        # Modern font ailesi
plt.rcParams['font.sans-serif'] = ['DejaVu Sans', 'Arial', 'Helvetica']

def aylik_grafik(df: pd.DataFrame, dosya_adi: str = "aylik_analiz_cizgi.png"):
    """
    Aylık gelir ve giderleri karşılaştıran premium çizgi grafiği oluşturur ve kaydeder.

    df: pd.DataFrame -> İşlem verileri DataFrame'i
    dosya_adi: str -> Grafiğin kaydedileceği dosya adı
    """
    # Veri setinde 'tip' sütunu varsa aylık analiz fonksiyonu ile gruplama yapılır
    if 'tip' in df.columns:
        aylik_df = aylik_analiz(df)
    else:
        aylik_df = df

    plt.figure(figsize=(10, 6))
    
    # Veri olmama durumu kontrolü
    if aylik_df.empty or (aylik_df['gelir'].sum() == 0 and aylik_df['gider'].sum() == 0):
        plt.text(0.5, 0.5, "Çizgi Grafiği İçin Kayıtlı Veri Bulunmamaktadır", 
                 horizontalalignment='center', verticalalignment='center', fontsize=14, color='gray')
        plt.title("Aylık Gelir ve Gider Karşılaştırması", fontsize=14, fontweight='bold', pad=15)
        plt.grid(True, linestyle='--', alpha=0.3)
        plt.savefig(dosya_adi, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"[Grafik] Kayıtlı veri bulunmadığı için boş çizgi grafiği kaydedildi: {dosya_adi}")
        return

    # Çizgilerin çizilmesi
    plt.plot(aylik_df.index, aylik_df['gelir'], marker='o', linewidth=3, color='#2ec4b6', label='Aylık Gelir')
    plt.plot(aylik_df.index, aylik_df['gider'], marker='s', linewidth=3, color='#e63946', label='Aylık Gider')
    
    # Gelirin giderden fazla olduğu bölgeleri açık turkuaz, ekside olduğu bölgeleri açık kırmızı gölgeleme
    plt.fill_between(aylik_df.index, aylik_df['gelir'], aylik_df['gider'], 
                     where=(aylik_df['gelir'] >= aylik_df['gider']), 
                     interpolate=True, color='#2ec4b6', alpha=0.15)
    plt.fill_between(aylik_df.index, aylik_df['gelir'], aylik_df['gider'], 
                     where=(aylik_df['gelir'] < aylik_df['gider']), 
                     interpolate=True, color='#e63946', alpha=0.15)
    
    # Detaylar ve Başlıklar
    plt.title("Aylık Gelir ve Gider Karşılaştırması", fontsize=14, fontweight='bold', pad=15)
    plt.xlabel("Dönem (Yıl-Ay)", fontsize=11, labelpad=10)
    plt.ylabel("Tutar (TL)", fontsize=11, labelpad=10)
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(frameon=True, facecolor='#ffffff', edgecolor='#e2e8f0', shadow=False)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.savefig(dosya_adi, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"[Grafik] Aylık karşılaştırma çizgi grafiği başarıyla kaydedildi: {dosya_adi}")

def gelir_gider_bar(df: pd.DataFrame, dosya_adi: str = "gelir_gider_toplam_bar.png"):
    """
    Toplam gelir ve gider değerlerini karşılaştıran sütun grafiği oluşturur ve kaydeder.

    df: pd.DataFrame -> İşlem verileri DataFrame'i
    dosya_adi: str -> Grafiğin kaydedileceği dosya adı
    """
    if 'tip' in df.columns:
        gelir, gider = toplam_gelir_gider(df)
    else:
        gelir = df['gelir'].sum() if 'gelir' in df.columns else 0.0
        gider = df['gider'].sum() if 'gider' in df.columns else 0.0

    plt.figure(figsize=(8, 6))
    
    # Veri olmama durumu kontrolü
    if gelir == 0 and gider == 0:
        plt.text(0.5, 0.5, "Bar Grafiği İçin Kayıtlı Veri Bulunmamaktadır", 
                 horizontalalignment='center', verticalalignment='center', fontsize=14, color='gray')
        plt.title("Toplam Gelir ve Gider Karşılaştırması", fontsize=14, fontweight='bold', pad=15)
        plt.savefig(dosya_adi, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"[Grafik] Kayıtlı veri bulunmadığı için boş bar grafiği kaydedildi: {dosya_adi}")
        return

    kategoriler = ['Toplam Gelir', 'Toplam Gider']
    degerler = [gelir, gider]
    renkler = ['#2ec4b6', '#e63946']
    
    # Sütunları çiziyoruz
    sutunlar = plt.bar(kategoriler, degerler, color=renkler, width=0.45, edgecolor='#1a202c', linewidth=0.8)
    
    # Her sütunun üstüne değeri formatlı yazıyoruz
    for sutun in sutunlar:
        yukseklik = sutun.get_height()
        plt.annotate(f'{yukseklik:,.2f} TL',
                    xy=(sutun.get_x() + sutun.get_width() / 2, yukseklik),
                    xytext=(0, 5),  # 5 piksel dikey ofset
                    textcoords="offset points",
                    ha='center', va='bottom', fontweight='bold', color='#2d3748')
                    
    plt.title("Toplam Gelir ve Gider Karşılaştırması", fontsize=14, fontweight='bold', pad=15)
    plt.ylabel("Toplam Tutar (TL)", fontsize=11, labelpad=10)
    plt.grid(True, axis='y', linestyle='--', alpha=0.5)
    plt.ylim(0, max(gelir, gider) * 1.15) # Üst sınırda yüzde 15 pay bırakıyoruz ki sayılar sığsın
    plt.tight_layout()
    
    plt.savefig(dosya_adi, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"[Grafik] Toplam karşılaştırma bar grafiği başarıyla kaydedildi: {dosya_adi}")

def pasta_grafik(df: pd.DataFrame, dosya_adi: str = "gelir_gider_pasta.png"):
    """
    Gelir ve gider oranlarını gösteren pasta grafiği oluşturur ve kaydeder.

    df: pd.DataFrame -> İşlem verileri DataFrame'i
    dosya_adi: str -> Grafiğin kaydedileceği dosya adı
    """
    if 'tip' in df.columns:
        gelir, gider = toplam_gelir_gider(df)
    else:
        gelir = df['gelir'].sum() if 'gelir' in df.columns else 0.0
        gider = df['gider'].sum() if 'gider' in df.columns else 0.0

    plt.figure(figsize=(7, 7))
    
    # Veri olmama durumu kontrolü
    if gelir == 0 and gider == 0:
        plt.text(0.5, 0.5, "Pasta Grafiği İçin Kayıtlı Veri Bulunmamaktadır", 
                 horizontalalignment='center', verticalalignment='center', fontsize=14, color='gray')
        plt.title("Gelir ve Gider Dağılım Oranı", fontsize=14, fontweight='bold', pad=15)
        plt.savefig(dosya_adi, dpi=150, bbox_inches='tight')
        plt.close()
        print(f"[Grafik] Kayıtlı veri bulunmadığı için boş pasta grafiği kaydedildi: {dosya_adi}")
        return

    etiketler = ['Gelir', 'Gider']
    degerler = [gelir, gider]
    renkler = ['#2ec4b6', '#e63946']
    
    # Eğer her iki değer de pozitifse hafif ayrıştırma (explode) efekti ekliyoruz
    dilim_ayrimi = (0.05, 0) if gelir > 0 and gider > 0 else (0, 0)
    
    # Pasta dilimlerini çiziyoruz
    plt.pie(degerler, explode=dilim_ayrimi, labels=etiketler, colors=renkler,
            autopct='%1.1f%%', shadow=True, startangle=140,
            textprops={'fontsize': 12, 'fontweight': 'bold', 'color': '#2d3748'},
            wedgeprops={'edgecolor': '#ffffff', 'linewidth': 1.5})
            
    plt.title("Gelir ve Gider Dağılım Oranı", fontsize=14, fontweight='bold', pad=15)
    plt.tight_layout()
    
    plt.savefig(dosya_adi, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"[Grafik] Oran dağılımı pasta grafiği başarıyla kaydedildi: {dosya_adi}")
