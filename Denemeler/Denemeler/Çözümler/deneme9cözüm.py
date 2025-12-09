# Bu denemede bir "Araba" sınıfı oluşturmanız isteniyor.

# Seviye: Çok Zor

# Gereksinimler:
# - marka, model, hız bilgisi olsun
# - hiz_arttir() fonksiyonu olsun
# - hiz_azalt() fonksiyonu olsun
# - hız 0’ın altına inemesin
# - __str__ override edilsin (print ile güzel gözüksün)

# ------------------------------------------------------------
# DÜZELTİLMİŞ VE TAMAMLANMIŞ KOD
# ------------------------------------------------------------

class Araba:
    def __init__(self, marka, model, hiz=0):
        self.marka = marka
        self.model = model
        self.hiz = hiz

    def hiz_arttir(self, miktar):
        # HATA: Fonksiyon boştu. Hız arttırma işlemi yapılmıyordu.
        # ÇÖZÜM: Verilen miktarı hıza ekledik.
        self.hiz += miktar
        print(f"Hız artırıldı. Yeni hız: {self.hiz} km/h")

    def hiz_azalt(self, miktar):
        # HATA: Hız azaltma işlemi yoktu, hatta negatif hıza düşme kontrolü eksikti.
        # ÇÖZÜM: Hız 0’ın altına düşmesin diye max(0, hız) kullandık.
        self.hiz = max(0, self.hiz - miktar)
        print(f"Hız azaltıldı. Yeni hız: {self.hiz} km/h")

    def __str__(self):
        # HATA: __str__ override edilmemişti.
        # ÇÖZÜM: Arabayı güzel formatlı bir string olarak döndürdük.
        return f"{self.marka} {self.model} | Hız: {self.hiz} km/h"


# ------------------------------------------------------------
# TEST
araba = Araba("BMW", "M4", 50)
print(araba)

araba.hiz_arttir(30)
araba.hiz_azalt(90)
print(araba)


# ------------------------------------------------------------
# HATA NEREDEYDİ?
# - Sınıf tamamen boştaydı, fonksiyonlar tanımlanmamıştı.
# - Hız artırma ve azaltma mekanizması yoktu.
# - Negatif hıza düşme kontrolü yapılmıyordu.
# - __str__ override edilmediği için print(araba) anlamsız çıktı veriyordu.

# NEDEN HATALIYDI?
# - Sınıf iskeleti çalışmadığından obje davranışı sıfırdı.
# - Nesne yönelimli programlama gereği fonksiyonlar ve koruma mekanizmaları eksikti.

# NASIL DÜZELTTİK?
# ✔ __init__ içinde marka, model, hız tanımlandı.
# ✔ hiz_arttir() ve hiz_azalt() fonksiyonları tamamen uygulandı.
# ✔ hızın 0’ın altına düşmemesi için koruma eklendi.
# ✔ __str__ override edilip arabayı okunabilir hale getirdik.
#
# Sonuç: Tamamen çalışan ve tüm gereksinimleri karşılayan bir Araba sınıfı oluştu.
# ------------------------------------------------------------
