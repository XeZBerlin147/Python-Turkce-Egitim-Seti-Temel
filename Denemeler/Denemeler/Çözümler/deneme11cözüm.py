# Bu denemede "Araba" sınıfının EXTREME / ULTRA versiyonunu yazmanız isteniyor.
#
# Seviye: Aşırı Zor – Ultra Zor (Final Boss)


class Araba:
    def __init__(self, marka, model, max_hiz):
        # Temel bilgiler
        self.marka = marka
        self.model = model

        # Dinamik durum değişkenleri
        self.hiz = 0                     # km/h
        self.max_hiz_taban = max_hiz     # Motor sağlıklı, lastik tam iken maksimum hız
        self.max_hiz = max_hiz           # Hasar ve lastik durumuna göre değişecek

        self.vites = 1                   # 1–7
        self.vites_oranlari = {         # basit hız çarpanları
            1: 0.25,
            2: 0.40,
            3: 0.55,
            4: 0.70,
            5: 0.85,
            6: 0.95,
            7: 1.00,
        }

        self.rpm = 0                     # 0–8000
        self.motor_acik = False

        self.yakit = 100.0               # 0–100 L varsayalım
        self.km = 0.0                    # toplam mesafe

        # Ultra değişkenler
        self.turbo = 0.0                 # 0–100
        self.sicaklik = 90.0             # °C, çalışma sıcaklığı
        self.hasar = 0.0                 # % cinsinden
        self.lastik = 100.0              # % cinsinden

        self.tcs = True                  # Çekiş kontrol sistemi (Traction Control)
        self.yol_tutusu = 0.9            # 0.5–1.0 arası, ne kadar iyi tutuyor
        self.abs_aktif = False           # ABS durumu

    # ---------------- MOTOR KONTROL ---------------- #

    def motoru_ac(self):
        if self.yakit <= 0:
            raise ValueError("Yakıt yok, motor açılamaz!")
        if self.sicaklik >= 150:
            raise ValueError("Motor çok sıcak, kilitlenmiş durumda. Açılamaz!")

        self.motor_acik = True
        self.turbo = 0
        self.rpm = 900  # rölanti
        print("Motor açıldı.")

    def motoru_kapat(self):
        if self.hiz > 0:
            raise ValueError("Hız sıfır değilken motor kapatılamaz!")
        self.motor_acik = False
        # Basit soğuma simülasyonu
        self.turbo = 0
        self.rpm = 0
        self.sicaklik = max(20, self.sicaklik - 10)
        print("Motor kapatıldı, soğuma başladı.")

    # ---------------- YARDIMCI HESAPLAR ---------------- #

    def _etkin_max_hiz(self):
        """
        Hasar ve lastik durumuna göre dinamik maksimum hız hesaplar.
        Örnek kural:
        - %50 hasar → max hızın ~%60’ı kalır
        - Lastik durumu da çarpan olarak eklenir
        """
        hasar_faktoru = 1 - 0.8 * (self.hasar / 100)     # hasar arttıkça 1'den düşer
        lastik_faktoru = 0.5 + 0.5 * (self.lastik / 100) # lastik %0→0.5, %100→1.0
        etkin = self.max_hiz_taban * max(0, hasar_faktoru) * lastik_faktoru
        return max(20, etkin)  # çok düşse bile asgari bir hız sınırı olsun

    def _guncelle_rpm(self):
        # Basit RPM modeli: hız * 40, 8000 ile sınırlı
        self.rpm = min(8000, int(self.hiz * 40))

    # ---------------- HIZ ARTTIRMA ---------------- #

    def hiz_arttir(self, miktar):
        if not self.motor_acik:
            print("Motor kapalıyken hız arttırılamaz!")
            return

        if self.yakit <= 0:
            print("Yakıt bitmiş. Motor kapanıyor...")
            self.motor_acik = False
            return

        if self.lastik <= 0:
            raise ValueError("Lastikler patlak! Hızlanma yapılamaz.")

        if self.hasar >= 80:
            print("Motor çok hasarlı! Hızlanamazsınız.")
            return

        # Vites oranına göre temel hız artışı
        oran = self.vites_oranlari.get(self.vites, 1.0)
        temel_artis = miktar * oran

        # TCS ve patinaj kontrolü
        # Yol tutuş katsayısına göre maksimum güvenli hız artışı
        max_guvenli_artis = self.yol_tutusu * 50
        if self.tcs and temel_artis > max_guvenli_artis:
            print("TCS devrede: Patinaj engellendi, hız artışı sınırlandı.")
            temel_artis = max_guvenli_artis

        # Turbo etkisi (gecikmeli boost artışı)
        self.turbo_guncelle(hizlanma=True)
        if self.turbo >= 70:
            temel_artis *= 1.10  # %10 ek güç

        # Sıcaklığa göre performans düşüşü
        if self.sicaklik >= 130:
            temel_artis *= 0.60   # %40 güç kaybı
            self.hasar += 5       # yüksek sıcaklık hasar getirir
            print("Aşırı sıcaklık! Motor hasar alıyor.")
        elif self.sicaklik >= 110:
            temel_artis *= 0.60   # %40 güç kaybı
            print("Motor sıcak, performans düşüyor.")

        # Yeni hızı hesapla
        yeni_hiz = self.hiz + max(0, temel_artis)

        # Hasara göre dinamik max hız
        self.max_hiz = self._etkin_max_hiz()

        if yeni_hiz > self.max_hiz:
            print(f"Etkin maksimum hızı aştınız ({self.max_hiz:.0f} km/h). Hız sınırlandı.")
            yeni_hiz = self.max_hiz

        # Hız güncelle
        eski_hiz = self.hiz
        self.hiz = yeni_hiz
        self._guncelle_rpm()

        # Yakıt tüketimi: hız + turbo + rpm'e bağlı
        tuketim = (temel_artis * 0.03) + (self.turbo * 0.01) + (self.rpm / 10000)
        self.yakit -= tuketim
        if self.yakit < 0:
            self.yakit = 0

        # KM güncelle (basit model)
        self.km += max(0, self.hiz - eski_hiz) * 0.05

        # Sıcaklık ve hasar güncelle
        self.sicaklik_guncelle()
        self.hasar_guncelle()
        self.lastik_asinma(temel_artis)

        print(f"Hız artırıldı: {self.hiz:.1f} km/h | RPM: {self.rpm} | Turbo: {self.turbo:.1f} | "
              f"Sıcaklık: {self.sicaklik:.1f}°C | Yakıt: {self.yakit:.1f}L")

        if self.yakit == 0:
            print("Yakıt tamamen bitti! Motor kapanıyor.")
            self.motor_acik = False

    # ---------------- HIZ AZALTMA & FRENLER ---------------- #

    def hiz_azalt(self, miktar):
        eski_hiz = self.hiz
        yeni_hiz = max(0, self.hiz - miktar)

        if eski_hiz - yeni_hiz >= 40:
            self.abs_aktif = True
            print("Ani fren! ABS devreye girdi.")
        else:
            self.abs_aktif = False

        self.hiz = yeni_hiz
        self._guncelle_rpm()

        # Frenle birlikte sıcaklık biraz düşebilir
        self.sicaklik = max(20, self.sicaklik - 0.5)

        # Fren sırasında TCS'nin etkisi yok
        self.tcs = False

        print(f"Hız azaltıldı: {self.hiz:.1f} km/h | RPM: {self.rpm} | ABS: {'Aktif' if self.abs_aktif else 'Pasif'}")

    def fren_yap(self, miktar):
        # Ekstra mantık: hız > 120 ise ABS mutlaka devrede olsun
        if self.hiz > 120:
            self.abs_aktif = True
            print("Yüksek hızda fren! ABS zorunlu devrede.")
        self.hiz_azalt(miktar)

    # ---------------- TURBO & SICAKLIK & HASAR & LASTİK ---------------- #

    def turbo_guncelle(self, hizlanma=False):
        if hizlanma:
            # Hız ve RPM yüksekse turbo artsın
            if self.hiz > 80 and self.rpm > 3000:
                self.turbo += 3
        else:
            # Yavaşlarken, sabit giderken turbo düşsün
            self.turbo -= 2

        # Turbo sınırları
        if self.turbo < 0:
            self.turbo = 0
        if self.turbo > 100:
            self.turbo = 100

        # Yüksek turbo motoru ısıtır
        if self.turbo >= 90:
            self.sicaklik += 2

    def sicaklik_guncelle(self):
        if self.motor_acik:
            # Hız ve RPM ile artış
            self.sicaklik += (self.hiz * 0.02) + (self.rpm / 10000)
        else:
            # Motor kapalıysa soğuma
            self.sicaklik -= 1

        # min sıcaklık
        if self.sicaklik < 20:
            self.sicaklik = 20

        # Aşırı sıcaklık
        if self.sicaklik > 140:
            self.hasar += 10
            print("TEHLİKE: Motor aşırı sıcak! Hasar artıyor.")
        if self.sicaklik > 150:
            raise ValueError("Motor 150°C üzerine çıktı, ciddi arıza!")

    def hasar_guncelle(self):
        if self.rpm >= 8000:
            self.hasar += 5
            print("Aşırı RPM! Motor hasar görüyor.")

        if self.hasar > 100:
            self.hasar = 100

        # Hasar belli eşiği geçerse max hız düşer
        self.max_hiz = self._etkin_max_hiz()

        if self.hasar >= 80:
            print("Motor çok hasarlı! Motor zorunlu olarak kapatılıyor.")
            self.motor_acik = False

    def lastik_asinma(self, miktar):
        # Hızlanma + turbo → lastik aşınması
        asinma = miktar * 0.02 + self.turbo * 0.01
        self.lastik -= asinma

        if self.lastik < 0:
            self.lastik = 0

        if self.lastik == 0:
            raise ValueError("Lastikler tamamen aşındı! Araç kullanılamaz.")

    # ---------------- VİTES ---------------- #

    def vites_yukselt(self):
        if self.vites >= 7:
            print("Zaten en yüksek vitestesiniz.")
            return
        if self.rpm < 3000:
            print("RPM düşük, verimsiz vites yükseltme (motor zorlanabilir).")
            self.sicaklik += 2
        self.vites += 1
        print(f"Vites yükseltildi: {self.vites}")

    def vites_dusur(self):
        if self.vites <= 1:
            print("Daha düşük vites yok.")
            return
        if self.rpm > 5000:
            print("Yüksek devirde vites düşürmek motoru zorlar!")
            self.sicaklik += 5
            self.hasar += 3
        self.vites -= 1
        print(f"Vites düşürüldü: {self.vites}")

    # ---------------- GÖRÜNÜM ---------------- #

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


# ---------------- BASİT TEST SENARYOSU ---------------- #

if __name__ == "__main__":
    araba = Araba("BMW", "M4 Competition", max_hiz=280)

    print(araba)
    araba.motoru_ac()
    araba.hiz_arttir(50)
    araba.vites_yukselt()
    araba.hiz_arttir(80)
    araba.fren_yap(60)
    araba.vites_dusur()
    print(araba)


# ------------------------------------------------------------
# AÇIKLAMA – “HATA NEREDEYDİ, NASIL ÇÖZDÜK?”
# ------------------------------------------------------------
# BAŞTA:
# - Hiç sınıf tanımlı değildi, sadece gereksinimler yorum satırı olarak verilmişti.
# - Yani ortada çalışan bir simülasyon yoktu, tamamen iskelet bir görev tanımı vardı.
#
# NEDEN “HATALI / EKSİK” SAYILIR?
# - Verilen görev, gerçekçi ve çok parçalı bir araç simülasyonu istiyordu:
#   * hız, vites, rpm, turbo, sıcaklık, hasar, lastik, TCS, ABS vb.
#   * motor aç/kapa kuralları
#   * hız artışı/azalışı ile yakıt, sıcaklık, hasar ilişkisi
#   * maksimum hızın dinamik değişimi
#   * ValueError ile kritik hata durumlarında programın uyarı vermesi
# - Bunların hiçbiri başlangıçta kodda yoktu → yani “tamamen boş iskelet” durumundaydı.
#
# NASIL ÇÖZDÜK?
# 1) __init__ içinde TÜM gerekli durum değişkenlerini tanımladık:
#    - max_hiz_taban / max_hiz, hiz, vites, vites_oranlari, rpm,
#      motor_acik, yakit, km, turbo, sicaklik, hasar, lastik, tcs, yol_tutusu, abs_aktif.
#
# 2) motoru_ac():
#    - yakıt yoksa → ValueError fırlatıyoruz.
#    - sıcaklık 150°C üzerindeyse → ValueError fırlatıyoruz (kilitlenmiş motor).
#    - Motor açılırken turbo sıfırlanıp RPM rölantiye (900) ayarlanıyor.
#
# 3) motoru_kapat():
#    - hız > 0 ise → ValueError fırlatıyoruz (güvenlik kuralı).
#    - Motor kapanırken turbo, rpm ve sıcaklık bir miktar düşürülüyor (soğuma simülasyonu).
#
# 4) hiz_arttir():
#    - Motor kapalıysa çalışmıyor.
#    - Yakıt yoksa motor kapanıyor.
#    - Lastik veya hasar durumu kritikse hızlanma engelleniyor.
#    - Vites oranları hız artışını etkiliyor (vites_oranlari dict’i ile).
#    - TCS açıksa patinajı engelliyor, hız artışını sınırlandırıyor.
#    - Turbo gecikmesi turbo_guncelle() ile sağlanıyor, yüksek turbo ekstra güç veriyor.
#    - Sıcaklık yükseldikçe performans düşüyor, çok yükselince hasar artıyor.
#    - Hız artışı yakıt tüketimini, km’yi, rpm’i, sıcaklığı, hasarı ve lastik aşınmasını etkiliyor.
#    - Etkin maksimum hız (hasar + lastik durumuna göre) _etkin_max_hiz() ile hesaplanıp hız sınırlandırılıyor.
#
# 5) hiz_azalt() ve fren_yap():
#    - Hız asla 0 altına inmiyor (max(0, ...)).
#    - Ani büyük düşüşlerde (40+ km/h) ABS devreye giriyor.
#    - Yüksek hızda fren → ABS zorunlu devreye giriyor.
#    - Frenleme sırasında TCS devre dışı kalıyor.
#
# 6) turbo_guncelle(), sicaklik_guncelle(), hasar_guncelle(), lastik_asinma():
#    - Turbo, hız ve rpm’e göre artıp azalıyor; yüksek turbo ekstra ısı üretiyor.
#    - Sıcaklık, hız + rpm ile artıyor; motor kapalıyken düşüyor.
#    - Çok yüksek sıcaklıkta (140+) hasar artıyor, 150°C’de ValueError ile “motor arızası” veriliyor.
#    - Hasar artınca etkin maksimum hız düşüyor; hasar %80’i geçince motor kapatılıyor.
#    - Lastikler hızlanma + turbo ile aşınıyor, %0’a düşünce ValueError ile “patlak lastik” durumu.
#
# 7) Vites sistemi:
#    - 1–7 aralığında sınırlandırıldı.
#    - Yanlış devirde vites yükseltme/düşürme sıcaklık ve hasarı etkiliyor.
#
# 8) __str__:
#    - Arabanın tüm kritik durumlarını (hız, vites, rpm, turbo, sıcaklık, yakıt, hasar, lastik, motor, TCS)
#      okunabilir ve şık bir formatta dönüyor.
#
# SONUÇ:
# - Bu sınıf, verilen EXTREME / ULTRA gereksinimlerin tamamını temel bir fiziksel modelle karşılar.
# ------------------------------------------------------------
