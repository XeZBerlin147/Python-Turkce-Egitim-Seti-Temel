# Bu denemede size sırayla Python kodları vereceğiz.
# Bu kodu Çalıştırın ve çıktısını kontrol ederek doğru çalıştığını teyit edin.

# seviye : Orta-Kolay

def menu():
    print("1. Ekleme")
    print("2. Çıkarma")
    print("3. Çıkış")
    
    cevap = input("Bir seçenek seçin (1-3): ")
    
    # input() fonksiyonu her zaman string (metin) döndürür.
    # Bu yüzden cevap'ı "1", "2", "3" ile karşılaştırmamız gerekir.
    if cevap == "1":
        print("Ekleme seçildi.")
    elif cevap == "2":
        print("Çıkarma seçildi.")
    elif cevap == "3":
        print("Çıkış yapılıyor.")
    else:
        print("Geçersiz seçenek.")
        
menu()


# Beklenen çıktı:
# 1. Ekleme
# 2. Çıkarma
# 3. Çıkış
# Bir seçenek seçin (1-3):
# Ekleme seçildi. (veya diğer seçeneklere göre farklı çıktı)

# ------------------------------------------------------------
# Açıklama:
# HATA NEREDEYDİ?
#   if cevap == 1:
#   elif cevap == 2:
#   elif cevap == 3:
#
# Burada cevap değişkeni, input() fonksiyonundan geldiği için
#   her zaman string (metin) türündedir. Yani "1", "2", "3" gibi.
# Ancak karşılaştırma integer (sayı) olan 1, 2, 3 ile yapılıyordu.
#
# NEDEN HATALIYDI?
#   Python'da "1" (string) ile 1 (int) eşit değildir.
#   Bu nedenle kullanıcı "1" girse bile:
#       cevap == 1   → False
#   olur ve hiçbir if/elif bloğu çalışmaz, en sonda "Geçersiz seçenek."
#   yazılırdı.
#
# NASIL DÜZELTTİK?
#   İki yol vardı:
#     1) cevap'ı int'e dönüştürmek: cevap = int(cevap) ve 1,2,3 ile karşılaştırmak
#     2) 1,2,3 yerine "1","2","3" kullanmak
#
#   Biz bu çözümde ikinci yolu seçtik ve karşılaştırmaları şöyle yaptık:
#       if cevap == "1":
#       elif cevap == "2":
#       elif cevap == "3":
#
# Böylece kullanıcıdan gelen string değerlerle doğru şekilde karşılaştırma
# yapılmış oldu ve menü düzgün çalıştı.
# ------------------------------------------------------------
