# Bu denemede "Araba" sınıfının EXTREME bir versiyonunu yazmanız isteniyor.

# Seviye: Aşırı Zor

# Artık arabada:
# ------------------------------------------------------------
# - hız
# - maksimum hız
# - vites (1–7 arası)
# - vites oranları (ör: 1 → 0.25, 7 → 1.0)
# - motor açık/kapalı
# - yakıt
# - km
# - motor sıcaklığı
# - motor hasarı (%)
# - turbo basıncı (0–100)
#
# Ek sistemler:
# - ABS fren sistemi
# - aşırı hız uyarı sistemi
# - turbo gecikmesi (boost yavaş yükselir)
# - motor sıcaklığı artışı ve soğuma mantığı
# - sıcaklık çok yükselirse performans düşüşü
# - motor hasarı arttıkça hız kapasitesi düşer
# - ani fren → ABS devreye girer
#
# ------------------------------------------------------------
# GEREKSİNİMLER (detaylı):
#
# 1) motoru_ac()
#    - yakıt yoksa açılamaz (raise)
#    - sıcaklık < 120 olmalı (koruma)
#
# 2) motoru_kapat()
#    - hız > 0 ise hata fırlatılmalı
#
# 3) hiz_arttir(deger)
#    - motor kapalıysa çalışmaz
#    - hız maksimum sınırı geçemez
#    - turbo gecikmesi: hız artırıldıkça turbo yavaşça artar
#    - turbo 70+ ise hız artışı %10 daha güçlü olsun
#    - sıcaklık arttıkça performans düşsün:
#         sıcaklık >= 110 → hız artışı %40 düşsün
#         sıcaklık >= 130 → motor hasarı artsın
#    - yakıt tüketimi hız ve turbo’ya göre hesaplansın
#    - km güncellensin
#
# 4) hiz_azalt(deger)
#    - hız 0 altına inemez
#    - ani düşüş (40 km/h üzeri) olursa ABS devreye girsin ve uyarı versin
#
# 5) fren_yap(deger)
#    - hız > 120 ise ABS devreye girsin
#    - fren etkisi hızla bağlantılı
#
# 6) turbo_guncelle()
#    - hız düşükse turbo yavaşça düşsün
#    - hız yüksekse turbo yavaşça artsın
#
# 7) sicaklik_guncelle()
#    - hız arttıkça sıcaklık artmalı
#    - hız düşükse yavaş yavaş soğumalı
#    - sıcaklık 140'ı geçerse motor hasarı artmalı (tehlike modu)
#
# 8) hasar_guncelle()
#    - motor hasarı arttıkça maksimum hız düşmeli
#      ör: %20 hasar → maksimum hız %10 düşer
#
# 9) vites_yukselt(), vites_dusur()
#    - 1–7 arası sınırlar
#    - vites oranları hız artışını etkiler
#
# 10) __str__ override:
#     Örn:
#     BMW M4 | Hız: 155 km/h | Vites: 5 | Sıcaklık: 103°C |
#     Turbo: 41 | Hasar: %3 | Yakıt: 72L | Motor: Açık
#
# ------------------------------------------------------------
# BURAYI TAMAMLAYIN.
# Bu denemede EXTREME seviye bir “Araba Simülasyonu” yazmanız isteniyor.

# Seviye: Ultra Zor (12. Deneme – Eğitim Seti Final Boss+)

# Bu görev, gerçek bir araç dinamiğini simüle eden çok parçalı bir sistemdir.

###################################################################
#                         GEREKSİNİMLER                           #
###################################################################

# Temel değişkenler:
# - marka
# - model
# - hız (0 – dinamik max hız arası)
# - maksimum hız (motor sıcaklığı + hasar + lastik durumu ile değişen)
# - vites (1–7)
# - vites oranları (her vites için hız yükseltme çarpanı)
# - devir (RPM, 0–8000)
# - motor_acik (bool)
# - yakıt (0–100)
# - km
#
# Yeni değişkenler (Ultra):
# - turbo basıncı (0–100)
# - motor sıcaklığı (°C)
# - motor hasarı (%)
# - lastik durumu (%)
# - çekiş kontrolü (TCS)
# - yol tutuş katsayısı (0.5–1.0)
# - kalkışta patinaj simülasyonu
#
# ---------------------------------------------------------------
# Sistemler:
# ---------------------------------------------------------------

# 1) motoru_ac()
#    - Yakıt yoksa raise ValueError
#    - Motor sıcaklığı 150°C üzerindeyse motor kilitlenmeli (açılamaz)
#    - Motor açılırken turbo sıfırlanmalı, RPM 900 olmalı

# 2) motoru_kapat()
#    - Hız 0 değilse raise
#    - Motor kapanınca turbo, RPM, sıcaklık düşüş başlasın (yapay bir soğuma simülasyonu)

# 3) hiz_arttir(miktar)
#    - Motor kapalıysa çalışmaz
#    - Vites oranı → hız artışına etki edecek
#    - Turbo gecikmesi (boost) → hız artışına % katkı sağlar
#    - TCS (çekiş kontrol) devredeyse patinaj engellenmeli:
#        Eğer hız artışı *lastik tutuş katsayısından* fazla ise,
#        TCS devreye girip hız artışını sınırlandırır.
#    - Sıcaklık arttıkça motorun güç verimi DÜŞMELİ:
#         110°C → %20 güç kaybı
#         130°C → %40 güç kaybı
#         150°C → motor hasarı artmalı (tehlike)
#    - RPM dinamik şekilde artmalı (ör: hız * 40)
#    - RPM 8000'i geçerse motor hasarı artmalı, ayrıca performans düşmeli
#    - Yakıt tüketimi hız + turbo + RPM'e bağlı olmalı
#    - km güncellenmeli
#    - Lastik durumu her hızlanmada aşınmalı

# 4) hiz_azalt(miktar)
#    - hız asla 0 altına inemez
#    - Ani fren (50+ km düşüş) varsa ABS devreye girsin
#    - TCS devre dışı kalmalı fren sırasında
#    - RPM hızla birlikte düşmeli

# 5) vites_yukselt() / vites_dusur()
#    - RPM 3000 üzerindeyken vites atılabilir
#    - Yanlış vites → motor zorlaması → sıcaklık artışı + hasar

# 6) turbo_guncelle()
#    - Hız yüksek ve RPM yüksekse turbo yavaşça artsın
#    - Hız düşükse turbo düşsün
#    - Turbo 90+ ise motor sıcaklığı ekstra yükselsin

# 7) sicaklik_guncelle()
#    - Hız + RPM doğrusal etkilesin
#    - Motor kapalıysa yavaş soğuma
#    - 150°C üstü → motor arızası (raise)

# 8) hasar_guncelle()
#    - Hasar arttıkça maksimum hız düşmeli
#    - %50 hasar → Max hızın %40’ı gider
#    - %80 hasar → Motor kapanmalı (zorunlu)

# 9) lastik_asinma()
#    - Hızlanma + turbo lastiği aşındırır
#    - %0 olunca hızlanma yapılamaz (patlak lastik → raise)

# 10) __str__ zorunlu:
#     Ör:
#     -------------------------------------------------------
#     BMW M4 Competition
#     Hız: 142 km/h | Vites: 5 | RPM: 6800
#     Turbo: 45 | Sıcaklık: 107°C | Yakıt: 61L
#     Motor Hasarı: %12 | Lastik Durumu: %73
#     Motor: Açık | TCS: Aktif
#     -------------------------------------------------------


###################################################################
#                          BURAYI TAMAMLAYIN                       #
###################################################################
