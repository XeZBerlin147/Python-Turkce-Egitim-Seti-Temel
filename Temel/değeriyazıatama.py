# Şimdi değeri atama işlemini gerçekleştirelim.
# Değer atamak için önce atanacak değeri yazıp sonra değerini eşitlememiz gerekir. Yani;

kahve = "Kahveyi çok seviyorum"  # kahve değişkeni "Kahveyi çok seviyorum" olarak atanır

süt = "Sütlü kahve"  # süt değişkeni "Sütlü kahve" olarak atanır

çay = "Çayı da severim"  # çay değişkeni "Çayı da severim" olarak atanır

toplam = kahve + ", " + süt + ", " + çay  # toplam değişkeni kahve, süt ve çay'ın birleştirilmiş hali olarak atanır

print(toplam)  # Çıktı: Kahveyi çok seviyorum, Sütlü kahve, Çayı da severim
print("-----------------------------------------------")


# toplam = kahve + ", "... kısmında dikkat ederseniz, değişkenleri birleştirirken aralarına virgül ve artı işareti koyduk.
# bu sayede değişkenleri yanyana yazdırabildik. Fakat eğer biri sayı biri yazı olacak olsaydı, + işareti hata verirdi.
# Çünkü Python, farklı türdeki verileri doğrudan toplama işlemi yapamaz, bu yüzden hepsini yazı türüne çevirmemiz gerekir.
# Örneğin;

sayi = "42"  # Sayi değişkeni 42 olarak atanır FAKAT yazı türünde.

yazi = " sayısı çok anlamlıdır."  # yazi değişkeni " sayısı çok anlamlıdır." olarak atanır.

print(sayi + yazi)  # Çıktı: 42 sayısı çok anlamlıdır.


# Eğer sayi değişkenini sayı türünde tanımlasaydık, yani sayi = 42 olarak atasaydık,
# print(sayi + yazi) satırı hata verirdi çünkü sayı ve yazı türleri doğrudan toplanamazdı.

sayi2 = 42  # sayi2 değişkeni 42 olarak atanır, bu sefer sayı türünde.
# print(sayi2 + yazi)  # Bu satır hata verir çünkü sayı ve yazı türleri doğrudan toplanamaz.
# Bu yüzden sayi2 değişkenini yazı türüne çevirmemiz gerekir. Bunu str() fonksiyonu ile yapabiliriz.

print(str(sayi2) + yazi)  # Çıktı: 42 sayısı çok anlamlıdır.



# Bir sonra ki dosya, değişkenlerveverikontrolu.py dosyasıdır. Oraya geçebilirsiniz.
