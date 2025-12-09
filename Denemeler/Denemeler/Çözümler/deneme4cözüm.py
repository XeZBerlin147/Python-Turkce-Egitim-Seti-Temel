import time

def tamamlandi():
    print("Kod başarıyla çalıştı!")
    time.sleep(5)
    
def basarisiz():
    print("Kod çalışmadı, lütfen hataları kontrol edin.")
    time.sleep(5)

def deneme():
    try:
        # HATA 1: 'a' ve 'b' değişkenleri string olarak tanımlanmıştı:
        # a = '5'
        # b = '10'
        # Bu durumda toplama işlemi sayı toplamaz, string birleştirme yapar -> "510"
        # ÇÖZÜM: Sayısal işlem olduğu için integer türüne çevirdik.
        a = 5
        b = 10

        toplam = a + b

        # HATA 2: toplam bir fonksiyon gibi çağrılıyordu:
        # print("Toplam:", toplam(15, 25))
        # Bu hata TypeError üretir çünkü "toplam" bir integer, çağrılabilir bir fonksiyon değil.
        #
        # ÇÖZÜM: total değişkenini doğrudan yazdırdık.
        print("Toplam:", toplam)

        tamamlandi()

    except Exception as e:
        # Eğer bir hata olsaydı buraya düşecekti
        print("Hata:", e)
        basarisiz()
        
        
deneme()

# Beklenen çıktı:
# Toplam: 15
# Kod başarıyla çalıştı!
