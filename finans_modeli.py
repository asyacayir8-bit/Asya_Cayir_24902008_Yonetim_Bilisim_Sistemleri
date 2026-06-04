class Islem:
    """
    Kişisel finans işlemlerini temsil eden sınıf (OOP).
    """
    def __init__(self, id: int, tutar: float, tarih: str, aciklama: str, tip: str):
        """
        İşlem nesnesini başlatır.

        id: int -> Benzersiz işlem kimliği
        tutar: float -> İşlem tutarı
        tarih: str -> YYYY-MM-DD formatında işlem tarihi
        aciklama: str -> İşlem açıklaması
        tip: str -> 'gelir' veya 'gider'
        """
        self.id = id
        self.tutar = tutar
        self.tarih = tarih
        self.aciklama = aciklama
        self.tip = tip

    def __str__(self) -> str:
        """
        Nesnenin okunabilir string temsilini döndürür.
        """
        tip_str = "Gelir" if self.tip == 'gelir' else "Gider"
        return f"[ID: {self.id:04d}] {self.tarih} | {tip_str:<5} | Tutar: {self.tutar:10.2f} TL | Açıklama: {self.aciklama}"

    def __repr__(self) -> str:
        return f"Islem(id={self.id}, tutar={self.tutar}, tarih='{self.tarih}', aciklama='{self.aciklama}', tip='{self.tip}')"
