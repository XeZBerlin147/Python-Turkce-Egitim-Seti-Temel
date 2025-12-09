# Bu denemede EXTREME seviye bir “Araba Simülasyonu” yazmanız isteniyor.

# Seviye: Ultra Zor

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
