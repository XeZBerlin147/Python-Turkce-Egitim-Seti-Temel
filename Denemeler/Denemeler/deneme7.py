# Bu denemede size Python kod iskeleti vereceğiz.
# Listeye eleman ekleme / silme işlemlerini sizin tamamlamanız gerekiyor.

# Seviye: Orta-Zor

sehirler = []

def ekle(sehir):
    # BURAYI TAMAMLAYIN:
    # sehir'i listeye ekleyin ve "Eklendi" yazdırın.
    pass

def sil(sehir):
    # BURAYI TAMAMLAYIN:
    # Eğer sehir listede varsa silin, yoksa "Bulunamadı" yazdırın.
    pass

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