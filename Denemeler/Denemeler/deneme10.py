# Bu denemede gelişmiş bir "Araba" sınıfı oluşturmanız isteniyor.

# Seviye: Çok Zor

# Gereksinimler:
# ------------------------------------------------------
# 1) Değişkenler:
#    - marka
#    - model
#    - hız (varsayılan 0)
#    - maksimum hız
#    - vites (1–6 arası)
#    - motor_acik (True/False)
#    - yakit (0–100 arası)
#    - km (katedilen toplam mesafe)

# 2) Fonksiyonlar:
#    - motoru_ac()
#    - motoru_kapat()  (hız 0 değilse kapatılamaz)
#
#    - hiz_arttir(miktar)
#         * motor kapalıysa arttırılamaz
#         * hız maksimum hızı geçemez
#         * hız vites aralığını aşarsa uyarı versin
#           ancak yine de hız uygulansın
#         * hız arttıkça yakıt tüketilsin (formülü size kalmış)
#
#    - hiz_azalt(miktar)
#         * hız 0 altına inemez
#
#    - vites_yukselt()
#         * 6’dan büyük olamaz
#
#    - vites_dusur()
#         * 1’den küçük olamaz
#
#    - bilgi() veya __str__()
#         Araba bilgilerini güzel formatta döndürsün:
#         Ör:
#         "BMW M4 | Hız: 120 km/h | Vites: 4 | Yakit: 73 | Motor: Açık"

# 3) Ek Gereksinimler:
# ------------------------------------------------------
# - Her hız arttırmada km sayacı artmalı
# - Eğer yakıt 0 olursa hız arttırılamaz ve motor kapanır
# - Eğer hız 0’dan büyükse vites 0 olamaz (koruma)
# - Eğer kullanıcı aşırı hız yapıyorsa bir uyarı basılabilir
#
# 4) Çok önemli:
#    - Kod içinde en az 1 yerde ValueError raise edin.
#    - __str__ override zorunludur.
#
# ------------------------------------------------------
# BURAYI TAMAMLAYIN.
