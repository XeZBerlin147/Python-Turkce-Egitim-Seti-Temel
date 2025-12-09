# Bu denemede size sırayla Python kodları vereceğiz.
# Bu kodu Çalıştırın ve çıktısını kontrol ederek doğru çalıştığını teyit edin.

# Seviye: Orta

def menu():
    print("1. Ekle")
    print("2. Sil")
    print("3. Güncelle")
    print("4. Listele")
    print("5. Çıkış")
    
    x = input("Bir seçenek seçin: ")

    # HATA: Menüde kullanıcıdan seçenek alınıyor ama bu seçenek hiçbir yerde kullanılmıyor.
    # Ayrıca menü fonksiyonunun içinde if-else yapısı hiç yoktu.
    # ÇÖZÜM: Kullanıcıdan alınan x değerine göre ilgili fonksiyonları burada çağırıyoruz.

    if x == "1":
        ekle()
    elif x == "2":
        sil()
    elif x == "3":
        guncelle()
    elif x == "4":
        listele()
    elif x == "5":
        print("Çıkış yapılıyor...")
    else:
        print("Geçersiz seçenek, lütfen tekrar deneyin.")

def ekle():
    print("Ekleme işlemi seçildi.")
    
def sil():
    print("Silme işlemi seçildi.")
    
def guncelle():
    print("Güncelleme işlemi seçildi.")
    
def listele():
    print("Listeleme işlemi seçildi.")
    
    
# İf -else yapısı ile menü seçeneklerini işleyin ve seçeneklere göre ilgili fonksiyonları çağırın.

menu()


# ------------------------------------------------------------
# HATA NEREDEYDİ?
# - Menüde kullanıcıdan alınan "x" hiçbir yerde kullanılmıyordu.
# - Menü fonksiyonunun içinde seçimlere bağlı çalışan if-else yapısı eksikti.
# - Bu nedenle kullanıcı bir değer girse bile program hiçbir işlem yapmıyordu.

# NEDEN HATALIYDI?
# - Menü sistemi tasarlanmıştı ama işlevsel değildi.
# - Seçeneklere göre fonksiyon çağırma mekanizması yoktu.
# - Yani menü sadece yazı gösteriyordu, davranış yoktu.

# NASIL DÜZELTTİK?
# ✔ Menü fonksiyonunun içine if-else yapısını yerleştirdik.
# ✔ x değişkenine göre doğru fonksiyonları çağırdık.
# ✔ Böylece menü artık tam anlamıyla çalışan bir yapıya dönüştü.

# ------------------------------------------------------------
