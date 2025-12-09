##############################################
#              TUPLE (DEMET) EĞİTİMİ        #
##############################################
# Bu dosya, Python'da tuple (demet) yapısını
# ileri-temel seviyede öğrenmek isteyenler için
# detaylı ve bol örnekli olarak Profesör ve Berlin
# Tarafından hazırlanmıştır, Başarılar dileriz!
#
# Konular:
# 1) Tuple nedir? Liste ile farkı nedir?
# 2) Tuple tanımlama yöntemleri
# 3) Index ile erişim, slicing (dilimleme)
# 4) Değiştirilemezlik (immutability) ve etkileri
# 5) Tuple -> list, list -> tuple dönüşümleri
# 6) Packing & Unpacking (paketleme / açma)
# 7) Fonksiyonlardan çoklu değer döndürme
# 8) Tuple'ı dict key'i olarak kullanma
##############################################


print("\n##############################################")
print("#                1) TUPLE NEDİR?             #")
print("##############################################\n")

# Tuple, listelere benzer, fakat:
# - Değiştirilemez (immutable)
# - Genelde sabit veriler için kullanılır
# - Parantez () ile tanımlanır
# - Sıralıdır ve index ile erişilebilir

# Basit bir tuple:
renkler_tuple = ("kırmızı", "mavi", "yeşil")
print("Tuple:", renkler_tuple)
print("Tipi:", type(renkler_tuple))


##############################################
#      2) TUPLE vs LİSTE KARŞILAŞTIRMASI      #
##############################################

print("\n--- Tuple vs Liste Karşılaştırması ---")

renkler_list = ["kırmızı", "mavi", "yeşil"]

print("Liste:", renkler_list, "| Tip:", type(renkler_list))
print("Tuple:", renkler_tuple, "| Tip:", type(renkler_tuple))

# Temel fark:
# Liste: Değiştirilebilir -> Eleman eklenebilir, silinebilir, değiştirilebilir.
# Tuple: Değiştirilemez -> Oluşturduktan sonra üzerinde değişiklik yapamazsınız.


##############################################
#         3) TUPLE OLUŞTURMA YÖNTEMLERİ       #
##############################################

print("\n##############################################")
print("#         3) TUPLE OLUŞTURMA YÖNTEMLERİ      #")
print("##############################################\n")

# Normal tanımlama:
sayilar = (1, 2, 3, 4)
print("Sayılar:", sayilar)

# Parantezsiz tanımlama (Packing):
karisik = 10, "merhaba", True
print("Karışık tuple:", karisik, "| Tip:", type(karisik))

# Tek elemanlı tuple:
tek_sayi = (5,)
print("Tek elemanlı tuple:", tek_sayi, "| Tip:", type(tek_sayi))

# Parantez koyup virgül koymazsan:
yalnizca_sayi = (5)
print("Virgülsüz:", yalnizca_sayi, "| Tip:", type(yalnizca_sayi))  # int

# NOT:
# Tek elemanlı tuple için SONDA virgül şart:
# tek = (5,)  # Doğru
# tek = (5)   # Sadece int olur


##############################################
#         4) INDEX İLE ERİŞİM & SLICING       #
##############################################

print("\n##############################################")
print("#        4) INDEX İLE ERİŞİM ve DİLİMLEME    #")
print("##############################################\n")

renkler = ("kırmızı", "mavi", "yeşil", "sarı", "mor")

print("Tuple:", renkler)
print("0. index:", renkler[0])   # kırmızı
print("2. index:", renkler[2])   # yeşil
print("Son eleman:", renkler[-1])  # mor

# Dilimleme (slicing)
print("0'dan 3'e kadar:", renkler[0:3])  # ('kırmızı', 'mavi', 'yeşil')
print("2'den sona kadar:", renkler[2:])  # ('yeşil', 'sarı', 'mor')
print("Tüm tuple:", renkler[:])         # tamamı


##############################################
#          5) DEĞİŞTİRİLEMEZLİK (IMMUTABLE)   #
##############################################

print("\n##############################################")
print("#      5) TUPLE DEĞİŞTİRİLEMEZLİĞİ (IMMUT.)  #")
print("##############################################\n")

# Tuple üzerinde doğrudan değişiklik yapmaya çalışalım:

print("Orijinal tuple:", renkler)

# Aşağıdaki satır HATA ÜRETİR (TypeError)
# renkler[0] = "turuncu"

print("Tuple'da bir elemanı değiştirmeye çalışırsanız TypeError alırsınız.")
print("Bu yüzden tuple, sabit veriler için güvenlidir.\n")

# Ama içindeki elemanlar mutable ise (örneğin bir liste) O liste değiştirilebilir:

icerik = (1, 2, [3, 4])
print("Başlangıç:", icerik)

icerik[2].append(5)  # Tuple'ın içindeki listeyi değiştirmek serbesttir!
print("Listedeki değişiklik sonrası:", icerik)


##############################################
#     6) TUPLE <-> LİSTE DÖNÜŞÜMLERİ          #
##############################################

print("\n##############################################")
print("#        6) TUPLE <-> LİSTE DÖNÜŞÜMLERİ      #")
print("##############################################\n")

orijinal_tuple = ("elma", "armut", "muz")
print("Orijinal tuple:", orijinal_tuple)

# Tuple -> Liste
liste = list(orijinal_tuple)
print("Listeye dönüştürüldü:", liste, "| Tip:", type(liste))

# Değişiklik yapalım:
liste.append("çilek")
liste[0] = "yeşil elma"
print("Değiştirilmiş liste:", liste)

# Liste -> Tuple
yeni_tuple = tuple(liste)
print("Tekrar tuple'a dönüştürüldü:", yeni_tuple, "| Tip:", type(yeni_tuple))

# NOT: Backend projelerinde sabit kalması gereken verileri tuple olarak tutmak,
# değişebilir verileri list olarak yönetmek iyi bir pratiktir.


##############################################
#      7) PACKING & UNPACKING (PAKETLEME)     #
##############################################

print("\n##############################################")
print("#      7) PACKING & UNPACKING (PAKETLEME)    #")
print("##############################################\n")

# PACKING: Birden fazla değeri tek bir tuple içinde toplamak
paket = 10, 20, 30
print("Paketlenmiş tuple:", paket)

# UNPACKING: Tuple'ı değişkenlere açmak
a, b, c = paket
print("a:", a, "b:", b, "c:", c)

# Dikkat: Sol taraftaki değişken sayısı, tuple içindeki eleman sayısına eşit olmalı.

# Örnek:
ogrenci = ("Ali", 20, "Bilgisayar Programcılığı")
isim, yas, bolum = ogrenci
print("İsim:", isim)
print("Yaş:", yas)
print("Bölüm:", bolum)

# * (yıldız) operatörü ile kalanları liste olarak yakalayabilirsin:
sayilar = (1, 2, 3, 4, 5)
ilk, *orta, son = sayilar
print("İlk:", ilk)
print("Orta:", orta)  # liste oldu
print("Son:", son)


##############################################
#  8) FONKSİYONLARDAN ÇOKLU DEĞER DÖNDÜRME    #
##############################################

print("\n##############################################")
print("#  8) FONKSİYONLARDAN ÇOKLU DEĞER DÖNDÜRME   #")
print("##############################################\n")

# Fonksiyonlardan birden fazla değer döndürmek için genelde tuple kullanılır.

def bolme_islemi(a, b):
    """
    a'yı b'ye böler ve:
    - sonucu
    - kalanı
    - b'nin sıfır olup olmadığını
    bir tuple olarak döndürür.
    """
    if b == 0:
        return None, None, False  # b sıfırsa hatalı durum
    sonuc = a // b
    kalan = a % b
    return sonuc, kalan, True

sonuc, kalan, basarili_mi = bolme_islemi(10, 3)
print("10 / 3 sonucu:", sonuc, "| kalan:", kalan, "| başarılı mı?", basarili_mi)


##############################################
#      9) TUPLE'I DICT KEY OLARAK KULLANMA    #
##############################################

print("\n##############################################")
print("#      9) TUPLE'I DICT KEY OLARAK KULLANMA   #")
print("##############################################\n")

# Tuple değiştirilemez olduğu için, dictionary'de anahtar (key) olarak kullanılabilir.
# Örneğin: (x, y) koordinatı anahtar olsun.

noktalar = {
    (0, 0): "Orijin",
    (10, 5): "A noktası",
    (3, -2): "B noktası"
}

print("Noktalar sözlüğü:", noktalar)
print("Orijin:", noktalar[(0, 0)])

# Listeler değiştirilebilir olduğu için key olamazlar:
# ornek = { [1, 2]: "hata" }  # TypeError verir.

##############################################
#  NOT:
#  Bu dosya, ileri-temel seviye bir tuple eğitimi
#  için hazırlanmıştır. Eğitim setinin bir parçasıdır.
##############################################
