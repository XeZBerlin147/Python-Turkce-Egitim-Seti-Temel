# Kullanıcıya tekrar tekrar soru sormak için sonsuz döngü kullanıyoruz.
# Kullanıcı geçerli giriş yapınca döngüyü break ile kıracağız.

while True: # Sonsuz döngü başlatıyoruz. Ta ki Break ile kırılana kadar devam edecek.
    try:
        # Kullanıcıdan cevap alıyoruz.
        soru = input("Hava bugün güneşli mi? (evet/hayır): ")

        # .strip() → baştaki ve sondaki boşlukları siler
        # .lower() → tüm harfleri küçültür
        cevap = soru.strip().lower()

        # Kullanıcı "evet" derse:
        if cevap == "evet":
            print("Harika! Güneşli havalarda dışarı çıkmak çok keyiflidir.")
            break  # Geçerli cevap → döngüyü bitir.

        # Kullanıcı "hayır" derse:
        elif cevap == "hayır":
            print("Üzgünüm! Umarım hava yakında düzelir.")
            break  # Geçerli cevap → döngüyü bitir.

        # Kullanıcı başka bir şey yazarsa:
        else:
            print("❗ Lütfen sadece 'evet' veya 'hayır' yazın.")
            print("Tekrar deneyelim...\n")
            # break yok → döngü yeniden başlar.

    except Exception as hata:
        # try bloğu içinde beklenmedik bir hata oluşursa burası çalışır.
        print("Bir hata oluştu:", hata)
        print("Program çökmemesi için except bloğu devreye girdi.")
        print("Lütfen tekrar deneyin.\n")
        # break yok → döngü yeniden başlar.
        
# Program burada sona erer.

# Bir sonra ki dosya: listelervekümeler.py