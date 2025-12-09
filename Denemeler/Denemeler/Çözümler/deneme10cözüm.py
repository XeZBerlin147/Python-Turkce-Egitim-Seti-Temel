# Bu denemede gelişmiş bir "Araba" sınıfı oluşturmanız isteniyor.
#
# Seviye: Çok Zor
#
# Aşağıdaki sınıf tüm gereksinimleri karşılayacak şekilde TAMAMLANMIŞTIR.
# Kodun sonunda detaylı açıklamalar yorum satırı olarak verilmiştir.


class Araba:
    def __init__(self, marka, model, max_hiz, yakit=100):
        self.marka = marka
        self.model = model
        self.hiz = 0
        self.max_hiz = max_hiz
        self.vites = 1
        self.motor_acik = False
        self.yakit = yakit
        self.km = 0

    # MOTOR AÇMA
    def motoru_ac(self):
        if self.yakit <= 0:
            raise ValueError("Yetersiz yakıt! Motor açılamaz.")
        self.motor_acik = True
        print("Motor açıldı.")

    # MOTOR KAPATMA
    def motoru_kapat(self):
        if self.hiz > 0:
            raise ValueError("Hız 0 değilken motor kapatılamaz!")
        self.motor_acik = False
        print("Motor kapatıldı.")

    # HIZ ARTTIRMA
    def hiz_arttir(self, miktar):
        if not self.motor_acik:
            print("Motor kapalıyken hız arttırılamaz!")
            return
        
        if self.yakit <= 0:
            print("YAKIT BİTTİ! Motor kapanıyor...")
            self.motor_acik = False
            return

        yeni_hiz = self.hiz + miktar

        # Maksimum hız kontrolü
        if yeni_hiz > self.max_hiz:
            print(f"UYARI: Maksimum hız {self.max_hiz} km/h! Daha fazla artılamaz.")
            yeni_hiz = self.max_hiz

        # Vites aralığı kontrolü (örneğin: vites * 40)
        vites_limiti = self.vites * 40
        if yeni_hiz > vites_limiti:
            print("UYARI: Vites aralığını aştınız! (Yine de hız artırıldı)")

        # Hız güncelle
        self.hiz = yeni_hiz

        # KM ARTTIR
        self.km += miktar * 0.1  # Basit bir km hesaplaması

        # YAKIT TÜKETİMİ
        self.yakit -= miktar * 0.05
        if self.yakit < 0:
            self.yakit = 0

        print(f"Hız artırıldı: {self.hiz} km/h | Yakit: {self.yakit:.1f}")

        if self.yakit == 0:
            print("Yakıt tamamen bitti! Motor kapanıyor.")
            self.motor_acik = False

    # HIZ AZALTMA
    def hiz_azalt(self, miktar):
        self.hiz = max(0, self.hiz - miktar)
        print(f"Hız azaltıldı: {self.hiz} km/h")

    # VİTES YÜKSELT
    def vites_yukselt(self):
        if self.vites >= 6:
            print("Zaten en yüksek vitestesiniz.")
        else:
            self.vites += 1
            print(f"Vites yükseltildi: {self.vites}")

    # VİTES DÜŞÜR
    def vites_dusur(self):
        if self.vites <= 1:
            print("Daha düşük vites yok.")
        else:
            self.vites -= 1
            print(f"Vites düşürüldü: {self.vites}")

    # BİLGİ - __str__ OVERRIDE
    def __str__(self):
        motor_durum = "Açık" if self.motor_acik else "Kapalı"
        return (f"{self.marka} {self.model} | Hız: {self.hiz} km/h | "
                f"Vites: {self.vites} | Yakit: {self.yakit:.1f} | Motor: {motor_durum} | KM: {self.km:.1f}")


# ------------------------------------------------------------
# TEST
araba = Araba("Mercedes", "AMG", max_hiz=280)
print(araba)

araba.motoru_ac()
araba.hiz_arttir(50)
araba.vites_yukselt()
araba.hiz_arttir(100)
araba.hiz_azalt(80)
print(araba)


# ------------------------------------------------------------
# AÇIKLAMALAR:
#
# ✔ TÜM GEREKSİNİMLER TAMAMLANDI.
#
# HATALARIN ORİJİNALİ: Kod tamamen eksikti, tüm sınıf davranışları boştaydı.
#
# NEDEN HATALIYDI?
# - Motor kontrolü yoktu
# - Yakıt sistemi yoktu
# - Vites limiti yoktu
# - KM artışı yoktu
# - Maksimum hız kontrolü yoktu
# - __str__ override yoktu
# - ValueError hiç kullanılmamıştı
#
# NASIL DÜZELTTİK?
# ✔ Tüm değişkenler eklendi
# ✔ Motor aç/kapat kontrolü yapıldı
# ✔ Hız arttırma ve azaltma mekanizması kuruldu
# ✔ Yakıt tüketimi eklendi
# ✔ Vites kontrolü eklendi
# ✔ KM sayaç sistemi kuruldu
# ✔ ValueError en az 1 yerde kullanıldı
# ✔ __str__ override ile detaylı çıktı oluşturuldu
#
# Sonuç: GERÇEĞE YAKIN, tam işlevli bir araç simülasyon sınıfı oluştu.
# ------------------------------------------------------------
