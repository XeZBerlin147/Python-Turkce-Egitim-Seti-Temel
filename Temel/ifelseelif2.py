# şimdi bir soru soracağız ve cevapa göre farklı mesajlar göstereceğiz.
soru = input("Hava bugün güneşli mi? (evet/hayır): ") #Soru değeri kullanıcıdan alınıyor.

if soru.lower() == "evet":  # Kullanıcı "evet" derse
    print("Harika! Güneşli havalarda dışarı çıkmak çok keyiflidir.") # Güzel mesajı göster.
    
elif soru.lower() == "hayır":  # Kullanıcı "hayır" derse
    print("Üzgünüm! Umarım hava yakında düzelir.") # Üzgün mesajı göster.
    
else:
    print("Lütfen sadece 'evet' veya 'hayır' ile cevap verin.")  # Geçersiz cevap alınca mesajı göster.
    
    
# Bu kod, kullanıcıdan hava durumuyla ilgili bir soru sorar ve cevaba göre farklı mesajlar gösterir.
# Eğer kullanıcı "evet" derse, güneşli havalarda dışarı çıkmanın keyifli olduğunu söyler.
# Eğer kullanıcı "hayır" derse, havanın yakında düzelmesini diler.
# Eğer kullanıcı geçersiz bir cevap verirse, sadece 'evet' veya 'hayır' ile cevap vermesini ister.
# Bu örnek, if, elif ve else ifadelerinin nasıl kullanılacağını göstermektedir.

# Bonus bilgi: .lower() metodu, kullanıcının girdiği cevabı küçük harflere çevirir, böylece "Evet", "EVET" gibi farklı yazımlar da "evet" olarak kabul edilir.
# Bu sayede kullanıcı girdisi daha esnek hale gelir.

# .upper() metodu ise tüm karakterleri büyük harfe çevirir. Örneğin, soru.upper() == "EVET" şeklinde de kullanılabilir.


# Bir sonra ki dosya, tryexcept.py dosyasıdır. Oraya geçebilirsiniz.

  