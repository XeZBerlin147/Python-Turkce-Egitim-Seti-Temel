##############################################
#    PYTHON FONKSİYONLARI (def) EĞİTİMİ      #
##############################################
# Bu ders fonksiyonları hem temel hem ileri
# seviye mantığıyla öğretmek için Profesör ve
# Berlin tarafından hazırlanmıştır.
#
# İçerik:
# 1) Fonksiyon nedir, neden kullanılır?
# 2) Temel fonksiyon tanımı
# 3) Parametreler, argümanlar
# 4) Varsayılan parametreler
# 5) Return mantığı (tekli–çoklu dönüş)
# 6) Keyword argümanları
# 7) *args ve **kwargs
# 8) Fonksiyon scope (yerel/global değişkenler)
# 9) Yüksek seviyeli fonksiyonlar
##############################################


print("\n##############################################")
print("#        1) Fonksiyon Nedir ve Neden Var?     #")
print("##############################################\n")

# Fonksiyon:
# - Belirli bir işi yapan kod bloğudur.
# - Tekrarlanan kodu azaltır.
# - Kodun düzenli ve anlaşılır olmasını sağlar.

print("Fonksiyonlar tekrar eden işleri düzenlemek için vardır.\n")


##############################################
#        2) Basit Fonksiyon Tanımı           #
##############################################

print("\n--- Basit Fonksiyon ---")

def selam_ver():
    print("Merhaba! Fonksiyon çalıştı.")

selam_ver()  # çağırma


##############################################
#        3) Parametreli Fonksiyon            #
##############################################

print("\n--- Parametreli Fonksiyon ---")

def selam(isim):
    print(f"Selam {isim}!")

selam("XeZ")
selam("Ahmet")


##############################################
#             4) Varsayılan Parametre         #
##############################################

print("\n--- Varsayılan Parametreler ---")

def carp(a, b=1):
    print("Sonuç:", a * b)

carp(5)
carp(5, 2)


##############################################
#     5) Return Mantığı (Değer Döndürme)     #
##############################################

print("\n--- Return Mantığı ---")

def topla(a, b):
    return a + b

sonuc = topla(3, 7)
print("Toplam:", sonuc)


# ÇOKLU DEĞER DÖNDÜRME (tuple)
def islemler(a, b):
    return a+b, a-b, a*b

toplam, fark, carpim = islemler(10, 3)
print("Toplam:", toplam, "| Fark:", fark, "| Çarpım:", carpim)


##############################################
#         6) Keyword Argümanları              #
##############################################

print("\n--- Keyword Argümanları ---")

def bilgiler(isim, yas, sehir):
    print(f"{isim}, {yas} yaşında, {sehir}'de yaşıyor.")

bilgiler(yas=20, isim="Samet", sehir="Ankara")


##############################################
#             7) *args ve **kwargs            #
##############################################

print("\n--- *args ve **kwargs ---")

# args: birden fazla isimsiz argüman
def toplam(*args):
    print(args, "| Tip:", type(args))
    return sum(args)

print("Toplam:", toplam(1, 2, 3, 4))


# kwargs: birden fazla isimli argüman
def bilgiler2(**kwargs):
    print(kwargs)

bilgiler2(isim="Ali", yas=30, sehir="İzmir")


##############################################
#             8) Scope Mantığı               #
##############################################

print("\n--- Scope (Yerel/Global Değişken) ---")

x = 10  # global değişken

def fonksiyon():
    x = 20  # yerel değişken
    print("Fonksiyon içi:", x)

fonksiyon()
print("Fonksiyon dışı:", x)


##############################################
#     9) Yüksek Seviyeli Fonksiyonlar         #
##############################################

print("\n--- Yüksek Seviyeli Fonksiyonlar ---")

def iki_kat(f, sayi):
    return f(sayi)

def katla(n):
    return n * 2

print("İki kat:", iki_kat(katla, 5))


##############################################
# Eğitimin Sonu. Kendinizi sadece kod yazarak ve proje oluşturarak geliştirebilirsiniz.
# İyi çalışmalar dileriz!
##############################################