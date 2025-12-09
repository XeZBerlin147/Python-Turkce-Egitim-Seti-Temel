# Mini bir "ürün veritabanı" yöneteceksiniz.
# Ürünler dict içinde tutulacak.
# Ürün formatı: {"ad": ..., "fiyat": ..., "stok": ...}

# Seviye: Zor

urunler = {}

def urun_ekle(kod, ad, fiyat, stok):
    # HATA: Fonksiyon boştu, hiçbir şekilde ürün eklenmiyordu.
    # ÇÖZÜM: kod'u key yapıp ürün bilgilerini dict olarak ekledik.
    urunler[kod] = {
        "ad": ad,
        "fiyat": fiyat,
        "stok": stok
    }
    print(f"{ad} ürünü eklendi.")

def stok_guncelle(kod, adet):
    # HATA: Ürün kontrolü, stok güncelleme ve uyarılar yoktu.
    # ÇÖZÜM: Tüm mantık aşağıdaki gibi uygulandı.

    if kod not in urunler:
        print("Hata: Bu ürün kodu bulunamadı.")
        return
    
    # Ürün varsa:
    if urunler[kod]["stok"] < adet:
        print("Yetersiz stok! Güncelleme yapılamadı.")
        return
    
    urunler[kod]["stok"] -= adet
    print(f"Stok güncellendi. Yeni stok: {urunler[kod]['stok']}")

def listele():
    # HATA: Listeleme fonksiyonunda hiç kod yoktu.
    # ÇÖZÜM: Tüm ürünleri düzgün formatta yazdırdık.

    print("\n--- Ürün Listesi ---")
    for kod, bilgi in urunler.items():
        print(f"Kod: {kod} | Ad: {bilgi['ad']} | Fiyat: {bilgi['fiyat']} | Stok: {bilgi['stok']}")
    print("---------------------\n")

# Test
urun_ekle(101, "Kalem", 10, 100)
urun_ekle(102, "Defter", 25, 50)
stok_guncelle(101, 20)
listele()


# ------------------------------------------------------------
# HATA NEREDEYDİ?
# - Tüm fonksiyonlar boştaydı, "pass" yüzünden hiçbir işlem yapılmıyordu.
# - urun_ekle() ürün eklemiyordu.
# - stok_guncelle() ürün var mı kontrol etmiyordu, stok azaltmıyordu.
# - listele() ürünleri göstermiyordu.

# NEDEN HATALIYDI?
# - Ürün veritabanı mantığı gereği dict yapısı asla boş işlevlerle çalışamaz.
# - Hiçbir işlem yapılmadığı için test çıktıları tamamen yanlış olurdu.

# NASIL DÜZELTTİK?
# ✔ urun_ekle(): Ürünü dict formatında veritabanına ekledik.
# ✔ stok_guncelle(): Ürün kontrolü → stok kontrolü → güncelleme akışı kuruldu.
# ✔ listele(): Tüm ürünleri kullanıcıya okunabilir formatta yazdırdık.

# Sonuç: Kod artık tam çalışan bir mini ürün veritabanı sistemine dönüştü.
# ------------------------------------------------------------
