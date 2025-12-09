# Bu denemede size Python kod iskeleti vereceğiz.
# Listeye eleman ekleme / silme işlemlerini sizin tamamlamanız gerekiyor.

# Seviye: Orta-Zor

sehirler = []

def ekle(sehir):
    # HATA: Fonksiyon iskeleti boş bırakılmıştı, 'pass' nedeniyle hiçbir işlem yapılmıyordu.
    # ÇÖZÜM: sehir'i listeye ekledik ve bilgi mesajı yazdırdık.
    sehirler.append(sehir)
    print(sehir, "eklendi.")

def sil(sehir):
    # HATA: Bu fonksiyon da boş bırakılmıştı, şehir listede olsa bile silinmiyordu.
    # ÇÖZÜM: Önce şehir listede mi kontrol ettik, varsa sildik yoksa mesaj verdik.
    if sehir in sehirler:
        sehirler.remove(sehir)
        print(sehir, "silindi.")
    else:
        print(sehir, "bulunamadı.")

def listele():
    print("Şehir Listesi:", sehirler)

# Test:
ekle("Ankara")
ekle("İzmir")
sil("Konya")
sil("İzmir")
listele()

# Beklenen çıktı:
# Şehir Listesi: ['Ankara']


# ------------------------------------------------------------
# HATA NEREDEYDİ?
# - 'ekle' ve 'sil' fonksiyonları tamamen boştaydı (pass kullanılmıştı).
# - Liste üzerinde hiçbir işlem yapılmadığından çıktı değişmiyordu.
#
# NEDEN HATALIYDI?
# - Fonksiyonlar çalışıyor gibi görünse de gerçekte hiçbir işlem yapmıyordu.
# - Listeye ekleme/silme davranışı olmadığı için test sonucu yanlış oluyordu.
#
# NASIL DÜZELTTİK?
# ✔ ekle() fonksiyonuna sehirler.append(sehir) ekledik.
# ✔ sil() fonksiyonuna liste kontrolü ve silme işlemi ekledik.
# ✔ Kullanıcıya her işlemde bilgi veren print() mesajları ekledik.
#
# Sonuç: Kod artık tamamen çalışır durumda ve beklenen liste çıktısını verir.
# ------------------------------------------------------------
