# Mini bir "ürün veritabanı" yöneteceksiniz.
# Ürünler dict içinde tutulacak.
# Ürün formatı: {"ad": ..., "fiyat": ..., "stok": ...}

# Seviye: Zor

urunler = {}

def urun_ekle(kod, ad, fiyat, stok):
    # BURAYI TAMAMLAYIN:
    # kod bir key, içi dict olsun.
    pass

def stok_guncelle(kod, adet):
    # Eğer ürün yoksa hata mesajı
    # Eğer stok yetersizse uyarı
    # Yeterliyse stok azaltın
    pass

def listele():
    # Tüm ürünleri yazdırın
    pass

# Test
urun_ekle(101, "Kalem", 10, 100)
urun_ekle(102, "Defter", 25, 50)
stok_guncelle(101, 20)
listele()
