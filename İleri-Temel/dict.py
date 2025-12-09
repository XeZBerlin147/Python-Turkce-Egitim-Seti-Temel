##############################################
#       PYTHON DICTIONARY (DICT) EĞİTİMİ     #
##############################################
# Bu ders, Python sözlük (dictionary) yapısını
# hem temel hem ileri seviyede öğretmek için Professor ve 
# Berlin tarafından hazırlanmış kapsamlı bir eğitim dosyasıdır.
#
# Konular:
# 1) Dictionary nedir?
# 2) Key–value mantığı
# 3) Dict oluşturma yöntemleri
# 4) Index yerine key kullanımı
# 5) Veri ekleme / güncelleme
# 6) Veri silme yöntemleri
# 7) keys(), values(), items()
# 8) get() ile güvenli erişim
# 9) İç içe (nested) dictionary
# 10) Liste içinde dict kullanımı
# 11) Dict içinde liste kullanımı
# 12) Dictionary comprehension
##############################################


print("\n##############################################")
print("#            1) Dictionary Nedir?            #")
print("##############################################\n")

# Dictionary, Python'da verileri "anahtar: değer" (key:value)
# ikilisi şeklinde tutan bir veri yapısıdır.

ogrenci = {
    "isim": "Ahmet",
    "yas": 20,
    "bolum": "Bilgisayar Programcılığı"
}

print("Örnek dictionary:", ogrenci)
print("Tip:", type(ogrenci))


##############################################
#        2) Key–Value (Anahtar–Değer) Mantığı #
##############################################

print("\n--- Key–Value Mantığı ---")
print("ogrenci['isim']:", ogrenci["isim"])
print("ogrenci['yas'] :", ogrenci["yas"])
print("ogrenci['bolum']:", ogrenci["bolum"])

# NOT: Key, dictionary içinde benzersiz olmalıdır (listede index gibi).


##############################################
#        3) Dict Oluşturma Yöntemleri         #
##############################################

print("\n##############################################")
print("#         3) Dict Oluşturma Yöntemleri       #")
print("##############################################\n")

# 1) Normal yol:
kitap = {"ad": "1984", "yazar": "George Orwell", "yil": 1949}
print("kitap:", kitap)

# 2) dict() fonksiyonu:
arac = dict(marka="BMW", model="M4", yil=2020)
print("arac:", arac)

# 3) Boş dict oluşturma:
bos = {}
print("Boş dict:", bos)


##############################################
#       4) INDEX YOK! Key ile erişilir        #
##############################################

print("\n--- Key ile veri okuma ---")

print("İsim:", ogrenci["isim"])
print("Yaş:", ogrenci["yas"])

# liste gibi "ogrenci[0]" çalışmaz → KeyError verir.


##############################################
#  5) Veri Ekleme ve Güncelleme İşlemleri     #
##############################################

print("\n##############################################")
print("#     5) Veri Ekleme / Güncelleme            #")
print("##############################################\n")

# Yeni key ekleme:
ogrenci["sinif"] = 1
print("Yeni key eklendi:", ogrenci)

# Varolan key'in değerini güncelleme:
ogrenci["yas"] = 21
print("Güncellenmiş yaş:", ogrenci)


##############################################
#           6) Veri Silme Yöntemleri          #
##############################################

print("\n##############################################")
print("#            6) Veri Silme Yöntemleri        #")
print("##############################################\n")

# 1) del anahtarı:
del ogrenci["sinif"]
print("del sonrası:", ogrenci)

# 2) pop(): key'i siler, DEĞERİ geri döndürür
yasi = ogrenci.pop("yas")
print("Silinen değer:", yasi)
print("pop sonrası:", ogrenci)

# 3) clear(): tüm dictionary'i temizler
kopya = ogrenci.copy()
kopya.clear()
print("clear() sonrası:", kopya)


##############################################
#       7) keys(), values(), items()          #
##############################################

print("\n##############################################")
print("#           7) Dict Metotları                #")
print("##############################################\n")

print("Keys:", ogrenci.keys())
print("Values:", ogrenci.values())
print("Items:", ogrenci.items())

# Döngü ile gezme:
for key, value in ogrenci.items():
    print(key, ":", value)


##############################################
#           8) get() ile güvenli okuma        #
##############################################

print("\n##############################################")
print("#       8) get() ile Güvenli Erişim          #")
print("##############################################\n")

# Normal erişimde olmayan key hata verir:
# ogrenci["soyisim"] → KeyError

print("Soyisim (güvenli):", ogrenci.get("soyisim"))
print("Varsayılan değerle:", ogrenci.get("soyisim", "bulunamadı"))


##############################################
#    9) İç İçe Sözlük (Nested Dictionary)     #
##############################################

print("\n##############################################")
print("#        9) Nested Dictionary Örneği         #")
print("##############################################\n")

okul = {
    "11-A": {"ogrenci_sayisi": 25, "sinif_baskani": "Ayşe"},
    "11-B": {"ogrenci_sayisi": 30, "sinif_baskani": "Mehmet"},
}

print("Okul verileri:", okul)
print("11-A başkanı:", okul["11-A"]["sinif_baskani"])
print("11-B öğrenci sayısı:", okul["11-B"]["ogrenci_sayisi"])


##############################################
#    10) Liste İçinde Dict Kullanımı         #
##############################################

print("\n##############################################")
print("#     10) Liste İçinde Dict Kullanımı        #")
print("##############################################\n")

urunler = [
    {"ad": "Kalem", "fiyat": 10},
    {"ad": "Defter", "fiyat": 25},
    {"ad": "Silgi", "fiyat": 5}
]

print("Ürünler listesi:", urunler)

for urun in urunler:
    print(f"{urun['ad']} fiyatı: {urun['fiyat']} TL")


##############################################
#    11) Dict İçinde Liste Kullanımı          #
##############################################

print("\n##############################################")
print("#       11) Dict İçinde Liste Kullanımı      #")
print("##############################################\n")

sinif = {
    "isimler": ["Ali", "Veli", "Ayşe"],
    "notlar": [85, 90, 78]
}

print("Sınıf:", sinif)
print("İkinci öğrenci:", sinif["isimler"][1])
print("Ayşe'nin notu:", sinif["notlar"][2])


##############################################
#         12) Dictionary Comprehension        #
##############################################

print("\n##############################################")
print("#          12) Dict Comprehension            #")
print("##############################################\n")

# Listeyi dict'e çevirelim:
sayilar = [1, 2, 3, 4, 5]

kareler = {x: x**2 for x in sayilar}
print("Kareler sozlugu:", kareler)

# Şartlı comprehension:
ciftler = {x: "çift" for x in sayilar if x % 2 == 0}
print("Çift sayılar sözlüğü:", ciftler)

##############################################
