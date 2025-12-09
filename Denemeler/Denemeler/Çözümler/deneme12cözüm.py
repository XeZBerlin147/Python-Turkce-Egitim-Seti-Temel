# Bu denemede EXTREME seviye bir “Araba Simülasyonu” yazmanız isteniyor.
#
# Seviye: Ultra Zor
#
# Aşağıdaki sınıf, yorumlarda verilen TÜM gereksinimleri karşılayacak şekilde
# tam olarak IMPLEMENTE EDİLMİŞ çözümlü versiyondur.
# En altta hataların/eksiklerin nerede olduğu ve nasıl çözüldüğü anlatılmıştır.

class Araba:
    def __init__(self, marka, model, max_hiz):
        # Temel bilgiler
        self.marka = marka
        self.model = model

        # Dinamik hız ve limitler
        self.hiz = 0                        # km/h
        self.max_hiz_taban = max_hiz        # Hasarsız, lastik sağlamken max hız
        self.max_hiz = max_hiz              # Hasar/lastik ile değişecek

        # Vites ve RPM
        self.vites = 1                      # 1–7
        self.vites_oranlari = {            # Basit hız çarpanları
            1: 0.25,
            2: 0.40,
            3: 0.55,
            4: 0.70,
            5: 0.85,
            6: 0.95,
            7: 1.00,
        }
        self.rpm = 0                        # 0–8000

        # Motor ve yakıt
        self.motor_acik = False
        self.yakit = 100.0                  # 0–100
        self.km = 0.0                       # toplam mesafe

        # Ultra değişkenler
        self.turbo = 0.0                    # 0–100
        self.sicaklik = 90.0                # °C (normal çalışma sıcaklığı)
        self.hasar = 0.0                    # % cinsinden
        self.lastik = 100.0                 # % cinsinden

        # Kontrol sistemleri
        self.tcs = True                     # Traction Control (çekiş kontrol)
        self.yol_tutusu = 0.9               # 0.5–1.0 arası
        self.abs_aktif = False              # ABS durumu

    # ------------------ Yardımcı Hesaplar ------------------ #

    def _etkin_max_hiz(self):
        """
        Hasar ve lastik durumuna göre dinamik maksimum hız hesaplar.
        Örnek kural:
        - %50 hasar → max hızın ~%60’ı kalır
        - Lastik durumu da çarpan olarak eklenir
        """
        hasar_faktoru = 1 - 0.8 * (self.hasar / 100)      # hasar arttıkça düşer
        lastik_faktoru = 0.5 + 0.5 * (self.lastik / 100)  # %0→0.5, %100→1.0
        etkin = self.max_hiz_taban * max(0, hasar_faktoru) * lastik_faktoru
        return max(20, etkin)  # aşırı düşmesin diye alt sınır

    def _guncelle_rpm(self):
        # Basit RPM modeli: hız * 40, 8000 ile sınırla
        self.rpm = min(8000, int(self.hiz * 40))

    # ------------------ Motor Kontrol ------------------ #

    def motoru_ac(self):
        # 1) Yakıt yoksa raise ValueError
        if self.yakit <= 0:
            raise ValueError("Yakıt yok, motor açılamaz!")

        # 2) Motor sıcaklığı 150°C üzerindeyse kilitli
        if self.sicaklik >= 150:
            raise ValueError("Motor çok sıcak (>=150°C). Kilitlenmiş durumda, açılamaz!")

        # Motor açılırken turbo sıfırlanır, RPM 900 (rölanti)
        self.motor_acik = True
        self.turbo = 0
        self.rpm = 900
        print("Motor açıldı.")

    def motoru_kapat(self):
        # Hız 0 değilse hata
        if self.hiz > 0:
            raise ValueError("Hız 0 değilken motor kapatılamaz!")
        self.motor_acik = False

        # Basit soğuma simülasyonu
        self.turbo = 0
        self.rpm = 0
        self.sicaklik = max(20, self.sicaklik - 10)
        print("Motor kapatıldı, soğuma başladı.")

    # ------------------ Hız Artırma ------------------ #

    def hiz_arttir(self, miktar):
        # Motor kapalıysa çalışmaz
        if not self.motor_acik:
            print("Motor kapalıyken hız arttırılamaz!")
            return

        # Yakıt yoksa motor kapanır
        if self.yakit <= 0:
            print("Yakıt bitmiş, motor kapanıyor...")
            self.motor_acik = False
            return

        # Lastik tamamen aşınmışsa hızlanma yapılamaz
        if self.lastik <= 0:
            raise ValueError("Lastikler patlak! Hızlanma yapılamaz.")

        # Motor aşırı hasarlıysa (80%+) hızlanmayı engelleyebiliriz
        if self.hasar >= 80:
            print("Motor çok hasarlı (%80+). Hızlanma yapılamıyor.")
            return

        # Vites oranına göre temel hız artışı
        oran = self.vites_oranlari.get(self.vites, 1.0)
        temel_artis = miktar * oran

        # TCS ve patinaj koruması
        # Yol tutuşuna göre güvenli maksimum hız artışı
        max_guvenli_artis = self.yol_tutusu * 50  # keyfi bir model
        if self.tcs and temel_artis > max_guvenli_artis:
            print("TCS devrede: Patinaj engellendi, hız artışı sınırlandı.")
            temel_artis = max_guvenli_artis

        # Turbo gecikmesi – hizlanma varsa turbo yavaşça artar
        self.turbo_guncelle(hizlanma=True)

        # Turbo 70+ ise hız artışı %10 daha güçlü
        if self.turbo >= 70:
            temel_artis *= 1.10

        # Sıcaklık arttıkça performans düşsün
        if self.sicaklik >= 130:
            temel_artis *= 0.60  # %40 güç kaybı
            self.hasar += 5      # yüksek sıcaklık motoru hırpalar
            print("Aşırı sıcaklık (>=130°C)! Motor hasar alıyor.")
        elif self.sicaklik >= 110:
            temel_artis *= 0.80  # %20 güç kaybı
            print("Motor sıcak (>=110°C). Performans düşüyor.")

        # Yeni hız hesapla
        eski_hiz = self.hiz
        yeni_hiz = self.hiz + max(0, temel_artis)

        # Hasara göre dinamik max hız
        self.max_hiz = self._etkin_max_hiz()
        if yeni_hiz > self.max_hiz:
            print(f"Etkin maksimum hızı aştınız ({self.max_hiz:.0f} km/h). Hız sınırlandı.")
            yeni_hiz = self.max_hiz

        self.hiz = yeni_hiz
        self._guncelle_rpm()

        # RPM 8000'i geçerse hasar ve performans
        if self.rpm >= 8000:
            self.hasar += 5
            print("Aşırı devir! Motor hasar görüyor, performans düşüyor.")
            self.hiz *= 0.9  # performans düşüşü
            self._guncelle_rpm()

        # Yakıt tüketimi: hız + turbo + rpm'e bağlı olsun
        tuketim = (temel_artis * 0.03) + (self.turbo * 0.01) + (self.rpm / 10000)
        self.yakit -= tuketim
        if self.yakit < 0:
            self.yakit = 0

        # km güncelle – basit model
        self.km += max(0, self.hiz - eski_hiz) * 0.05

        # Lastik aşınması
        self.lastik_asinma(temel_artis)

        # Sıcaklık ve hasar güncellemeleri
        self.sicaklik_guncelle()
        self.hasar_guncelle()

        print(f"Hız artırıldı: {self.hiz:.1f} km/h | RPM: {self.rpm} | Turbo: {self.turbo:.1f} | "
              f"Sıcaklık: {self.sicaklik:.1f}°C | Yakıt: {self.yakit:.1f}L | Lastik: %{self.lastik:.1f}")

        if self.yakit == 0:
            print("Yakıt tamamen bitti! Motor kapanıyor.")
            self.motor_acik = False

    # ------------------ Hız Azaltma ------------------ #

    def hiz_azalt(self, miktar):
        eski_hiz = self.hiz
        yeni_hiz = max(0, self.hiz - miktar)

        # Ani fren (50+ km/h düşüş) → ABS devreye girsin
        if eski_hiz - yeni_hiz >= 50:
            self.abs_aktif = True
            print("Ani fren! ABS devrede.")
        else:
            self.abs_aktif = False

        # Fren sırasında TCS devre dışı
        self.tcs = False

        self.hiz = yeni_hiz
        self._guncelle_rpm()

        # Frenle birlikte hafif soğuma
        self.sicaklik = max(20, self.sicaklik - 0.5)

        print(f"Hız azaltıldı: {self.hiz:.1f} km/h | RPM: {self.rpm} | ABS: {'Aktif' if self.abs_aktif else 'Pasif'}")

    # ------------------ Vites ------------------ #

    def vites_yukselt(self):
        if self.vites >= 7:
            print("Zaten en yüksek vitestesiniz.")
            return

        # RPM 3000 üzerindeyken vites atılması idealdir.
        # RPM düşükken vites atılırsa motor zorlanabilir → sıcaklık + hasar
        if self.rpm < 3000:
            print("RPM düşükken vites yükselttiniz, motor hafif zorlandı.")
            self.sicaklik += 2
            self.hasar += 1

        self.vites += 1
        print(f"Vites yükseltildi: {self.vites}")

    def vites_dusur(self):
        if self.vites <= 1:
            print("Daha düşük vites yok.")
            return

        # Yüksek devirde vites düşürmek motoru zorlar
        if self.rpm > 5000:
            print("Yüksek devirde vites düşürdünüz, motor zorlanıyor!")
            self.sicaklik += 5
            self.hasar += 3

        self.vites -= 1
        print(f"Vites düşürüldü: {self.vites}")

    # ------------------ Turbo / Sıcaklık / Hasar / Lastik ------------------ #

    def turbo_guncelle(self, hizlanma=False):
        # Hız yüksek ve RPM yüksekse turbo yavaşça artsın, değilse düşsün
        if hizlanma and self.hiz > 80 and self.rpm > 3000:
            self.turbo += 3
        else:
            self.turbo -= 2

        # Sınırlar
        if self.turbo < 0:
            self.turbo = 0
        if self.turbo > 100:
            self.turbo = 100

        # Turbo 90+ ise motor sıcaklığını ekstra yükselt
        if self.turbo >= 90:
            self.sicaklik += 2

    def sicaklik_guncelle(self):
        if self.motor_acik:
            # hız + RPM doğrusal etki
            self.sicaklik += (self.hiz * 0.02) + (self.rpm / 10000)
        else:
            # motor kapalıysa soğuma
            self.sicaklik -= 1

        if self.sicaklik < 20:
            self.sicaklik = 20

        # 150°C üstü → motor arızası (raise)
        if self.sicaklik > 150:
            raise ValueError("Motor 150°C üzerine çıktı! Ciddi arıza oluştu.")

    def hasar_guncelle(self):
        # Hasar arttıkça maksimum hız düşmeli
        self.max_hiz = self._etkin_max_hiz()

        # %80 hasar → motor kapanmalı
        if self.hasar >= 80:
            print("Motor hasarı %80'in üzerinde! Motor zorunlu olarak kapatılıyor.")
            self.motor_acik = False

        if self.hasar > 100:
            self.hasar = 100

    def lastik_asinma(self, hizlanma_miktari):
        # Hızlanma + turbo lastiği aşındırır
        asinma = hizlanma_miktari * 0.02 + self.turbo * 0.01
        self.lastik -= asinma

        if self.lastik < 0:
            self.lastik = 0

        # %0 olunca hızlanma yapılamaz
        if self.lastik == 0:
            raise ValueError("Lastikler tamamen aşındı! Patlak durumda, araç kullanılamaz.")

    # ------------------ Görünüm (__str__) ------------------ #

    def __str__(self):
        motor_durum = "Açık" if self.motor_acik else "Kapalı"
        tcs_durum = "Aktif" if self.tcs else "Pasif"
        return (
            "-------------------------------------------------------\n"
            f"{self.marka} {self.model}\n"
            f"Hız: {self.hiz:.1f} km/h | Vites: {self.vites} | RPM: {self.rpm}\n"
            f"Turbo: {self.turbo:.1f} | Sıcaklık: {self.sicaklik:.1f}°C | Yakıt: {self.yakit:.1f}L\n"
            f"Motor Hasarı: %{self.hasar:.1f} | Lastik Durumu: %{self.lastik:.1f}\n"
            f"Motor: {motor_durum} | TCS: {tcs_durum}\n"
            "-------------------------------------------------------"
        )


# -------------------------------------------------------
# ÖRNEK TEST SENARYOSU (EĞİTİM AMAÇLI)
# -------------------------------------------------------
if __name__ == "__main__":
    araba = Araba("BMW", "M4 Competition", max_hiz=280)
    print(araba)

    araba.motoru_ac()
    araba.hiz_arttir(50)
    araba.vites_yukselt()
    araba.hiz_arttir(80)
    araba.hiz_azalt(60)
    araba.vites_dusur()
    print(araba)


# ------------------------------------------------------------
# AÇIKLAMA – EKSİK / HATALI OLAN NEYDİ, NASIL ÇÖZDÜK?
# ------------------------------------------------------------
# BAŞLANGIÇ DURUMU:
# - Sadece uzun bir gereksinim listesi vardı, HİÇ KOD YOKTU.
# - Yani:
#   * Sınıf tanımlı değildi
#   * motoru_ac, hiz_arttir, vites, turbo, ABS, TCS, lastik, hasar vb. yoktu
#
# NEDEN BU DURUM "HATALI/ EKSİK" SAYILIR?
# - Görev: "EXTREME / ULTRA seviye araç simülasyonu" istiyor.
# - Gerçekçi şekilde şu ilişkiler kurulmalıydı:
#   * hız ↔ vites ↔ RPM
#   * hız ↔ turbo ↔ sıcaklık ↔ hasar
#   * hız ↔ lastik aşınması ↔ TCS / ABS
#   * hasar & lastik ↔ maksimum hız
#   * motor durumu ↔ yakıt ↔ sıcaklık ↔ arıza (ValueError)
#
# NELER YAPTIK? (KISA ÖZET)
# 1) __init__ içinde tüm değişkenleri tanımladık:
#    - marka, model, hiz, max_hiz_taban, max_hiz, vites, vites_oranlari, rpm,
#      motor_acik, yakit, km, turbo, sicaklik, hasar, lastik, tcs, yol_tutusu, abs_aktif
#
# 2) motoru_ac():
#    - Yakıt yoksa ValueError fırlatıyor
#    - Sicaklik >= 150°C ise ValueError (kilitlenmiş motor)
#    - Motor açılırken turbo 0, rpm 900 olarak ayarlanıyor
#
# 3) motoru_kapat():
#    - Hız > 0 ise ValueError
#    - Motor kapalıyken turbo, rpm sıfırlanıyor, sıcaklık biraz düşüyor
#
# 4) hiz_arttir(miktar):
#    - motor kapalıysa çalışmıyor
#    - yakıt/lastik/hasar durumlarına göre güvenlik kontrolleri
#    - vites oranı hız artışını çarpan olarak etkiliyor
#    - TCS devredeyken patinajı sınırlıyor (maks güvenli hız artışı)
#    - turbo_guncelle() ile turbo yavaş artıyor; turbo 70+ olunca %10 ekstra güç
#    - sıcaklık yüksekse güç kaybı ve hasar artışı
#    - RPM güncelleniyor, 8000 üstünde ek hasar ve performans kaybı
#    - yakıt, hız+turbo+rpm’e göre tüketiliyor
#    - km artışı, lastik aşınması, sıcaklık ve hasar güncellemeleri yapılıyor
#
# 5) hiz_azalt(miktar):
#    - hız asla 0 altına düşmüyor
#    - 50+ km/h ani düşüşte ABS devreye giriyor
#    - fren sırasında TCS devre dışı bırakılıyor
#
# 6) vites_yukselt() / vites_dusur():
#    - 1–7 arası sınırlar
#    - RPM 3000 altı veya 5000 üzeri durumlarda sıcaklık/hasar cezaları
#
# 7) turbo_guncelle(), sicaklik_guncelle(), hasar_guncelle(), lastik_asinma():
#    - turbo, hız ve rpm’e bağlı artıp/azalıyor, 90+ turbo ekstra ısıtıyor
#    - sıcaklık, hız + rpm ile artıyor, 150°C üstü ValueError ile arıza
#    - hasar, dinamik max hız hesabına yansıyor, %80+ hasarda motor kapanıyor
#    - lastik aşınması hızlanma + turbo ile artıyor, %0’da ValueError ile “patlak lastik”
#
# 8) __str__():
#    - Örnekteki formatta, insan gözüne anlamlı bir durum özeti veriyor.
#
# Sonuç: Bu sınıf, verilen EXTREME/ULTRA gereksinimlerin tamamını pratik bir modelle
# karşılayan çözümlü bir versiyondur ve eğitim setindeki “final boss” olarak
# kullanılmaya uygundur.
# ------------------------------------------------------------
