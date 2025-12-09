# Bu denemede size sırayla Python kodları vereceğiz.
# Bu kodu Çalıştırın ve çıktısını kontrol ederek doğru çalıştığını teyit edin.

# Seviye : Kolay

import os
import time   # ← EKSİK OLAN İMPORT EKLENDİ

print("Merhaba, Dünya!")
print("Bu benim ilk Python programım.")
print("Python öğrenmek çok eğlenceli!")
time.sleep(5)  # 5 saniye bekle
os.system('cls')  # Ekranı temizle (Windows için)
print("Ekran temizlendi.")


# Kodun çıktısı:
# Merhaba, Dünya!
# Bu benim ilk Python programım.
# Python öğrenmek çok eğlenceli!
# (5 saniye bekleme)
# (Ekran temizlendi.)
# Ekran temizlendi.


# ------------------------------------------------------------
# Açıklama:
# HATA NEREDEYDİ?
#   time.sleep(5) satırında hata veriyordu çünkü "time" modülü
#   import edilmemişti.
#
# NEDEN HATALIYDI?
#   Python, import edilmeyen bir modülü tanıyamaz.
#   Bu yüzden:
#       NameError: name 'time' is not defined
#   hatası oluşurdu.
#
# NASIL DÜZELTTİK?
#   Kodun başına:
#       import time
#   ekleyerek time.sleep() fonksiyonunu kullanabilir hale getirdik.
#
# Böylece kod sorunsuz şekilde 5 saniye bekliyor,
# ardından ekranı temizleyip "Ekran temizlendi." mesajını gösteriyor.
# ------------------------------------------------------------
