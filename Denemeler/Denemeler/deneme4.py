# Bu denemede size sırayla Python kodları vereceğiz.
# Bu kodu Çalıştırın ve çıktısını kontrol ederek doğru çalıştığını teyit edin.

# Seviye: Orta

import time

def tamamlandi():
    print("Kod başarıyla çalıştı!")
    time.sleep(5)
    
def basarisiz():
    print("Kod çalışmadı, lütfen hataları kontrol edin.")
    time.sleep(5)
def deneme():
    try:
        # Basit bir toplama işlemi
        a = '5'
        b = '10'
        toplam = a + b
        print("Toplam:", toplam(15 , 25))
        tamamlandi()
    except Exception as e:
        print("Hata:", e)
        basarisiz()
        
        
deneme()

# Beklenen çıktı:
# Toplam: 15
# Kod başarıyla çalıştı!

# Not: Eğer kod doğru çalışmazsa, lütfen hataları kontrol edin ve düzeltin.