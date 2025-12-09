##############################################
#                LİSTELER (LIST)             #
##############################################

# Liste, Python'da birden fazla değeri sıralı bir şekilde tutmamızı sağlayan veri yapısıdır.
# Listeler:
# - Sıralıdır
# - Index (sıra numarası) ile erişilebilir
# - Değiştirilebilir (eleman eklenebilir, silinebilir)
# - Farklı veri tiplerini aynı anda tutabilir


# Basit bir liste oluşturalım:
meyveler = ["elma", "armut", "muz"]

print("Başlangıç listesi:", meyveler)  # ['elma', 'armut', 'muz']


##############################################
#            LİSTEDE INDEX KULLANIMI          #
##############################################

# Index numarası 0'dan başlar!
print("\n--- Index Kullanımı ---")
print("0. index:", meyveler[0])  # elma
print("1. index:", meyveler[1])  # armut
print("2. index:", meyveler[2])  # muz

# Negatif index: sondan başa doğru sayılır.
print("Son eleman (negatif index):", meyveler[-1])  # muz


##############################################
#            LİSTEYE ELEMAN EKLEME            #
##############################################

print("\n--- Eleman Ekleme ---")

# 1) append(): Listenin SONUNA ekler
meyveler.append("kiraz")
print("append sonrası:", meyveler)

# 2) insert(): Belirli bir indexe ekler
meyveler.insert(1, "çilek")
print("insert sonrası:", meyveler)

# 3) extend(): Birden fazla eleman ekler
meyveler.extend(["kavun", "karpuz"])
print("extend sonrası:", meyveler)


##############################################
#            LİSTEDEN ELEMAN SİLME            #
##############################################

print("\n--- Eleman Silme ---")

# 1) remove(): Değer verilir, o değeri siler (ilk bulduğunu)
meyveler.remove("armut")
print("remove sonrası:", meyveler)

# 2) pop(): Index'e göre siler, SİLİNEN DEĞERİ GERİ VERİR
silinen = meyveler.pop(2)
print("pop sonrası:", meyveler)
print("Silinen değer:", silinen)

# 3) del: index'e göre siler (geri döndürmez)
del meyveler[0]
print("del sonrası:", meyveler)


##############################################
#         LİSTE ÖRNEĞİ — KULLANICI GİRİŞİ     #
##############################################

print("\n--- Liste Yönetimi Örneği ---")

# Basit bir liste yönetim sistemi
sepet = ["ekmek", "su", "yumurta"]
print("Sepetiniz:", sepet)

# Eleman ekleme
yeni = "çikolata"
print(f"Sepete '{yeni}' ekleniyor...")
sepet.append(yeni)
print("Güncel sepet:", sepet)

# Eleman silme (kontrollü)
sil = "su"
if sil in sepet:
    sepet.remove(sil)
else:
    print(f"'{sil}' sepette bulunamadı!")

print("Son sepet durumu:", sepet)



################################################
#                  KÜMELER (SET)               #
################################################

# Set (küme) yapısı:
# - Sırasızdır
# - Index ile erişilemez
# - Tekrar eden elemanları otomatik siler
# - Matematiksel küme işlemlerini destekler (union, intersection, difference)

print("\n##############################################")
print("#                  KÜMELER (SET)             #")
print("##############################################\n")

renkler = {"kırmızı", "mavi", "yeşil", "mavi"}  # 'mavi' 2 kez yazsak bile 1 kez tutulur!
print("Başlangıç seti:", renkler)


##############################################
#          SET'E ELEMAN EKLEME/SİLME         #
##############################################

print("\n--- Set İşlemleri ---")

# add(): Eleman ekler
renkler.add("sarı")
print("add sonrası:", renkler)

# remove(): Eleman siler (yoksa hata verir)
renkler.remove("yeşil")
print("remove sonrası:", renkler)

# discard(): Eleman siler (yoksa hata vermez)
renkler.discard("mor")  # Hata vermez
print("discard sonrası:", renkler)



##############################################
#        KÜME (SET) — MATEMATİKSEL İŞLEMLER   #
##############################################

print("\n--- Küme İşlemleri ---")

A = {1, 2, 3}
B = {3, 4, 5}

print("A:", A)
print("B:", B)

# Birleşim (union)
print("A ∪ B:", A | B)  # {1,2,3,4,5}

# Kesişim (intersection)
print("A ∩ B:", A & B)  # {3}

# Fark (difference)
print("A - B:", A - B)  # {1,2}



##############################################
#          LİSTE VE SET'İ BİRLİKTE KULLANMA   #
##############################################

print("\n--- Liste → Set Dönüşümü (Tekrarları Silme) ---")

ogrenciler = ["Ali", "Veli", "Ayşe", "Ali", "Mehmet", "Ayşe"]

print("Liste:", ogrenciler)

# set() tekrar edenleri temizler
ogrenciler_set = set(ogrenciler)
print("Set:", ogrenciler_set)



##############################################
#        EĞİTMEN NOTU — ÖĞRENİLMESİ GEREKENLER #
##############################################

# 1. Listeler sıralıdır, index ile erişilir, tekrar eden değer tutabilir.
# 2. Set'ler sırasızdır, index yoktur, tekrar eden değerleri siler.
# 3. append(), insert(), extend() → veri ekler
# 4. remove(), pop(), del → veri siler
# 5. Set işlemleri programlamada veri temizliği ve kontrol için çok önemlidir.
# 6. Liste → set dönüşümü tekrar eden verileri temizlemede profesyonel bir tekniktir.
# 7. Kümeler matematiksel işlemler için güçlü araçlardır (birleşim, kesişim, fark).