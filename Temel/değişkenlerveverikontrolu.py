# Değişkenleri ve veri kontrolünü gösteren basit bir Python programı;

# Bu program kullanıcıdan bazı bilgiler alır ve bu bilgilerin türlerini kontrol eder.

# Kullanıcıdan isim, yaş ve boy bilgilerini alalım

isim = input("Lütfen isminizi girin: ")
yas = int(input("Lütfen yaşınızı girin: "))
boy = int(input("Lütfen boyunuzu (Santim cinsinden) girin: "))

# Değişken türlerini kontrol edelim
print(f"İsminiz: {isim} (Tür: {type(isim)})") # string türünde (Metin)
print(f"Yaşınız: {yas} (Tür: {type(yas)})") # integer türünde (Tam sayı)
print(f"Boyunuz: {boy} cm (Tür: {type(boy)})") # integer türünde (Tam sayı)


# input() fonksiyonu her zaman string (metin) türünde veri alır.
# Bu nedenle, yaş ve boy bilgilerini integer türüne dönüştürdük.
# Eğer kullanıcı geçersiz bir veri girerse, program hata verebilir.
# Bu durumu önlemek için try-except blokları kullanılabilir.
# Buna sonraki derslerde değineceğiz.



# Bir sonra ki dosya, ifelseelif1.py dosyasıdır. Oraya geçebilirsiniz.