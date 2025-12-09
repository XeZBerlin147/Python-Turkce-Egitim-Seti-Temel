# Şimdi size Python'da if, elif ve else ifadelerinin nasıl kullanıldığını gösteren basit bir örnek vereceğim.
# Kullanıcıdan bir sayı alacağız ve bu sayının pozitif, negatif veya sıfır olup olmadığını kontrol edeceğiz.
# Kullanıcıdan bir sayı almak için input() fonksiyonunu kullanacağız ve ardından if, elif ve else ifadeleriyle durumu kontrol edeceğiz.

# Kullanıcıdan bir sayı al

#---------------------------------------------------------------

sayi = float(input("Lütfen bir sayı girin: "))

#---------------------------------------------------------------

# Sayının pozitif, negatif veya sıfır olup olmadığını kontrol et

if sayi > 0: # Sayi 0'dan büyükse
    print("Girdiğiniz sayı pozitiftir.") # Sayi sıfırdan büyükse ekrana pozitif mesajı yazdır
    
elif sayi < 0: # Sayi 0'dan küçükse
    print("Girdiğiniz sayı negatiftir.") # Sayi sıfırdan küçükse ekrana negatif mesajı yazdır
    
else: # Bunlardan hiç biri değilse, yani sayı 0 ise
    print("Girdiğiniz sayı sıfırdır.") # Sayi sıfırsa ekrana sıfır mesajı yazdır
    
#---------------------------------------------------------------
    
# Bu kod, kullanıcıdan bir sayı alır ve bu sayının pozitif, negatif veya sıfır olup olmadığını kontrol eder.
# Eğer sayı pozitifse, "Girdiğiniz sayı pozitiftir." mesajını yazdırır.
# Eğer sayı negatifse, "Girdiğiniz sayı negatiftir." mesajını yazdırır.
# Eğer sayı sıfırsa, "Girdiğiniz sayı sıfırdır." mesajını yazdırır.

#---------------------------------------------------------------

# Ekstra Bilgi;

# Sayinin sifira eşit veya büyük olup olmadığını kontrol etmek için ise;
if sayi >= 0: # Sayi 0'a eşit veya büyükse
    print("Girdiğiniz sayı sıfır veya pozitiftir.")
    
# Fakat Pozitif negatif kontrolü için yukarıdaki gibi => yerine > kullanmak daha mantıklıdır.
# Çünkü pozitif sayılar 0'dan büyük sayılardır.

#---------------------------------------------------------------

# Bir sonra ki örnekte görüşmek üzere! Sonraki: ifelseelif2.py dosyasına bakabilirsiniz.