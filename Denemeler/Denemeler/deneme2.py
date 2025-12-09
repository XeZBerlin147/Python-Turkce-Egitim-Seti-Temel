# Bu denemede size sırayla Python kodları vereceğiz.
# Bu kodu Çalıştırın ve çıktısını kontrol ederek doğru çalıştığını teyit edin.

# seviye : Orta-Kolay

def menu():
    print("1. Ekleme")
    print("2. Çıkarma")
    print("3. Çıkış")
    
    cevap = input("Bir seçenek seçin (1-3): ")
    
    if cevap == 1:
        print("Ekleme seçildi.")
    elif cevap == 2:
        print("Çıkarma seçildi.")
    elif cevap == 3:
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

# Kodda bir hata var ve bu hatayı bulup düzeltmeniz gerekiyor.
    