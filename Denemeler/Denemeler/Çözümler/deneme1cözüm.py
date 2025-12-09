# Bu denemede size sırayla Python kodları vereceğiz.
# Bu kodu Çalıştırın ve çıktısını kontrol ederek doğru çalıştığını teyit edin.

# Seviye : Kolay

def topla(a, b):
    return a + b

sonuc = topla(5, 7)
print("Toplam:", sonuc)  # ← DÜZELTİLMİŞ KISIM


# Beklenen çıktı: Toplam: 12
# Not: Çıktının doğru olduğunu teyit etmek için "Toplam: 12" ifadesinin terminalde göründüğünden emin olun.


# ------------------------------------------------------------
# Açıklama:
# HATA NEREDEYDİ?
#   print("Toplam:", topla)
# Burada 'topla' fonksiyonun kendisini yazdırıyordu,
# yani fonksiyonun bellekteki adresini, sonucunu değil.
#
# NEDEN HATALIYDI?
#   Çünkü yazdırılması gereken şey fonksiyonun kendisi değil,
#   fonksiyonun döndürdüğü değer (return sonucu) olmalıydı.
#
# NASIL DÜZELTTİK?
#   topla(5, 7) sonucunu 'sonuc' değişkenine kaydedip,
#   print içerisinde fonksiyonu değil, değişkeni kullandık:
#       print("Toplam:", sonuc)
#
# Böylece çıktı doğru şekilde: Toplam: 12 oldu.
# ------------------------------------------------------------
